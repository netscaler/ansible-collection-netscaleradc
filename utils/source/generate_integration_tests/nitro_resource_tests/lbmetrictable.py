from . import *

def generate_all(args):
    playbook = []
    resource= {
        'lbmetrictable': {
            'metrictable': 'integration_test_metric_table',
        },
        'lbmetrictable_metric_binding_1': {
            'metrictable': 'integration_test_metric_table',
            'metric': 'currentconn',
            'Snmpoid': '1.3.6.1.4.1.3375.1.1.1.2.10.0',
        },
        'lbmetrictable_metric_binding_2': {
            'metrictable': 'integration_test_metric_table',
            'metric': 'cpu',
            'Snmpoid': '1.3.6.1.4.1.5951.4.1.1.41.1.0',
        }
    }
    lbmetrictable_step = functools.partial(
        generate_step,
        workflow_key='lbmetrictable',
        resource=resource['lbmetrictable']
    )

    metric_1_step = functools.partial(
        generate_step,
        workflow_key='lbmetrictable_metric_binding',
        resource=resource['lbmetrictable_metric_binding_1']
    )

    metric_2_step = functools.partial(
        generate_step,
        workflow_key='lbmetrictable_metric_binding',
        resource=resource['lbmetrictable_metric_binding_2']
    )

    full_cycle(playbook, lbmetrictable_step, cycle='present')
    full_cycle(playbook, metric_1_step, cycle='present')
    full_cycle(playbook, metric_2_step, cycle='present')

    full_cycle(playbook, metric_1_step, cycle='absent')
    full_cycle(playbook, metric_2_step, cycle='absent')

    full_cycle(playbook, lbmetrictable_step, cycle='absent')

    save_test(args, 'lbmetrictable', playbook)
