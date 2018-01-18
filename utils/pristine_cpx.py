#!/usr/bin/env python

import subprocess
import time
import paramiko
import sys
import os.path

if len(sys.argv) == 1 or sys.argv[1] == '120':
    DOCKER_NAME = 'test_fixture_120'
    DOCKER_NET = 'mynet'
    DOCKER_IP = '172.18.0.200'
    DOCKER_IMAGE = 'cpx:12.0-41.22'
    DOCKER_EXTRA = ''
elif sys.argv[1] == '111':
    DOCKER_NAME = 'test_fixture_111'
    DOCKER_NET = 'mynet'
    DOCKER_IP = '172.18.0.2'
    DOCKER_IMAGE = 'cpx:11.1-48.10'
    DOCKER_EXTRA = ''

cmd = 'docker ps -a --filter name=%s' % DOCKER_NAME
print('cmd: %s' % cmd)
output = subprocess.check_output(cmd, shell=True)
print('output is %s' % str(output))
print('output len %s' % len(str(output).split('\n')))
if DOCKER_NAME in str(output):
    print('Removing existing container')
    subprocess.check_call('docker stop %s' % DOCKER_NAME, shell=True)
    subprocess.check_call('docker rm %s' % DOCKER_NAME, shell=True)

if len(sys.argv) == 1 or sys.argv[1] == '120':
    subprocess.check_call('docker run -dt -p 22 -p 80 -p 161/udp -e EULA-yes --ulimit core=-1 -v /var/cpx:/cpx --cap-add=NET_ADMIN --name %s --net %s  --ip %s  %s ' % (DOCKER_NAME, DOCKER_NET, DOCKER_IP, DOCKER_IMAGE), shell=True)
elif sys.argv[1] == '111':
    subprocess.check_call('docker run -dt -p 22 -p 80 -p 161/udp -e EULA-yes --ulimit core=-1 --privileged=true --name %s --net %s  --ip %s  %s ' % (DOCKER_NAME, DOCKER_NET, DOCKER_IP, DOCKER_IMAGE), shell=True)
time.sleep(10)



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(DOCKER_IP, username='root', password='linux')

stdin, stdout, stderr = ssh.exec_command('/var/netscaler/bins/cli_script.sh "add tcpprofile tcp-profile-1"')
print('stdout lines %s' % stdout.readlines())
print('stderr lines %s' % stderr.readlines())

stdin, stdout, stderr = ssh.exec_command('/var/netscaler/bins/cli_script.sh "add netprofile net-profile-1"')
print('stdout lines %s' % stdout.readlines())
print('stderr lines %s' % stderr.readlines())

stdin, stdout, stderr = ssh.exec_command('/var/netscaler/bins/cli_script.sh "add httpprofile http-profile-1"')
print('stdout lines %s' % stdout.readlines())
print('stderr lines %s' % stderr.readlines())

stdin, stdout, stderr = ssh.exec_command('/var/netscaler/bins/cli_script.sh "add dnsprofile dns-profile-1"')
print('stdout lines %s' % stdout.readlines())
print('stderr lines %s' % stderr.readlines())

transport = paramiko.Transport(DOCKER_IP, 22)
transport.connect(username='root', password='linux')
sftp = paramiko.SFTPClient.from_transport(transport)
here = os.path.dirname(os.path.realpath(__file__))
for file in ['server.crt', 'server.key', 'server2.key', 'server2.crt']:
    sftp.put(os.path.join(here, '..', 'test', 'datafiles', file), os.path.join('/nsconfig/ssl', file))
