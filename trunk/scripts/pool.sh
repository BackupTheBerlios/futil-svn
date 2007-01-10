#!/bin/sh

cat log/futil.log | grep "URIs pending to visit" | awk '{print $4}' | cat -n > data/pool.data

gnuplot << EOF
set terminal postscript eps color enhanced
set output "data/pool.eps"
set xlabel "URIs visited (x100)"
set ylabel "URIs pending to visit"
set grid
plot "data/pool.data" using 1:2 with lines title "futil pool size"
save "data/pool.plt"
EOF

evince data/pool.eps &

