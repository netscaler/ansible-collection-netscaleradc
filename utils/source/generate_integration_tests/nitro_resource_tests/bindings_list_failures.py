from . import *

def generate_all(args):
    playbook = []
    resource_lbvserver = {
        'name': 'resource-lb-vserver',
        'servicetype': 'HTTP',
        'ipv46': '10.60.44.22',
        'port': '8080',
    }

    resource_service_1 = {
        'name': 'service-http-1',
        'servicetype': 'HTTP',
        'ip': '10.78.0.1',
        'port': '80',
    }

    resource_service_2 = {
        'name': 'service-http-2',
        'servicetype': 'HTTP',
        'ip': '10.78.0.2',
        'port': '80',
    }


    lbvserver_step = functools.partial(
        generate_step,
        workflow_key = 'lbvserver',
        resource = resource_lbvserver,
        check_mode = 'no'
    )

    service_1_step = functools.partial(
        generate_step,
        workflow_key = 'service',
        resource = resource_service_1,
        check_mode = 'no'
    )

    service_2_step = functools.partial(
        generate_step,
        workflow_key = 'service',
        resource = resource_service_2,
        check_mode = 'no'
    )

    def generate_test_step(workflow, resource, step_name, state):
        step = od([
            ('name', step_name),
            ('include_tasks', od([
                ('file', 'tasks/nitro_resource_task.yaml'),
                ('apply', od([
                    ('vars', od([
                        ('state', state),
                        ('check_mode', 'no'),
                        ('ignore_errors', 'yes'),
                        ('workflow_dict', workflow),
                        ('resource_attributes', resource),
                    ])),
                ])),
            ])),
         ])
        return step

    workflow_dict = od([

          ('lifecycle', 'bindings_list'),
          ('bound_resource_id', 'resource-lb-vserver'),
          ('binding_workflow', od([
                ('lifecycle', 'binding'),
                ('endpoint', 'lbvserver_service_binding'),
                ('bound_resource_missing_errorcode', '258'),
                ('primary_id_attribute', 'name'),
                ('delete_id_attributes', [ 'servicename', 'servicegroupname']),
            ])),
    ])

    bindings = [
        od([
            ('name', 'resource-lb-vserver'),
            ('servicename', 'service-http-1'),
            ('weight', '!!str 40'),
        ]),

        od([
            ('name', 'resource-lb-vserver'),
            ('servicename', 'service-http-2'),
            ('weight', '!!str 40'),
        ]),
    ]

    not_uniform_key_attributes_resource = {
        'bindings_list': copy.deepcopy(bindings)
    }
    del not_uniform_key_attributes_resource['bindings_list'][0]['servicename']

    not_uniform_step = functools.partial(
        generate_test_step,
        resource=not_uniform_key_attributes_resource,
        workflow=copy.deepcopy(workflow_dict),
        step_name='Cause not uniform key error',
        state='present',
    )

    not_uniform_key_assertion = od([
        ('name', 'Assert error msg contains("Bindings list key attributes are not uniform")'),
        ('assert', {
            'that': [
              "'msg' in result",
              'result.msg.find("Bindings list key attributes are not uniform") != -1'
          ]
        })
    ])

    multiple_primary_ids_resource = {
        'bindings_list': copy.deepcopy(bindings)
    }
    multiple_primary_ids_resource['bindings_list'][0]['name'] = 'other-lb-vserver'

    multiple_primary_ids_step = functools.partial(
        generate_test_step,
        resource=multiple_primary_ids_resource,
        workflow=copy.deepcopy(workflow_dict),
        step_name='Cause multiple primary ids error',
        state='present',
    )

    multiple_primary_ids_assertion = od([
        ('name', 'Assert error msg contains("Need to have only one primary id value")'),
        ('assert',{
            'that': [
              "'msg' in result",
              'result.msg.find("Need to have only one primary id value") != -1'
          ]
        }),
    ])

    empty_bindings_list_step = functools.partial(
        generate_test_step,
        resource={'bindings_list': []},
        workflow=copy.deepcopy(workflow_dict),
        step_name='Cause empty items list error',
        state='present',
    )

    empty_bindings_list_assertion = od([
        ('name', 'Assert error msg contains("Bindings list must have at least one item.")'),
        ('assert',{
            'that': [
              "'msg' in result",
              'result.msg.find("Bindings list must have at least one item.") != -1'
          ]
        }),
    ])



    # Create prerequisites
    #playbook.append(lbvserver_step(state='present', step_name='Create prerequisite lb vserver'))
    #playbook.append(service_1_step(state='present', step_name='Create prerequisite service 1'))
    #playbook.append(service_2_step(state='present', step_name='Create prerequisite service 2'))

    playbook.append(not_uniform_step())
    playbook.append(not_uniform_key_assertion)

    playbook.append(multiple_primary_ids_step())
    playbook.append(multiple_primary_ids_assertion)

    playbook.append(empty_bindings_list_step())
    playbook.append(empty_bindings_list_assertion)

    # Delete prerequisites
    #playbook.append(lbvserver_step(state='absent', step_name='Delete prerequisite lb vserver'))
    #playbook.append(service_1_step(state='absent', step_name='Delete prerequisite service 1'))
    #playbook.append(service_2_step(state='absent', step_name='Delete prerequisite service 2'))

    save_test(args, 'bindings_list_failures', playbook)
