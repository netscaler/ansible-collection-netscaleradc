import os
import argparse
import copy
from collections import OrderedDict
import json
import pyaml
import shutil

lbgroup_definition = OrderedDict((
    ('resource', 'lbgroup'),
    ('resource_name', 'integration_test_lbgroup1'),
    ('resource_missing_errorcode', [258]),
    ('resource_non_updateable_attributes', ['newname']),
    ('resource_attributes', OrderedDict((
        ('name', 'integration_test_lbgroup1'),
        ('persistencetype', 'SOURCEIP'),
    ))),
))


usage_playbook_template = OrderedDict((
    ('hosts', 'citrix_adc'),
    ('gather_facts', 'no'),
    ('tasks', [
        OrderedDict((
            ('name', 'Create resource'),
            ('import_role', OrderedDict((
                    ('name', 'adc_resource_create_or_update'),
                ))
            ),
            ('vars', OrderedDict()),
        )),
        OrderedDict((
            ('name', 'Delete resource'),
            ('import_role', OrderedDict((
                    ('name', 'adc_resource_delete'),
                ))
            ),
            ('vars', OrderedDict()),
        )),
    ]),
)),

adc_resource_integration_test_playbook_template = [
    OrderedDict((
        ('hosts', 'citrix_adc'),
        ('gather_facts', 'no'),
        ('tasks', []),
    ))
]

def create_integration_task(step_title, role, role_input):
    stepdict = OrderedDict((
        ('name', None),
        ('import_role', OrderedDict((
                ('name', None),
            ))
        ),
        ('vars', OrderedDict((
            ('role_input', None),
        ))),
    ))

    #print(json.dumps(stepdict, indent=4))
    output = copy.deepcopy(stepdict)
    output['name'] = step_title
    output['import_role']['name'] = role
    output['vars']['role_input'] = role_input
    return output

def create_integration_assertion(assertion_title, assertions):
    assertion_dict = OrderedDict((
        ('name', None),
        ('assert', OrderedDict((
                ('that', []),
            ))
        ),
    ))

    output = copy.deepcopy(assertion_dict)
    output['name'] = assertion_title
    output['assert']['that'] = assertions
    
    return output

def generate_mutator(key, value):
    def mutator(resource_definition):
        new_definition = copy.deepcopy(resource_definition)
        new_definition['resource_attributes'][key] = value
        return new_definition

    return mutator

def generate_adc_resource_binding_integration_test(binding, mutators, dependencies, output_yaml):
    print('Generating %s' % output_yaml)
    tasks = []
    
    # Create dependencies
    for dep_resource in dependencies:
        tasks.append(
            create_integration_task(
                'Create dependency',
                'adc_resource_create_or_update',
                copy.deepcopy(dep_resource)
            )
        )

    dry_run_binding = copy.deepcopy(binding)
    dry_run_binding['dry_run'] = True

    # Create binding dry run
    tasks.append(
        create_integration_task(
            'Create binding dry run',
            'adc_resource_binding_create',
            copy.deepcopy(dry_run_binding)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create',
            ['role_output.operation == "create"']
        )
    )

    # Create binding
    tasks.append(
        create_integration_task(
            'Create binding dry run',
            'adc_resource_binding_create',
            copy.deepcopy(binding)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create',
            ['role_output.operation == "create"']
        )
    )

    # Delete binding dry run
    tasks.append(
        create_integration_task(
            'Delete binding dry run',
            'adc_resource_binding_delete',
            copy.deepcopy(dry_run_binding)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert delete',
            ['role_output.operation == "delete"']
        )
    )

    # Delete binding
    tasks.append(
        create_integration_task(
            'Delete binding',
            'adc_resource_binding_delete',
            copy.deepcopy(binding)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert delete',
            ['role_output.operation == "delete"']
        )
    )

    # Delete dependencies
    for dep_resource in reversed(dependencies):
        tasks.append(
            create_integration_task(
                'Delete dependency',
                'adc_resource_delete',
                copy.deepcopy(dep_resource)
            )
        )

    playbook = copy.deepcopy(adc_resource_integration_test_playbook_template )
    playbook[0]['tasks'] = tasks
    print(json.dumps(playbook, indent=4))

    with open(output_yaml, 'w') as fh:
        pyaml.dump(playbook, fh, indent=2, vspacing=[0,0,1])

def generate_adc_resource_integration_test(resource_definition, update_mutator, non_updateable_mutator, output_yaml):
    print('Generating %s' % output_yaml)
    tasks = []


    dry_run_definition = copy.deepcopy(resource_definition)
    dry_run_definition['dry_run'] = True

    # Delete idempotency check
    tasks.append(
        create_integration_task(
            'Delete idempotency',
            'adc_resource_delete',
            copy.deepcopy(resource_definition)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert delete operation was none',
            ['role_output.operation == "none"']
        )
    )

    # Create resource dry run
    tasks.append(
        create_integration_task(
            'Create resource dry run',
            'adc_resource_create_or_update',
            copy.deepcopy(dry_run_definition)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create dry run',
            ['role_output.operation == "create"']
        )
    )

    # Create resource
    tasks.append(
        create_integration_task(
            'Create resource dry run',
            'adc_resource_create_or_update',
            copy.deepcopy(resource_definition)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create',
            ['role_output.operation == "create"']
        )
    )

    if update_mutator is not None:
        resource_definition = update_mutator(resource_definition)
        dry_run_definition = copy.deepcopy(resource_definition)
        dry_run_definition['dry_run'] = True

        # Update resource dry run
        tasks.append(
            create_integration_task(
                'Create resource dry run',
                'adc_resource_create_or_update',
                copy.deepcopy(dry_run_definition)
            )
        )

        tasks.append(
            create_integration_assertion(
                'Assert update',
                ['role_output.operation == "update"']
            )
        )

        # Update resource
        tasks.append(
            create_integration_task(
                'Create resource dry run',
                'adc_resource_create_or_update',
                copy.deepcopy(resource_definition)
            )
        )

        tasks.append(
            create_integration_assertion(
                'Assert update',
                ['role_output.operation == "update"']
            )
        )

    if non_updateable_mutator is not None:
        resource_definition = non_updateable_mutator(resource_definition)
        dry_run_definition = copy.deepcopy(resource_definition)
        dry_run_definition['dry_run'] = True

        # Recreate resource dry run
        tasks.append(
            create_integration_task(
                'Create resource dry run',
                'adc_resource_create_or_update',
                copy.deepcopy(dry_run_definition)
            )
        )

        tasks.append(
            create_integration_assertion(
                'Assert recreate',
                ['role_output.operation == "recreate"']
            )
        )

        # Recreate resource
        tasks.append(
            create_integration_task(
                'Create resource dry run',
                'adc_resource_create_or_update',
                copy.deepcopy(resource_definition)
            )
        )

        tasks.append(
            create_integration_assertion(
                'Assert recreate',
                ['role_output.operation == "recreate"']
            )
        )

    # Delete resource dry run
    tasks.append(
        create_integration_task(
            'Create resource dry run',
            'adc_resource_delete',
            copy.deepcopy(dry_run_definition)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create',
            ['role_output.operation == "delete"']
        )
    )

    # Delete resource
    tasks.append(
        create_integration_task(
            'Create resource dry run',
            'adc_resource_delete',
            copy.deepcopy(resource_definition)
        )
    )

    tasks.append(
        create_integration_assertion(
            'Assert create',
            ['role_output.operation == "delete"']
        )
    )

    playbook = copy.deepcopy(adc_resource_integration_test_playbook_template )
    #print(json.dumps(playbook, indent=4))
    playbook[0]['tasks'] = tasks

    with open(output_yaml, 'w') as fh:
        pyaml.dump(playbook, fh, indent=2, vspacing=[0,0,1])
    

def generate_use_stub(resource_definition, output_yaml):
    #print(json.dumps(usage_playbook_template, indent=4))
    playbook = copy.deepcopy(usage_playbook_template)
    playbook[0]['tasks'][0]['vars'] = copy.deepcopy(resource_definition)
    delete_resource_definition= copy.deepcopy(resource_definition)
    del delete_resource_definition['resource_attributes']
    del delete_resource_definition['resource_non_updateable_attributes']

    playbook[0]['tasks'][1]['vars'] = delete_resource_definition
    #print(json.dumps(playbook, indent=4))
    with open(output_yaml, 'w') as fh:
        pyaml.dump(playbook, fh, indent=2)
    pass

def make_all_stubs(args):
    # Having the here dir is useful
    here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

    # Make sure the path exists
    if not os.path.exists(args.stubs_dir):
        os.makedirs(args.stubs_dir)

    # Copy roles to stubs dir
    target_roles_path = os.path.join(args.stubs_dir, 'roles')
    if os.path.exists(target_roles_path):
        shutil.rmtree(target_roles_path)
    shutil.copytree(os.path.join(here, 'roles'), target_roles_path)

    generate_use_stub(
        lbgroup_definition,
        os.path.join(args.stubs_dir, 'lbgroup.yaml')
    )

def make_all_integration_tests(args):

    # Having the here dir is useful
    here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

    # Make sure the path exists
    if not os.path.exists(args.integration_dir):
        os.makedirs(args.integration_dir)

    # Copy roles to integration dir
    target_roles_path = os.path.join(args.integration_dir, 'roles')
    if os.path.exists(target_roles_path):
        shutil.rmtree(target_roles_path)
    shutil.copytree(os.path.join(here, 'roles'), target_roles_path)

    # lbgroup
    generate_adc_resource_integration_test(
        lbgroup_definition,
        generate_mutator('persistencetype', 'NONE'),
        None,
        os.path.join(args.integration_dir, 'lbgroup.yaml'),
    )

    # lbgroup_lbvserver_binding
    dependencies = [
        {
            'resource': 'lbvserver',
            'resource_name': 'integration_test_lbvserver1',
            'resource_missing_errorcode': [258],
            'resource_attributes': {
                'name': 'integration_test_lbvserver1',
                'ipv46': '12.23.53.31',
                'servicetype': 'HTTP',
                'port': 80,
            }
        },

        {
            'resource': 'lbvserver',
            'resource_name': 'integration_test_lbvserver2',
            'resource_missing_errorcode': [258],
            'resource_attributes': {
                'name': 'integration_test_lbvserver2',
                'ipv46': '12.23.53.32',
                'servicetype': 'HTTP',
                'port': 80,
            }
        },

        {
            'resource': 'lbgroup',
            'resource_name': 'integration_test_lbgroup1',
            'resource_missing_errorcode': [258],
            'resource_non_updateable_attributes': ['newname'],
            'resource_attributes': {
                'name': 'integration_test_lbgroup1',
                'persistencetype': 'SOURCEIP',
            }
        },
    ]

    global lbgroup_lbvserver_binding
    lbgroup_lbvserver_binding = OrderedDict((
        ('resource', 'lbgroup_lbvserver_binding'),
        ('resource_name', 'integration_test_lbgroup1'),
        ('resource_missing_errorcode', [258]),
        ('id_attributes', ['vservername']),
        ('resource_attributes', OrderedDict((
            ('name', 'integration_test_lbgroup1'),
            ('vservername', 'integration_test_lbvserver1'),
        ))),
    ))

    generate_adc_resource_binding_integration_test(
        lbgroup_lbvserver_binding,
        None,
        dependencies,
        os.path.join(args.integration_dir, 'lbgroup_lbvserver_biding.yaml'),
    )


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--stubs-dir', required=False)
    parser.add_argument('--integration-dir', required=False)
    parser.add_argument('--non-updateable-json', required=True)

    args = parser.parse_args()

    if args.stubs_dir is not None:
        make_all_stubs(args)

    if args.integration_dir is not None:
        make_all_integration_tests(args)

    global non_updateable_dict
    with open(args.non_updateable_json, 'r') as fh:
        non_updateable_dict = json.load(fh)




if __name__ == '__main__':
    main()
