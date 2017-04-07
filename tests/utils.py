import subprocess
import time
import os
import pyaml
import json
import re


TESTDIR = os.path.join(os.getcwd(), 'testdir')
INVENTORY = '\n'.join(['[netscaler]', '', '172.18.1.1'])
ANSIBLE_MODULE_PATH = os.path.join(os.getcwd(), 'ansible-modules')

DOCKER_NAME = 'test_fixture'
DOCKER_NET = 'mynet'
DOCKER_IP = '172.18.0.2'

nitro_dict = {
    'nsip': DOCKER_IP,
    'nitro_user': 'nsroot',
    'nitro_pass': 'nsroot',
    'ssl_cert_validation': 'no',
}


def ensure_pristine_cpx(name=DOCKER_NAME, net=DOCKER_NET, ip=DOCKER_IP):
    output = subprocess.check_output('docker ps -a -f name=%s' % name, shell=True)
    #print('output %s' % len(output.split('\n')))
    if len(output.split('\n')) != 2:
        print('Removing existing container')
        subprocess.check_call('docker stop %s' % name, shell=True)
        subprocess.check_call('docker rm %s' % name, shell=True)
    retval = subprocess.check_call('docker run -dt -p 22 -p 80 -p 161/udp -e EULA-yes --ulimit core=-1 --privileged=true --name %s --net %s  --ip %s  cpx:11.1-48.10 ' % (name, net, ip), shell=True)
    time.sleep(10)



def ensure_cpx_up(name):
    output = subprocess.check_output('docker ps -f name=%s' % name, shell=True)
    if output == '':
        raise Exception('cpx is not up')

def ensure_teardown_cpx(name):
    retval = subprocess.check_call('docker stop %s' % name, shell=True)
    retval = subprocess.check_call('docker rm %s' % name, shell=True)

    print(retval)

def run_ansible_play(play_dict, ansible_module_path=ANSIBLE_MODULE_PATH, inventory=INVENTORY, testdir=TESTDIR, testcase=None):

    if testcase is not None:
        testdir = os.path.join(testdir, testcase)

    if not os.path.exists(testdir):
        os.makedirs(testdir)

    test_log = os.path.join(testdir, 'test.log')
    inventory_file = os.path.join(testdir, 'inventory.txt')
    play_yml = os.path.join(testdir, 'play.yml')

    # Remove stale logs
    if os.path.exists(test_log):
        os.remove(test_log)

    # Write dict to proper yaml playbook
    with open(play_yml, 'w') as fh:
        fh.write(pyaml.dumps(play_dict))

    # Write the inventory
    with open(inventory_file, 'w') as fh:
        fh.write(inventory)


    actual_command = 'ANSIBLE_LOG_PATH="%s" ansible-playbook -i %s -M %s %s -vvv' % (test_log, inventory_file, ansible_module_path,  play_yml)
    print(actual_command)
    retval = subprocess.call(actual_command, shell=True)

    # Parse json return object from verbose log output
    with open(test_log, 'r') as fh:
        json_lines = []
        in_json = False
        for line in fh:
            if not in_json:
                # Start of ansible return json
                if '{' in line:
                    json_lines.append(line[line.index('{'):])
                    in_json = True
            else:
                json_lines.append(line)
                # break at last line of ansible return json
                if re.match(r'^}$', line) is not None:
                    break

    # Return json object or None for failed parsing
    if len(json_lines) > 0:
        return json.loads(''.join(json_lines))
    else:
        return None
