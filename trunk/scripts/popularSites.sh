#!/bin/bash

SITES=('my.opera.com' 'people.tribe.net' 'livejournal.com' 'ecademy.com' 'linkedin.com' 'kwark.org' 'elgg.net' 'w3.org')


echo Popular Sites:
echo -------------

for site in ${SITES[@]}; do
    NUMBER=$(cat log/futil.log | grep pinged | grep -c $site)
    echo  - $site: $NUMBER
done