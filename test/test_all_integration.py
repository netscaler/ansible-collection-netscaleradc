
import sys
if sys.version_info[0] == 2:
    import unittest2 as unittest
else:
    import unittest

import subprocess
import os
import os.path
import copy


class IntegrationTests(unittest.TestCase):
    def test_run_all_integration_tests(self):
        here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
        #os.chdir(os.path.join(here, 'integration'))
        # Iterate roles dir to get all modules integration tests
        roles_dir = os.path.join(here, 'integration', 'roles')
        modules = []
        for item in os.listdir(roles_dir):
            if os.path.isdir(os.path.join(roles_dir, item)):
                modules.append(item)
        vpx_only = [
            'netscaler_gslb_service',
            'netscaler_gslb_vserver',
            'netscaler_gslb_site',
        ]

        # Get target netscaler
        # Default to CPX
        netscaler_target = os.getenv('NETSCALER_TARGET', 'CPX')
        inventory_file = {
            'CPX': 'inventory.txt',
            'VPX': 'inventory_vpx.txt',
        }[netscaler_target]
        # Run collected tests
        for module in modules:
            inventory_file = os.path.join(here, 'integration', inventory_file)
            playbook_yml = os.path.join(here, 'integration', 'netscaler.yaml')
            argument_list = ['ansible-playbook', '-i', inventory_file]
            tags = os.getenv('ANSIBLE_TAGS')
            if tags is not None:
                argument_list.extend(['--tags', tags])
            argument_list.extend(['-e', 'limit_to=%s' % module])
            argument_list.extend([playbook_yml, '-vvv'])


            with self.subTest(module=module):
                if module in vpx_only and netscaler_target != 'VPX':
                    self.skipTest('Skipping VPX only module %s' % module)
                print('Running %s' % ' '.join(argument_list))
                retval = subprocess.call(argument_list)
                self.assertEqual(retval, 0, msg='Running of integration tests\' for module %s failed.' % module)

    def old_test_run_all_integration_tests(self):
        here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
        os.chdir(os.path.join(here, 'integration'))
        inventory_file = os.path.join(here, 'integration', 'inventory.txt')
        playbook_yml = os.path.join(here, 'integration', 'netscaler.yaml')
        argument_list = ['ansible-playbook', '-i', inventory_file]
        tags = os.getenv('ANSIBLE_TAGS')
        if tags is not None:
            argument_list.extend(['--tags', tags])
        argument_list.extend([playbook_yml, '-vvvv'])
        retval = subprocess.call(argument_list)
        self.assertEqual(retval, 0, msg='Running of integration tests\' playbook failed')
