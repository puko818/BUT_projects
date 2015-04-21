###########
#Batch for gnuplot visualisation and coupling conditions with file names
###########
#!/bin/bash

files=(*.txt)
conditions=(cts1 ctr1 cts2 ctr2 cts3 ctr3 cus1 cur1 cus2 cur2 cus3 cur3 cts4 ctr4 cts5 ctr5 cts6 ctr6 zns1 znr1 zns2 znr2 zns3 znr3 cts7 ctr7 cts8 ctr8 cts9 ctr9 cds1 cdr1 cds2 cdr2 cds3 cdr3)

for ((i = 0; i < ${#files[@]} && i < ${#conditions[@]}; i++))
do
  f=${files[i]%*.txt}
  cat ${files[i]} | awk '$2<1360 {print $2,$3}' | awk 'BEGIN{size=5} {mod=NR%size; if(NR<=size){count++}else{sum-=array[mod]};sum+=$1;array[mod]=$3;print $2,sum/count}' > $f".gp"
  awk 'BEGIN{size=5} {mod=NR%size; if(NR<=size){count++}else{sum-=array[mod]};sum+=$1;array[mod]=$1;print sum/count}'
  echo $f
  gnuplot -e "filename='$f'" -e "condition='${conditions[i]}'"  script.gnuplot
  
done



#batch converting to csv files (delimited with ";") amd preserving the header unchanged
for ((i = 0; i < ${#files[@]} && i < ${#conditions[@]}; i++))
do
    echo "${files[i]}" "${conditions[i]}"
    echo  "${conditions[i]}" | cat - "${files[i]}" | awk  'BEGIN {OFS=";"} {if (NR==0) print; else print  $2,$1}'  > temp && mv temp "${files[i]}"
done

