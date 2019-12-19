from . import *

def generate_all(args):
    playbook = []
    resources = {
        'spilloverpolicy': {
            'name': 'myspilloverpolicy',
            'rule': 'SYS.VSERVER("vserver").RESPTIME.GT(100)',
            'action': 'spillover',
            'comment': 'original comment',
        },
    }

    policy_step = functools.partial(
        generate_step,
        workflow_key='spilloverpolicy',
        resource=copy.deepcopy(resources['spilloverpolicy'])
    )

    resource = copy.deepcopy(resources['spilloverpolicy'])
    resource['comment'] = 'new comment'
    policy_modified_step = functools.partial(
        generate_step,
        workflow_key='spilloverpolicy',
        resource=resource,
    )

    # Make sure starting state is clear
    playbook.append(policy_step(state='absent', check_mode='no'))

    # Full cycles for lbgroup and standalone bindings
    full_cycle(playbook, policy_step, cycle='present')
    full_cycle(playbook, policy_modified_step, cycle='present')
    full_cycle(playbook, policy_modified_step, cycle='absent')

    save_test(args, 'spilloverpolicy', playbook)
