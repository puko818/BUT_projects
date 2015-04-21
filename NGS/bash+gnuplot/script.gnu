#!/usr/bin/gnuplot 
reset
#set terminal png truecolor size 1024,500
set terminal pdf
#set output filename.'.png'
set output filename.'.pdf'
unset key
set size ratio 0.25
set xrange [0:1360]
#set yrange [-860:860]
set style line 1 lc rgb 'black' pt 7
set title condition
#plot filename  with points ls 1 ps 0.5
#plot filename.'.gp'  with lines ls 1 pt 0.5
plot filename.'.gp' with lines
#pause -1
