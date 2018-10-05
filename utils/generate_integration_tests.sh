#!/usr/bin/env bash

if [[ "$1" == "" ]] ; then
echo Must provide target dir
exit 1
fi


# All script path locations are relative to HERE
HERE=$(realpath $( dirname ${BASH_SOURCE[0]}))

echo "here is $HERE"

# Target dir is relative to cwd
target_dir=$(realpath "$1")

if [[ $target_dir == "" ]] ; then
echo "No target directory given. Exiting"
exit 1
fi

if [[ ! -d $target_dir ]] ; then
echo "$target_dir does not exist. Will create."
mkdir -p $target_dir
fi

# Copy skeletons to target dir
rsync -avP $HERE/source/skeleton/ $target_dir

# Generate direct integration tests
cd $HERE/source/generate_integration_tests

for file in netscaler_*.py ; do
module=${file%.py}

python generate_integration_test.py \
--module $module \
--test-type netscaler_direct_calls \
--dir-path $target_dir/netscaler_direct_calls/roles

done

cd -

# Use the transpile script to generate the mas proxy calls
python ${HERE}/transpile_integration_tests_to_mas.py \
--source ${target_dir}/netscaler_direct_calls/roles \
--target ${target_dir}/netscaler_mas_proxied_calls/roles
