#!/usr/bin/env bash


# All script path locations are relative to HERE
HERE=$(realpath $( dirname ${BASH_SOURCE[0]}))

echo "here is $HERE"

generators_dir=$HERE/source/generators

for gen in $generators_dir/generate_* ; do
echo "Running $gen"
python $gen
done
