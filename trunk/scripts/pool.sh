#!/bin/sh

cat log/futil.log | grep "to visit" | awk '{print $4}' | cat -n > data/pool.data

gnuplot << EOF
set terminal postscript eps color enhanced
set output "data/pool.eps"
set xlabel "URIs visited (x100)"
set ylabel "URIs pending to visit"
set title "futil pool size"
plot "data/pool.data" using 1:2 with lines
EOF

evince data/pool.eps &

