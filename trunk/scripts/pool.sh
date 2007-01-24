#!/bin/sh

cat log/futil.log | grep "URIs pending to visit" | awk '{print $4}' | cat -n > data/pool.data

gnuplot << EOF
set terminal png 
set output "data/pool.png"
set size 1.5, 1.5
set xlabel "URIs visited (x100)"
set ylabel "URIs pending to visit"
set grid
plot "data/pool.data" using 1:2 with lines title "futil pool size"
save "data/pool.plt"
EOF

#gqview data/pool.png &

