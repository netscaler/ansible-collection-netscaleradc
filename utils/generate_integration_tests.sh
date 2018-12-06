#!/usr/bin/env bash

set -e

if [[ "$1" == "" ]] ; then
echo Must provide target dir
exit 1
fi

if [[ "$2" != "" ]] ; then
NS_VERSION="$2"
else
NS_VERSION="12.1"
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

DIRECT_CALLS_ROLE_FILE=$target_dir/citrix_adc_direct_calls/citrix_adc.yaml
mkdir -p $(realpath $(dirname $DIRECT_CALLS_ROLE_FILE))

touch $DIRECT_CALLS_ROLE_FILE

echo "---

- hosts: citrix_adc

  gather_facts: no
  connection: local

  vars:
    limit_to: \"*\"
    debug: false

  roles:" > $DIRECT_CALLS_ROLE_FILE

for file in citrix_adc_*.py ; do
module=${file%.py}


    echo "    - { role: $module, when: \"limit_to in ['*', '$module']\" }" >> $DIRECT_CALLS_ROLE_FILE 

    python generate_integration_test.py \
    --module $module \
    --test-type citrix_adc_direct_calls \
    --ns-version $NS_VERSION \
    --dir-path $target_dir/citrix_adc_direct_calls/roles
    
done
    #TODO: complete the mas_api integratin tests generation
    
    #python generate_integration_test.py \
    #--module $module \
    #--test-type mas_proxied_calls \
    #--ns-version $NS_VERSION \
    #--dir-path $target_dir/citrix_adc_mas_proxied_calls/roles
    

for file in citrix_adm_*.py ; do
module=${file%.py}

python generate_integration_test.py \
--module $module \
--ns-version $NS_VERSION \
--test-type citrix_adm \
--dir-path $target_dir/citrix_adm/roles

python generate_integration_test.py \
--module $module \
--ns-version $NS_VERSION \
--test-type citrix_adm_auth_token \
--dir-path $target_dir/citrix_adm_auth_token/roles

done

cd -
