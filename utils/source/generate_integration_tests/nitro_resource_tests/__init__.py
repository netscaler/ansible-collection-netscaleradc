import os.path
import yaml
import pyaml
import functools
import copy
from collections import OrderedDict as od

HERE = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))

NITRO_RESOURCE_TASK_FILE='''\
- name: "Nitro resource task: `{{ resource_name | default('') }}` for state `{{ state }}`"
  delegate_to: localhost
  register: result
  ignore_errors: "{{ ignore_errors | default('no') }}"
  check_mode: "{{ check_mode }}"
  citrix_adc_nitro_resource:
    nitro_user: '{{ nitro_user }}'
    nitro_pass: '{{ nitro_pass }}'
    nsip: '{{ nsip }}'
    state: '{{ state }}'

    workflow: "{{ workflow_dict }}"
    resource: "{{ resource_attributes }}"
'''

MAIN_ROLE_FILE='''\
- include: nitro.yaml
  tags:
    - nitro
'''

NITRO_ROLE_FILE='''\
- name: 'collect all nitro test cases'
  find:
    paths: '{{ role_path }}/tests/nitro'
    patterns: '{{ testcase }}.yaml'
  register: test_cases
- name: 'set test_items'
  set_fact: 'test_items="{{ test_cases.files | map(attribute=''path'') | list }}"'
- name: 'run test case'
  include: '{{ test_case_to_run }}'
  with_items: '{{ test_items }}'
  loop_control:
    loop_var: test_case_to_run
'''

DEFAUTLS_VARIABLES_FILE='''\
testcase: "*"
test_cases: []
nitro_user: nsroot
nitro_pass: nsroot
'''

def generate_skeleton(args):

    role_path = os.path.join(args.dir_path, 'citrix_adc_nitro_resource')
    if not os.path.exists(role_path):
        os.makedirs(role_path)

    paths = [
        os.path.join(role_path, 'tasks'),
        os.path.join(role_path, 'defaults'),
        os.path.join(role_path, 'vars'),
        os.path.join(role_path, 'tests/nitro/tasks'),
    ]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

    with open(os.path.join(role_path, 'tasks', 'main.yaml'), 'w') as fh:
        fh.write(MAIN_ROLE_FILE)

    with open(os.path.join(role_path, 'tasks', 'nitro.yaml'), 'w') as fh:
        fh.write(NITRO_ROLE_FILE)

    with open(os.path.join(role_path, 'defaults', 'main.yaml'), 'w') as fh:
        fh.write(DEFAUTLS_VARIABLES_FILE)

    with open(os.path.join(role_path, 'tests/nitro/tasks', 'nitro_resource_task.yaml'), 'w') as fh:
        fh.write(NITRO_RESOURCE_TASK_FILE)


    workflow_source = os.path.join(HERE, '../../nitro_resource_utils/workflows.yaml')
    with open(workflow_source, 'r') as fh:
        workflow = yaml.load(fh)

    with open(os.path.join(role_path, 'vars', 'main.yaml'), 'w') as fh:
        pyaml.dump(workflow, fh)



def generate_step(workflow_key, resource, state, check_mode, step_name=None):
    if step_name is None:
        step_name = 'Processing resource `%s` for state `%s` with check_mode `%s`' % (workflow_key, state, check_mode)
    step = od([
        ('name', step_name),
        ('include_tasks', od([
            ('file', 'tasks/nitro_resource_task.yaml'),
            ('apply', od([
                ('vars', od([
                    ('resource_name', workflow_key),
                    ('state', state),
                    ('check_mode', check_mode),
                    ('workflow_dict', '{{ workflow.%s }}' % workflow_key),
                    ('resource_attributes', copy.deepcopy(resource)),
                ])),
            ])),
        ])),
     ])
    return step

def generate_bindings_list_step(workflow_key, resource, state, check_mode, step_name=None):
    if step_name is None:
        step_name = 'Processing bindings list `%s` for state `%s` with check_mode `%s`' % (workflow_key, state, check_mode)
    step = od([
        ('name', step_name),
        ('include_tasks', od([
            ('file', 'tasks/nitro_resource_task.yaml'),
            ('apply', od([
                ('vars', od([
                    ('resource_name', '%s bindings list' % workflow_key),
                    ('state', state),
                    ('check_mode', check_mode),
                    ('workflow_dict', od([
                        ('lifecycle', 'bindings_list'),
                        ('binding_workflow', '{{ workflow.%s }}' % workflow_key),
                    ])),
                    ('resource_attributes', od([
                        ('bindings_list', copy.deepcopy(resource)),
                    ])),
                ])),
            ])),
        ])),
     ])
    return step

ASSERT_RESULT_CHANGED_STEP = {
    'assert':{
        'that': 'result is changed'
    }
}

ASSERT_RESULT_NOT_CHANGED_STEP = {
    'assert':{
        'that': 'not result is changed'
    }
}

def full_cycle(playbook, step_function, cycle):
    if cycle not in ('present', 'absent'):
        raise Exception('cycle value not valid %s' % cycle)

    # Fallthrough

    playbook.append(step_function(state=cycle, check_mode='yes'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_CHANGED_STEP))

    playbook.append(step_function(state=cycle, check_mode='no'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_CHANGED_STEP))

    playbook.append(step_function(state=cycle, check_mode='yes'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_NOT_CHANGED_STEP))

    playbook.append(step_function(state=cycle, check_mode='no'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_NOT_CHANGED_STEP))

def save_test(args, playbook_name, playbook):
    playbook_file = os.path.join(args.dir_path, 'citrix_adc_nitro_resource', 'tests', 'nitro', '%s.yaml' % playbook_name)
    with open(playbook_file, 'w') as fh:
        pyaml.dump(playbook, fh, vspacing=[1,0])
