#!/bin/bash
######
#Script for normalizing the sRNA-read counts related to Ogre Transposable Elements (Kubat et al)
#Input: raw alignment (from MicroRazers)
#Output: normalized and averaged (sliding window) 
######
module add python-2.6.2

#paths to library size and TE copy-number information
LIBR=libraries.txt
COPYN=copy_numbers.txt

sliding_window()
{
  data=$(</dev/stdin)
  echo "$data"| awk 'NR>2 {print}'|  awk -v window="$1" 'BEGIN{size=window} {mod=NR%size; if(NR<=size){count++}else{sum-=array[mod]};sum+=$2;array[mod]=$2;print $1,sum/count}'
}


#Parameters
#1-copy_numbers
#2-lib_size
normalize() 
{
 data=$(</dev/stdin)
 libsize=`cat $LIBR |  awk -F ":" -v dataset="$1" ' $1==dataset {print $2}'`
 copynumber=`cat $COPYN | awk -F ":" -v element="$2" '$1==element {print $2}'`
 factor=`echo "(5*10^10)/($libsize*$copynumber)" | bc -l`
 echo "$data" | awk -v factor="$factor" '{print $1,$2*factor}'
}

add_origin()
{
 data=$(</dev/stdin)
 echo "$data" | awk 'BEGIN {print 0,0} {print}'
}



for i in  1.0 2.0 3.0 4.0 5.0
do
 python ../join.py <(cat Ogre_CL5_267_LTR*$i | awk '{print int(($1/18333)*1000),$2}'  | sort -u -k1,1n   | awk '$1<=114 {print}') <(cat Ogre_CL5_277_LTR*$i |  awk '{print int(($1/19565)*1000),$2}' |  sort -u -k1,1n | awk '$1<=124  {print}')  |  normalize $i CL5 | add_origin | sliding_window 15  > CL5.hits.$i
 python ../join.py <(cat Retand-1*LTR*$i |  awk '{print int(($1/3680)*1000),$2}' | sort -u -k1,1n | awk '$1<=166 {print}') <(cat Retand-2*LTR*$i | awk '{print int(($1/11064)*1000),$2}' | sort -u -k1,1n | awk '$1<=53 {print}')  |  normalize $i Retand | add_origin | sliding_window 15  > Retand.hits.$i
 cat *CL11*$i | awk '{print int(($1/18328)*1000),$2}'  | sort -u -k1,1n | awk '$1<=131 {print}' |   normalize $i CL11 | add_origin |  sliding_window 15 > CL11.hits.$i
 cat *CL6*$i |  awk '{print int(($1/19658)*1000),$2}'  | sort -u -k1,1n | awk '$1<=125 {print}'  |  normalize $i CL6 | add_origin |  sliding_window 15 > CL6.hits.$i
done




