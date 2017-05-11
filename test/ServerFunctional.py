#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import unittest
import subprocess
import os.path
import os
import functools

from . import utils


def setUpModule():
    pass

def tearDownModule():
    pass


minimal_attrs = {
    'name': 'vserver1',
    'ipaddress': '192.168.1.1',
}

class ServerFullInitalValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utils.ensure_pristine_cpx()


    def test_01(self):
        playbook = [{
            'hosts': 'netscaler',
            'gather_facts': False,
            'tasks': [{
                'name': 'Setup server',
                'local_action': {
                    'module': 'netscaler_server',
                    'operation': 'present',

                    'name': 'server1',
                    'ipaddress': '192.168.1.1',

                }
            }]
        }]
        playbook[0]['tasks'][0]['local_action'].update(utils.nitro_dict)
        result = utils.run_ansible_play(playbook, testcase='server_test_01')
        self.assertIsNotNone(result, msg='Result from playbook run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertTrue(result['changed'], msg='Changed status was not set correctly')

        # Make second run
        result = utils.run_ansible_play(playbook, testcase='server_test_01_second_run')
        self.assertIsNotNone(result, msg='Result from playbook second run did not return valid json')
        self.assertFalse(result['failed'], msg='Playbook initial returned failed status')
        self.assertFalse(result['changed'], msg='Changed status was not set correctly')
