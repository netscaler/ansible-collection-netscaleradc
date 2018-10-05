from __future__ import print_function
import os
from collections import OrderedDict

import file_operations as fileop
import template_yaml


class IntegrationTest(object):
    def __init__(self, module_name, entity_name, integration_test_type, integration_dir_path, is_testbed=False):
        """
            Initialize for the below tree structrue:
                defaults
                    main.yaml
                tasks
                    main.yaml
                    nitro.yaml
                tests
                    nitro
                        <entity_name>
                            disable.yaml
                            remove.yaml
                            setup.yaml
                            update.yaml
                        <entity_name>.yaml
        """
        self.module_name = module_name
        self.entity_name = entity_name
        self.integration_test_type = integration_test_type
        self.integration_dir_path = integration_dir_path
        self.is_testbed = is_testbed

        self.entity_dir_path = os.path.join(self.integration_dir_path, self.entity_name)

        self.defaults_dir = os.path.join(self.entity_dir_path, 'defaults')
        self.defaults_main_file = os.path.join(self.defaults_dir, 'main.yaml')

        self.tasks_dir = os.path.join(self.entity_dir_path, 'tasks')
        self.tasks_main_file = os.path.join(self.tasks_dir, 'main.yaml')
        self.tasks_nitro_file = os.path.join(self.tasks_dir, 'nitro.yaml')
        if self.is_testbed:
            self.tasks_testbed_file = os.path.join(self.tasks_dir, 'testbed.yaml')

        self.tests_dir = os.path.join(self.entity_dir_path, 'tests')
        self.tests_nitro_dir = os.path.join(self.tests_dir, 'nitro')
        self.tests_nitro_entity_dir = os.path.join(self.tests_nitro_dir, self.entity_name)

    def create_directory_structure(self):
        # mkdir entity directory
        fileop.create_directory(self.entity_dir_path)

        # mkdir defaults, tasks and tests directories
        fileop.create_directory(self.defaults_dir)
        fileop.create_directory(self.tasks_dir)
        fileop.create_directory(self.tests_dir)

        # mkdir tests/nitro
        fileop.create_directory(self.tests_nitro_dir)

        # mkdir tests/nitro/<entity_name>
        input_data = self.module_name.input_data
        for sub_module in input_data:
            sub_module_dir = os.path.join(self.tests_nitro_dir, sub_module)
            fileop.create_directory(sub_module_dir)

    def create_defaults_main_file(self):
        fileop.yamlstr_to_yaml(self.defaults_main_file, template_yaml.defaults_main_data)

    def create_tasks_main_file(self):
        if self.is_testbed:
            data = template_yaml.tasks_main_data_with_testbed
        else:
            data = template_yaml.tasks_main_data
        fileop.yamlstr_to_yaml(self.tasks_main_file, data) 

    def create_tasks_nitro_file(self):
        fileop.yamlstr_to_yaml(self.tasks_nitro_file, template_yaml.tasks_nitro_data)

    def create_tasks_testbed_file(self):
        testbed_data = self.module_name.testbed_data
        fileop.python_to_yaml(self.tasks_testbed_file, testbed_data)

    def create_operation_files(self):
        input_data = self.module_name.input_data
        for sub_module in input_data:
            operation = input_data[sub_module]
            for op_item in operation:
                for op_name in op_item: # only one {op_name:op_data} will be there
                    output_op_data = op_item[op_name]
                    operation_file = os.path.join(self.tests_nitro_dir, sub_module, "{}.yaml".format(op_name))
                    fileop.python_to_yaml(operation_file, output_op_data)

    def generate_test_step(self, operation, sub_module, check_mode, idempotency, assertion=True):
        test_step = []
        task = {
                    'include': os.path.join('{{ role_path }}', 'tests', 'nitro', sub_module, "{}.yaml".format(operation)),
                    'vars': {
                        'check_mode': check_mode
                    }
                }
        assertion_changed = {
                    'assert': {'that': 'result is changed'}
                    }
        
        assertion_not_changed = {
                    'assert': {'that': 'not result is changed'}
                    }
        
        # Task steps
        test_step.append(task)

        if assertion: 
            if idempotency:
                test_step.append(assertion_not_changed)
            else:
                test_step.append(assertion_changed)

        return test_step

    def create_integration_test_file(self):
        # Assuming that VERIFY_CHECK_MODE and VERIFY_IDEMPOTENCY is always True
        input_data = self.module_name.input_data
        for sub_module in input_data:
            integration_test_data = []
            operation = input_data[sub_module]
            for op_item in operation:
                # for run_once flag, only generate one task without any assertion
                if op_item['run_once'] == True:
                    for op_name in op_item:
                        if op_name.strip() == 'run_once': # skip run_once key, as it is not an operation
                            continue
                        integration_test_data += self.generate_test_step(op_name, sub_module, check_mode=False, idempotency=False, assertion=False)

                #Otherwise, generate a full fledged integration suite
                else:
                    for op_name in op_item: # only one {op_name:op_data} will be there
                        if op_name.strip() == 'run_once': # skip run_once key, as it is not an operation
                            continue
                        if op_name.strip() != 'disable':
                            integration_test_data += self.generate_test_step(op_name, sub_module, check_mode=True, idempotency=False)
                            integration_test_data += self.generate_test_step(op_name, sub_module, check_mode=False, idempotency=False)
            
                        integration_test_data += self.generate_test_step(op_name, sub_module, check_mode=True, idempotency=True)
                        integration_test_data += self.generate_test_step(op_name, sub_module, check_mode=False, idempotency=True)
        
                self.integration_test_file = os.path.join(self.tests_nitro_dir, "{}.yaml".format(sub_module))
                fileop.python_to_yaml(self.integration_test_file, integration_test_data)
