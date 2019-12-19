from . import *



def generate_monitor(args):
    playbook = []

    resources = {
        'lbmonitor':{
            'monitorname': 'lb-monitor-http',
            'type': 'HTTP',
            'httprequest': 'HEAD /file.html',
        },

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

        'service_lbmonitor_bindings': [
            {
                'name': 'service-http-1',
                'monitor_name': 'lb-monitor-http',
            },
            {
                'name': 'service-http-2',
                'monitor_name': 'lb-monitor-http',
            },
        ],

        'servicegroups': [
            {
                'servicegroupname': 'integration-test-servicegroup-1',
                'servicetype': 'HTTP',
            },
            {
                'servicegroupname': 'integration-test-servicegroup-2',
                'servicetype': 'HTTP',
            },
        ],

        'servicegroup_lbmonitor_bindings': [
            {
                'servicegroupname': 'integration-test-servicegroup-1',
                'monitor_name': 'lb-monitor-http',
            },
            {
                'servicegroupname': 'integration-test-servicegroup-2',
                'monitor_name': 'lb-monitor-http',
            },
        ]

    }


    lbmonitor_step = functools.partial(
        generate_step,
        workflow_key='lbmonitor',
        resource=copy.deepcopy(resources['lbmonitor'])
    )

    resource=copy.deepcopy(resources['lbmonitor'])
    resource['httprequest'] = 'HEAD /other_file.html'
    lbmonitor_modified_step = functools.partial(
        generate_step,
        workflow_key='lbmonitor',
        resource=resource,
    )
    service_steps = []
    for item in resources['services']:
        step = functools.partial(
            generate_step,
            workflow_key='service',
            resource=item,
        )
        service_steps.append(step)

    service_lbmonitor_binding_steps = []
    for item in resources['service_lbmonitor_bindings']:
        step = functools.partial(
            generate_step,
            workflow_key='service_lbmonitor_binding',
            resource=item,
        )
        service_lbmonitor_binding_steps.append(step)

    service_lbmonitor_binding_list_full_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='service_lbmonitor_binding',
        resource=copy.deepcopy(resources['service_lbmonitor_bindings'])
    )

    resource=copy.deepcopy(resources['service_lbmonitor_bindings'][:-1])

    service_lbmonitor_binding_list_reduced_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='service_lbmonitor_binding',
        resource=resource,
    )


    servicegroup_steps = []
    for item in resources['servicegroups']:
        step = functools.partial(
            generate_step,
            workflow_key='servicegroup',
            resource=item,
        )
        servicegroup_steps.append(step)

    servicegroup_lbmonitor_binding_steps = []
    for item in resources['servicegroup_lbmonitor_bindings']:
        step = functools.partial(
            generate_step,
            workflow_key='servicegroup_lbmonitor_binding',
            resource=item,
        )
        servicegroup_lbmonitor_binding_steps.append(step)

    servicegroup_lbmonitor_binding_list_full_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='servicegroup_lbmonitor_binding',
        resource=copy.deepcopy(resources['servicegroup_lbmonitor_bindings'])
    )

    servicegroup_lbmonitor_binding_list_reduced_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='servicegroup_lbmonitor_binding',
        resource=copy.deepcopy(resources['servicegroup_lbmonitor_bindings'][:-1])
    )


    # Clean up before starting the full cycle tests
    playbook.append(lbmonitor_step(state='absent', check_mode='no'))

    # Standalone full cycle
    full_cycle(playbook, lbmonitor_step, cycle='present')
    full_cycle(playbook, lbmonitor_modified_step, cycle='present')
    full_cycle(playbook, lbmonitor_modified_step, cycle='absent')

    # Recreate for subsequent prerequisites
    playbook.append(lbmonitor_step(state='present', check_mode='no'))

    # Rest of prerequisites
    playbook.append(service_steps[0](state='present', check_mode='no'))
    playbook.append(service_steps[1](state='present', check_mode='no'))

    playbook.append(servicegroup_steps[0](state='present', check_mode='no'))
    playbook.append(servicegroup_steps[1](state='present', check_mode='no'))

    # Full cycle standalone service to monitor bindings
    full_cycle(playbook, service_lbmonitor_binding_steps[0], cycle='present')
    full_cycle(playbook, service_lbmonitor_binding_steps[1], cycle='present')
    full_cycle(playbook, service_lbmonitor_binding_steps[0], cycle='absent')
    full_cycle(playbook, service_lbmonitor_binding_steps[1], cycle='absent')

    # Full cycle standalone servicegroup to monitor bindings
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[0], cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[1], cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[0], cycle='absent')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[1], cycle='absent')

    # Full cycle service to monitor binding lists
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_reduced_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='absent')


    # Full cycle servicegroup to monitor binding lists
    #full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, servicegroup_lbmonitor_binding_list_reduced_step, cycle='present')
    #full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='absent')

    # Clean up prerequisites
    playbook.append(lbmonitor_step(state='absent', check_mode='no'))

    playbook.append(service_steps[0](state='absent', check_mode='no'))
    playbook.append(service_steps[1](state='absent', check_mode='no'))

    playbook.append(servicegroup_steps[0](state='absent', check_mode='no'))
    playbook.append(servicegroup_steps[1](state='absent', check_mode='no'))

    save_test(args, 'lbmonitor', playbook)

def generate_lbprofile(args):
    playbook = []

    resources = {
        'lbprofile': {
          'lbprofilename': 'my-lb-profile',
          'dbslb': 'DISABLED',
        }
    }
    lbprofile_step = functools.partial(
        generate_step,
        workflow_key='lbprofile',
        resource = copy.deepcopy(resources['lbprofile']),
    )

    resource = copy.deepcopy(resources['lbprofile'])
    resource['dbslb'] = 'ENABLED'

    lbprofile_modified_step = functools.partial(
        generate_step,
        workflow_key='lbprofile',
        resource=resource,
    )

    # Clean up
    playbook.append(lbprofile_step(state='absent', check_mode='no'))

    full_cycle(playbook, lbprofile_step, cycle='present')
    full_cycle(playbook, lbprofile_modified_step, cycle='present')
    full_cycle(playbook, lbprofile_modified_step, cycle='absent')

    save_test(args, 'lbprofile', playbook)

def generate_lbroute(args):
    playbook = []
    resources = {
        'lbvservers': [
            od([
                ('name', 'lbroute-gw-lbvserver'),
                ('servicetype', 'ANY'),
                ('lbmethod', 'ROUNDROBIN'),
                ('persistencetype', 'SOURCEIP'),
            ]),
            od([
                ('name', 'lbroute-gw-lbvserver-alt'),
                ('servicetype', 'ANY'),
                ('lbmethod', 'ROUNDROBIN'),
                ('persistencetype', 'SOURCEIP'),
            ]),
        ],
        'lbroutes': [
            od([
                ('network', '193.168.1.0'),
                ('netmask', '255.255.255.0'),
                ('gatewayname', 'lbroute-gw-lbvserver'),
            ]),
            od([
                ('network', '193.168.1.0'),
                ('netmask', '255.255.255.0'),
                ('gatewayname', 'lbroute-gw-lbvserver-alt'),
            ]),
        ],
    }
    lbvserver_steps = []
    for lbvserver in resources['lbvservers']:
        lbvserver_steps.append(
            functools.partial(
                generate_step,
                workflow_key='lbvserver',
                resource=lbvserver,
            )
        )

    lbroute_steps = []

    for lbroute in resources['lbroutes']:
        lbroute_steps.append(
            functools.partial(
                generate_step,
                workflow_key='lbroute',
                resource=lbroute,
            )
        )

    # Prereqsite create
    playbook.append(lbvserver_steps[0](state='present', check_mode='no'))
    playbook.append(lbvserver_steps[1](state='present', check_mode='no'))

    # Sanitize
    playbook.append(lbroute_steps[0](state='absent', check_mode='no'))

    full_cycle(playbook, lbroute_steps[0], cycle='present')
    full_cycle(playbook, lbroute_steps[1], cycle='present')
    full_cycle(playbook, lbroute_steps[1], cycle='absent')

    # Prereqsite delete
    playbook.append(lbvserver_steps[0](state='absent', check_mode='no'))
    playbook.append(lbvserver_steps[1](state='absent', check_mode='no'))



    save_test(args, 'lbroute', playbook)

def generate_all(args):
    generate_monitor(args)
    generate_lbprofile(args)
    generate_lbroute(args)
