#!/usr/bin/env bash


set -e

# Run unit tests
pversions=("2.7" "3.5")
for version in "${pversions[@]}" ; do
ansible-test units --tox --python "${version}" "$1"
done
