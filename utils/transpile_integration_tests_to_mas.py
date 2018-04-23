#!/usr/bin/env python3

import argparse
import os.path
import shutil
import yaml
import pyaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--target', required=True)


    args = parser.parse_args()

    if os.path.exists(args.target):
        raise Exception('Cannot ovewrite %s' % args.target)


    shutil.copytree(args.source, args.target)

    # Process each playbook
    for role_dir in os.listdir(args.target):
        if role_dir == 'netscaler_nitro_request':
            continue
        role_path = os.path.join(args.target, role_dir)
        if os.path.isdir(role_path):
            print('Would process %s' % role_dir)
            process_role_dir(role_path)

def process_role_dir(role_dir):
    test_dir = os.path.join(role_dir,'tests', 'nitro')
    for item in os.listdir(test_dir):
        item_path = os.path.join(test_dir, item)
        if os.path.isdir(item_path):
            print('Would process test dir %s' % item_path)
            process_test_dir(item_path)

    for testbed_setup in ('testbed.yaml', 'testbed_setup.yaml'):
        testbed_playbook = os.path.join(role_dir, 'tasks', testbed_setup)
        if os.path.exists(testbed_playbook):
            print('Processing testbed playbook %s' % testbed_playbook)
            process_playbook(testbed_playbook)


def process_test_dir(test_dir):
    for item in os.listdir(test_dir):
        item_path = os.path.join(test_dir, item)
        process_playbook(item_path)

def process_playbook(playbook_path):
    print('Processing playbook %s' % playbook_path)
    with open(playbook_path, 'r') as fh:
        data = yaml.load(fh)


    for task in data:
        task_keys = frozenset(task.keys())
        for key in task_keys:
            if key.startswith('netscaler_'):
                module_name = key
        print('module name is %s' % module_name)
        module_arguments = task[module_name]
        del module_arguments['nsip']
        del module_arguments['nitro_user']
        del module_arguments['nitro_pass']
        module_arguments['mas_ip'] = '{{ nsip }}'
        module_arguments['mas_auth_token'] = '{{ mas_login_result.nitro_auth_token }}'
        module_arguments['mas_proxy_call'] = 'true'
        module_arguments['instance_ip'] = '{{ instance_ip }}'

    with open(playbook_path, 'w') as fh:
        pyaml.dump(data,fh, indent=2)

if __name__ == '__main__':
    main()
