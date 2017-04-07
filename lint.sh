#!/bin/bash

# Run lint tools to check codebase

find ansible-modules -name '*.py' -exec pep8 --ignore=E402 --max-line-length=160 {} \;
