from __future__ import print_function
import os
import argparse
import importlib

from IntegrationTest import IntegrationTest
import file_operations as fileop


def main():
    parser = argparse.ArgumentParser(description="Netscaler Ansible Integration Tests Generator")
    test_type_choices = [
            'netscaler_direct_calls',
            'mas_proxied_calls',
            ]
    parser.add_argument('--test-type', help='Integration Test Type (default: netscaler_direct_calls)', default='netscaler_direct_calls', choices=test_type_choices)
    parser.add_argument('--module', required=True, nargs='+')
    parser.add_argument('--dir-path', default=None, help="Directory path to where the integration tests to be generated")

    args = parser.parse_args()

    integration_test_type = args.test_type.lower()
    module_list = list(args.module)

    DEFAULT_DIR_PATH = os.path.join('../../../', 'test', 'integration', integration_test_type, 'roles')
    if args.dir_path is None:
        integration_dir_path = DEFAULT_DIR_PATH
    else:
        integration_dir_path = args.dir_path.lower()

    fileop.create_directory(integration_dir_path, nested=True)

    for module in module_list:
        try:
            module_name = importlib.import_module(module)
        except ImportError as e:
            print(e)
            print('Could not import \'{}\' module. Please check if this module present'.format(module))
            exit()

        entity_name = module_name.ENTITY_NAME
        if not entity_name.startswith('netscaler_'):
            print('Entity Name should start with "netscaler_" prefix.')
            exit()
    
        is_testbed = True if module_name.testbed_data else False
        entity_obj = IntegrationTest(module_name, entity_name, integration_test_type, integration_dir_path, is_testbed)
    
        # Create a directory structure required for integration tests
        entity_obj.create_directory_structure()
    
        entity_obj.create_defaults_main_file()
    
        entity_obj.create_tasks_main_file()
        entity_obj.create_tasks_nitro_file()

        #check if any prerequisite/testbed is required
        if module_name.testbed_data:
            entity_obj.create_tasks_testbed_file()
    
        entity_obj.create_operation_files()
    
        entity_obj.create_integration_test_file()
    

if __name__ == '__main__':
    main()
