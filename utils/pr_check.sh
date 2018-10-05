#!/usr/bin/env bash


set -e

pversions=("2.7" "3.5")
for version in "${pversions[@]}" ; do
ansible-test sanity --tox --python "$version" --test yamllint
ansible-test sanity --tox --python "$version" --test pep8
ansible-test sanity --tox --python "$version" --test validate-modules
done
