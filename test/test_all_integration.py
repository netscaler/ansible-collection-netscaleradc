
import sys
if sys.version_info[0] == 2:
    import unittest2 as unittest
else:
    import unittest

import subprocess
import os
import os.path


class IntegrationTests(unittest.TestCase):
    def test_run_all_integration_tests(self):
        here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
        os.chdir(os.path.join(here, 'integration'))
        inventory_file = os.path.join(here, 'integration', 'inventory.txt')
        playbook_yml = os.path.join(here, 'integration', 'netscaler.yml')
        argument_list = ['ansible-playbook', '-i', inventory_file]
        tags = os.getenv('ANSIBLE_TAGS')
        if tags is not None:
            argument_list.extend(['--tags', tags])
        argument_list.extend([playbook_yml, '-vvvv'])
        retval = subprocess.call(argument_list)
        self.assertEqual(retval, 0, msg='Running of integration tests\' playbook failed')
