#!/usr/bin/env python

import subprocess
import time
import paramiko
import sys

if len(sys.argv) == 1 or sys.argv[1] == '111':
    DOCKER_NAME = 'test_fixture_111'
    DOCKER_NET = 'mynet'
    DOCKER_IP = '172.18.0.2'
    DOCKER_IMAGE= 'cpx:11.1-48.10'
    DOCKER_EXTRA=''
elif sys.argv[1] == '120':
    DOCKER_NAME = 'test_fixture_120'
    DOCKER_NET = 'mynet'
    DOCKER_IP = '172.18.0.200'
    DOCKER_IMAGE= 'cpx:12.0-41.22'
    DOCKER_EXTRA=''

output = subprocess.check_output('docker ps -a -f name=%s' % DOCKER_NAME, shell=True)
# print('output %s' % len(output.split('\n')))
if len(str(output).split('\n')) != 2:
    print('Removing existing container')
    subprocess.check_call('docker stop %s' % DOCKER_NAME, shell=True)
    subprocess.check_call('docker rm %s' % DOCKER_NAME, shell=True)

if len(sys.argv) == 1 or sys.argv[1] == '111':
    subprocess.check_call('docker run -dt -p 22 -p 80 -p 161/udp -e EULA-yes --ulimit core=-1 --privileged=true --name %s --net %s  --ip %s  %s ' % (DOCKER_NAME, DOCKER_NET, DOCKER_IP, DOCKER_IMAGE), shell=True)
elif sys.argv[1] == '120':
    subprocess.check_call('docker run -dt -p 22 -p 80 -p 161/udp -e EULA-yes --ulimit core=-1 -v /var/cpx:/cpx --cap-add=NET_ADMIN --name %s --net %s  --ip %s  %s ' % (DOCKER_NAME, DOCKER_NET, DOCKER_IP, DOCKER_IMAGE), shell=True)
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
