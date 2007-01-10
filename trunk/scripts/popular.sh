#!/bin/sh

cat log/futil.log | grep "exists on db" |  awk '{ print $5}' | sort | uniq -c | sort -nr > data/popular.dat

echo `wc -l data/popular.dat`
