from . import *

def generate_all(args):
    playbook = []
    resource= {
        'lbgroup': {
            'name': 'mylbgroup',
            'timeout': 150,
        },
        'lbvserver': [
            {
                'name': 'resource-lb-vserver-1',
                'servicetype': 'HTTP',
                'ipv46': '10.60.44.22',
                'port': '8080',
            },
            {
                'name': 'resource-lb-vserver-2',
                'servicetype': 'HTTP',
                'ipv46': '10.60.44.23',
                'port': '8080',
            },
        ],
        'lbgroup_lbvserver_binding': [
            {
                'name': 'mylbgroup',
                'vservername': 'resource-lb-vserver-1'
            },
            {
                'name': 'mylbgroup',
                'vservername': 'resource-lb-vserver-2'
            }
        ],
    }

    lbgroup_step = functools.partial(
        generate_step,
        workflow_key='lbgroup',
        resource=resource['lbgroup']
    )

    lbvserver_step_1 = functools.partial(
        generate_step,
        workflow_key='lbvserver',
        resource=resource['lbvserver'][0],
    )

    lbvserver_step_2 = functools.partial(
        generate_step,
        workflow_key='lbvserver',
        resource=resource['lbvserver'][1],
    )

    lbgroup_binding_step = functools.partial(
        generate_step,
        workflow_key='lbgroup_lbvserver_binding ',
        resource=copy.deepcopy(resource['lbgroup_lbvserver_binding'][0])
    )

    full_bindings_list = copy.deepcopy(resource['lbgroup_lbvserver_binding'])
    full_bindings_list_short = copy.deepcopy(resource['lbgroup_lbvserver_binding'])[:-1]

    full_bindings_list_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbgroup_lbvserver_binding ',
        resource=full_bindings_list,
    )

    full_bindings_list_short_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbgroup_lbvserver_binding ',
        resource=full_bindings_list_short,
    )


    # Prerequisite create
    playbook.append(lbvserver_step_1(state='present', check_mode='no', step_name='Create prerequisite lb vserver'))
    playbook.append(lbvserver_step_2(state='present', check_mode='no', step_name='Create prerequisite lb vserver'))

    # Cleanup possible remnants
    playbook.append(lbgroup_step(state='absent', check_mode='no'))
    

    # Full cycles for lbgroup and standalone bindings
    full_cycle(playbook, lbgroup_step, cycle='present')
    full_cycle(playbook, lbgroup_binding_step, cycle='present')

    full_cycle(playbook, lbgroup_binding_step, cycle='absent')
    full_cycle(playbook, lbgroup_step, cycle='absent')

    # Full cycle for bindings lists
    playbook.append(lbgroup_step(state='present', check_mode='no'))

    full_cycle(playbook, full_bindings_list_step, cycle='present')
    full_cycle(playbook, full_bindings_list_short_step, cycle='present')
    full_cycle(playbook, full_bindings_list_step, cycle='present')
    full_cycle(playbook, full_bindings_list_step, cycle='absent')

    playbook.append(lbgroup_step(state='absent', check_mode='no'))

    # Check binding not erroring when parent is already removed
    playbook.append(lbgroup_step(state='present', check_mode='no'))
    playbook.append(lbgroup_binding_step(state='present', check_mode='no'))
    playbook.append(lbgroup_step(state='absent', check_mode='no'))
    playbook.append(lbgroup_binding_step(state='absent', check_mode='no'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_NOT_CHANGED_STEP))

    # Prerequisite delete
    playbook.append(lbvserver_step_1(state='absent', check_mode='no', step_name='Clean up prerequisite lb vserver'))
    playbook.append(lbvserver_step_2(state='absent', check_mode='no', step_name='Clean up prerequisite lb vserver'))

    save_test(args, 'lbgroup', playbook)
