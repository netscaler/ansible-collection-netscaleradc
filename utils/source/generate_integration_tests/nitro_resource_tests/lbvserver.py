from . import *

resources = {
    'lbvservers': [
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
}

lbvserver_step = functools.partial(
    generate_step,
    workflow_key='lbvserver',
    resource=copy.deepcopy(resources['lbvservers'][0])
)

lbvserver_modified_resource = copy.deepcopy(resources['lbvservers'][0])
lbvserver_modified_resource['port'] = '9090'
lbvserver_modified_step = functools.partial(
    generate_step,
    workflow_key='lbvserver',
    resource=lbvserver_modified_resource
)
def generate_spilloverpolicy_bindings(args):
    playbook = []
    local_resources = {
        'spilloverpolicies': [
            od([
                ('name', 'spillover-policy-1'),
                ('rule', 'SYS.VSERVER("vserver").RESPTIME.GT(100)'),
                ('action', 'spillover'),
            ]),
            od([
                ('name', 'spillover-policy-2'),
                ('rule', 'SYS.VSERVER("vserver").THROUGHPUT.LT(100)'),
                ('action', 'spillover'),
            ])
        ],

        'lbvserver_spilloverpolicy_bindings': [
            od([
                ('name', resources['lbvservers'][0]['name']),
                ('bindpoint', 'REQUEST'),
                ('policyname', 'spillover-policy-1'),
                ('priority', 100),
            ]),
            od([
                ('name', resources['lbvservers'][0]['name']),
                ('bindpoint', 'REQUEST'),
                ('policyname', 'spillover-policy-2'),
                ('priority', 101),
            ]),
        ]
    }

    spilloverpolicy_steps = []
    for policy in local_resources['spilloverpolicies']:
        step = functools.partial(
            generate_step,
            workflow_key='spilloverpolicy',
            resource=copy.deepcopy(policy)
        )
        spilloverpolicy_steps.append(step)

    single_binding_step = functools.partial(
        generate_step,
        workflow_key='lbvserver_spilloverpolicy_binding',
        resource=copy.deepcopy(local_resources['lbvserver_spilloverpolicy_bindings'][0])
    )

    bindings_list_all_bindings_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbvserver_spilloverpolicy_binding',
        resource=copy.deepcopy(local_resources['lbvserver_spilloverpolicy_bindings'])
    )

    resource = copy.deepcopy(local_resources['lbvserver_spilloverpolicy_bindings'][:-1])
    bindings_list_one_binding_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbvserver_spilloverpolicy_binding',
        resource=resource,
    )

    # Prerequisites create for spillover policy bindings
    playbook.append(lbvserver_step(state='present', check_mode='no'))
    playbook.append(spilloverpolicy_steps[0](state='present', check_mode='no'))
    playbook.append(spilloverpolicy_steps[1](state='present', check_mode='no'))


    # Single binding
    playbook.append(single_binding_step(state='present', check_mode='no'))
    playbook.append(single_binding_step(state='absent', check_mode='no'))

    # Bindings list
    playbook.append(bindings_list_all_bindings_step(state='present', check_mode='no'))
    playbook.append(bindings_list_one_binding_step(state='present', check_mode='no'))
    playbook.append(bindings_list_all_bindings_step(state='present', check_mode='no'))
    playbook.append(bindings_list_all_bindings_step(state='absent', check_mode='no'))

    # Check for missing bound object
    playbook.append(lbvserver_step(state='absent', check_mode='no'))
    playbook.append(bindings_list_all_bindings_step(state='absent', check_mode='no'))


    # Prerequisites delete for spillover policy bindings
    playbook.append(lbvserver_step(state='absent', check_mode='no'))
    playbook.append(spilloverpolicy_steps[0](state='absent', check_mode='no'))
    playbook.append(spilloverpolicy_steps[1](state='absent', check_mode='no'))
    

    save_test(args, 'lbvserver_spilloverpolicy_bindings', playbook)

def generate_service_bindings(args):
    playbook = []
    local_resources = {
        'services': [
            {
                'name': 'service-http-1',
                'servicetype': 'HTTP',
                'ip': '10.78.0.1',
                'port': '80',
            },
            {
                'name': 'service-http-2',
                'servicetype': 'HTTP',
                'ip': '10.78.0.2',
                'port': '80',
            },
        ],
        'lbvserver_service_bindings': [
            {
                'name': 'resource-lb-vserver-1',
                'servicename': 'service-http-1',
            },
            {
                'name': 'resource-lb-vserver-1',
                'servicename': 'service-http-2',
            },
        ],
    }
    service_steps = []
    for service in local_resources['services']:

        step = functools.partial(
            generate_step,
            workflow_key='service',
            resource=copy.deepcopy(service)
        )
        service_steps.append(step)

    single_binding_step = functools.partial(
        generate_step,
        workflow_key='lbvserver_service_binding',
        resource=copy.deepcopy(local_resources['lbvserver_service_bindings'][0])
    )

    resource = copy.deepcopy(local_resources['lbvserver_service_bindings'])

    all_bindings_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbvserver_service_binding',
        resource=resource,
    )

    resource = copy.deepcopy(local_resources['lbvserver_service_bindings'][:-1])
    all_bindings_fewer_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='lbvserver_service_binding',
        resource=resource,
    )


    # Prerequisites create for service bindings
    playbook.append(lbvserver_step(state='present', check_mode='no'))
    playbook.append(service_steps[0](state='present', check_mode='no'))
    playbook.append(service_steps[1](state='present', check_mode='no'))

    # Single binding
    full_cycle(playbook, single_binding_step, cycle='present')
    full_cycle(playbook, single_binding_step, cycle='absent')

    # Bindings list
    full_cycle(playbook, all_bindings_step, cycle='present')
    full_cycle(playbook, all_bindings_fewer_step, cycle='present')
    full_cycle(playbook, all_bindings_step, cycle='present')
    full_cycle(playbook, all_bindings_step, cycle='absent')

    # Prerequisites delete for service bindings
    playbook.append(lbvserver_step(state='absent', check_mode='no'))
    playbook.append(service_steps[0](state='absent', check_mode='no'))
    playbook.append(service_steps[1](state='present', check_mode='no'))

    save_test(args, 'lbvserver_service_bindings', playbook)

def generate_analyticsprofile_bindings(args):
    playbook = []
    local_resources = {
        'lbvserver_analyticsprofile_binding': {
            'name': resources['lbvservers'][0]['name'],
            'analyticsprofile': 'ns_analytics_default_http_profile'
        }
    }

    lbvserver_analyticsprofile_binding_step = functools.partial(
        generate_step,
        workflow_key='lbvserver_analyticsprofile_binding',
        resource=local_resources['lbvserver_analyticsprofile_binding'],
    )
    # Prerequisites create for service bindings
    playbook.append(lbvserver_step(state='present', check_mode='no'))

    full_cycle(playbook, lbvserver_analyticsprofile_binding_step, cycle='present')
    full_cycle(playbook, lbvserver_analyticsprofile_binding_step, cycle='absent')

    # Prerequisites delete for service bindings
    playbook.append(lbvserver_step(state='absent', check_mode='no'))

    save_test(args, 'lbvserver_analyticsprofile_bindings', playbook)

def generate_all(args):
    playbook = []


    # Sanitize before full cycle tests
    playbook.append(lbvserver_step(state='absent', check_mode='no'))

    # Full cycle present, update and delete
    full_cycle(playbook, lbvserver_step, cycle='present')
    full_cycle(playbook, lbvserver_modified_step, cycle='present')
    full_cycle(playbook, lbvserver_modified_step, cycle='absent')


    save_test(args, 'lbvserver', playbook)

    # Bindings
    generate_service_bindings(args)
    generate_spilloverpolicy_bindings(args)
    generate_analyticsprofile_bindings(args)
