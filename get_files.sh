#!/bin/bash

if [ $# -eq 0 ]
  then
    printf -v usage 'usage: %s number_of_images' "$0"
    echo $usage
    exit 1
fi

for i in $(eval echo {1..$1})
do
  printf -v filename '%04d.jpg' "$i"
  wget https://picsum.photos/400 -O $filename
done
