from . import *

def generate_service(args):
    playbook = []
    resources = {
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
        'lbmonitors':[
            {
                'monitorname': 'lb-monitor-http',
                'type': 'HTTP',
            },
            {
                'monitorname': 'lb-monitor-http-inline',
                'type': 'HTTP-INLINE',
            },
        ],
        'service_lbmonitor_bindings': [
            {
                'name': 'service-http-1',
                'monitor_name': 'lb-monitor-http',
            },
            {
                'name': 'service-http-1',
                'monitor_name': 'lb-monitor-http-inline',
            },
        ],
        'service_tcp_default_binding': {
            'name': 'service-http-1',
            'monitor_name': 'tcp-default',
        },
    }

    service_step = functools.partial(
        generate_step,
        workflow_key='service',
        resource=resources['services'][0],
    )

    lbmonitor_steps = []
    for item in resources['lbmonitors']:
        step = functools.partial(
            generate_step,
            workflow_key='lbmonitor',
            resource=item
        )
        lbmonitor_steps.append(step)

    service_lbmonitor_binding_steps = []
    for item in resources['service_lbmonitor_bindings']:
        step = functools.partial(
            generate_step,
            workflow_key='service_lbmonitor_binding',
            resource=item
        )
        service_lbmonitor_binding_steps.append(step)

    resource=copy.deepcopy(resources['service_lbmonitor_bindings'])
    resource.append(copy.deepcopy(resources['service_tcp_default_binding']))
    service_lbmonitor_binding_list_full_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='service_lbmonitor_binding',
        resource=resource,
    )

    resource=copy.deepcopy(resources['service_lbmonitor_bindings'][:-1])
    resource.append(copy.deepcopy(resources['service_tcp_default_binding']))
    service_lbmonitor_binding_list_short_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='service_lbmonitor_binding',
        resource=resource,
    )

    # Clean up remains
    playbook.append(service_step(state='absent', check_mode='no'))

    # Standalone full cycle

    playbook.append(service_step(state='present', check_mode='no'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_CHANGED_STEP))

    playbook.append(service_step(state='absent', check_mode='no'))
    playbook.append(copy.deepcopy(ASSERT_RESULT_CHANGED_STEP))

    # Prerequisites for next steps
    playbook.append(service_step(state='present', check_mode='no'))
    playbook.append(lbmonitor_steps[0](state='present', check_mode='no'))
    playbook.append(lbmonitor_steps[1](state='present', check_mode='no'))

    # full cycle lbmonitor bidings
    full_cycle(playbook, service_lbmonitor_binding_steps[0], cycle='present')
    full_cycle(playbook, service_lbmonitor_binding_steps[1], cycle='present')
    full_cycle(playbook, service_lbmonitor_binding_steps[1], cycle='absent')
    full_cycle(playbook, service_lbmonitor_binding_steps[0], cycle='absent')

    # fails trying to delete default tcp monitor
    # full cycle lbmonitor binding list
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_short_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='present')
    #full_cycle(playbook, service_lbmonitor_binding_list_full_step, cycle='absent')

    # Prerequisites clean up
    playbook.append(service_step(state='absent', check_mode='no'))
    playbook.append(lbmonitor_steps[0](state='absent', check_mode='no'))
    playbook.append(lbmonitor_steps[1](state='absent', check_mode='no'))

    save_test(args, 'service', playbook)

def generate_servicegroup(args):
    pass
    playbook = []
    resources = {
        'servicegroup': {
                'servicegroupname': 'integration-test-servicegroup-1',
                'servicetype': 'HTTP',
            },

        'lbmonitors':[
            {
                'monitorname': 'lb-monitor-http',
                'type': 'HTTP',
            },
            {
                'monitorname': 'lb-monitor-http-inline',
                'type': 'HTTP-INLINE',
            },
        ],
        'servicegroup_lbmonitor_bindings': [
            {
                'servicegroupname': 'integration-test-servicegroup-1',
                'monitor_name': 'lb-monitor-http',
            },
            {
                'servicegroupname': 'integration-test-servicegroup-1',
                'monitor_name': 'lb-monitor-http-inline',
            },
        ]
    }

    servicegroup_step = functools.partial(
        generate_step,
        workflow_key='servicegroup',
        resource=resources['servicegroup']
    )

    lbmonitor_steps = []
    for item in resources['lbmonitors']:
        step = functools.partial(
            generate_step,
            workflow_key='lbmonitor',
            resource=item
        )
        lbmonitor_steps.append(step)

    servicegroup_lbmonitor_binding_steps = []
    for item in resources['servicegroup_lbmonitor_bindings']:
        step = functools.partial(
            generate_step,
            workflow_key='servicegroup_lbmonitor_binding',
            resource=item
        )
        servicegroup_lbmonitor_binding_steps.append(step)

    servicegroup_lbmonitor_binding_list_full_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='servicegroup_lbmonitor_binding',
        resource=copy.deepcopy(resources['servicegroup_lbmonitor_bindings'])
    )

    servicegroup_lbmonitor_binding_list_short_step = functools.partial(
        generate_bindings_list_step,
        workflow_key='servicegroup_lbmonitor_binding',
        resource=copy.deepcopy(resources['servicegroup_lbmonitor_bindings'][:-1])
    )


    # Clean up remains
    playbook.append(servicegroup_step(state='absent', check_mode='no'))

    # Full cycle
    full_cycle(playbook, servicegroup_step, cycle='present')
    full_cycle(playbook, servicegroup_step, cycle='absent')

    # Prerequisites
    playbook.append(servicegroup_step(state='present', check_mode='no'))
    playbook.append(lbmonitor_steps[0](state='present', check_mode='no'))
    playbook.append(lbmonitor_steps[1](state='present', check_mode='no'))

    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[0], cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[1], cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[1], cycle='absent')
    full_cycle(playbook, servicegroup_lbmonitor_binding_steps[0], cycle='absent')

    full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_list_short_step, cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='present')
    full_cycle(playbook, servicegroup_lbmonitor_binding_list_full_step, cycle='absent')

    save_test(args, 'servicegroup', playbook)

def generate_all(args):
    generate_service(args)
    generate_servicegroup(args)
