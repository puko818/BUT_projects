#!/bin/bash
#PBS -N sRNA_to_mRNA
#PBS -l walltime=1d
#PBS -l nodes=1:ppn=30
#PBS -l mem=50gb
#PBS -l scratch=500mb
#PBS -j oe
##instructions for the computer cluster (resource constraints)
module add fastx-0.0.13
module add bowtie2-2.2.3

##########################################################
##script running the sRNA reads alignment to mRNA
##########################################################

#simple queuing system assuring only $MAX_NPROC processes will be run in parallel
NUM=0
QUEUE=""
MAX_NPROC=30 # default
REPLACE_CMD=0 # no replacement by default
  
function queue {
    QUEUE="$QUEUE $1"
    NUM=$(($NUM+1))
}
 
function regeneratequeue {
    OLDREQUEUE=$QUEUE
    QUEUE=""
    NUM=0
    for PID in $OLDREQUEUE
    do
        if [ -d /proc/$PID  ] ; then
            QUEUE="$QUEUE $PID"
            NUM=$(($NUM+1))
        fi
    done
}
 
function checkqueue {
    OLDCHQUEUE=$QUEUE
    for PID in $OLDCHQUEUE
    do
        if [ ! -d /proc/$PID ] ; then
            regeneratequeue # at least one PID has finished
            break
        fi
    done
}


#array of commands to be run
ary=( )

outputdir=/storage/ostrava1/home/ivogel/SL_sRNA_to_mRNA


#loop generating command string that is added to ${ary} and subsequently to a queue
for d in /storage/ostrava1/home/ivogel/SL_RNA_seq_To_Genomic/results/[1-5]erne*/
do
  cd $d
  prefix=`basename $d`
  prefix=`echo $prefix | cut -c1`
  suffix=`basename $d | cut -d'_' -f2`
  for i in *
  do 
    for j in /storage/brno2/home/ivogel/small_rna/clustering/representatives/*001.fa
     do
     
      dataset=`basename $j | cut -d'_'  -f1`
      ##reffile=`echo ${i%*.fasta}"DB"`
      outputfilename=$prefix$suffix"_"$i"_"$dataset"_erne"
      #only 1M1,2F2,3F3,4F4,5M5
      echo $outputfilename |  egrep "([0-9]).*\1_erne"|  egrep   "1M|2F|3F|4F|5M" | egrep -v  "NONTE"
      if [ $? -eq 0 ]; then
       ##bowtie2 -x  $reffile -L 15 -p 4 -U $j  -S $outputdir/$outputfilename &  <-bowtie variant
       ary+=("/storage/ostrava1/home/ivogel/progs/MicroRazerS/micro_razers64 $d$i $j -o $outputdir/$outputfilename &")
      fi
      #ary+=("$cmd")
      #echo $cmd
    done
  #wait
    done
  cd ..
done


 
#run the queue
for CMD in "${ary[@]}"
do
    echo $CMD
    eval "$CMD"
    PID=$!
    queue $PID
 
    while [ $NUM -ge $MAX_NPROC ]; do
        checkqueue
        sleep 0.4
    done
done
wait # wait for all processes to finish before exit




