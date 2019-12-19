import os
import argparse
import pyaml
import yaml
import copy
import functools
from collections import OrderedDict as od

def generate_test_cases(args):
    generate_lbgroup(args)
    generate_lbmetrictable(args)
    generate_bindings_list_failure_checks(args)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir-path', default=None, help="Directory path to where the integration tests to be generated")
    parser.add_argument('--ns-version', default='12.1', help="Target Netscaler version")
    
    args = parser.parse_args()

    import nitro_resource_tests
    nitro_resource_tests.generate_skeleton(args)

    from nitro_resource_tests import lbvserver
    lbvserver.generate_all(args)

    from nitro_resource_tests import lbassorted
    lbassorted.generate_all(args)

    from nitro_resource_tests import lbgroup
    lbgroup.generate_all(args)

    from nitro_resource_tests import lbmetrictable
    lbmetrictable.generate_all(args)

    from nitro_resource_tests import bindings_list_failures
    bindings_list_failures.generate_all(args)

    from nitro_resource_tests import spillover
    spillover.generate_all(args)

    from nitro_resource_tests import basic
    basic.generate_all(args)



if __name__ == '__main__':
    main()
