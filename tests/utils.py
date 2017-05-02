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

import subprocess
import time
import os
import pyaml
import json
import re
import unittest
import sys
import paramiko

import pexpect

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

def get_nitro_client():
    from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service

    client = nitro_service(nitro_dict['nsip'], 'HTTPS')
    client.set_credential(nitro_dict['nitro_user'], nitro_dict['nitro_pass'])
    client.timeout = 320.0
    client.certvalidation = False
    client.login()
    return client

from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception


def make_dnsprofile(profilename):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsprofile import dnsprofile
        profile = dnsprofile()
        profile.dnsprofilename = profilename
        dnsprofile.add(client, profile)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)

def make_metrictable(tablename):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmetrictable import lbmetrictable
        table = lbmetrictable()
        table.metrictable = tablename
        lbmetrictable.add(client, table)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)

def make_server(name, ipaddress):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.basic.server import server
        myserver = server()
        myserver.name = name
        myserver.ipaddress = ipaddress
        server.add(client, myserver)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_tcpprofile(profilename):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nstcpprofile import nstcpprofile
        profile = nstcpprofile()
        profile.name = profilename
        nstcpprofile.add(client, profile)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_netprofile(profilename):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.network.netprofile import netprofile
        profile = netprofile()
        profile.name = profilename
        netprofile.add(client, profile)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_httpprofile(profilename):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nshttpprofile import nshttpprofile
        profile = nshttpprofile()
        profile.name = profilename
        nshttpprofile.add(client, profile)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_authnprofile(profilename, authnvsname, authenticationhost, authenticationdomain, authenticationlevel):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.authentication.authenticationauthnprofile import authenticationauthnprofile
        profile = authenticationauthnprofile()
        profile.name = profilename
        profile.authnvsname = authnvsname
        profile.authenticationhost = authenticationhost
        profile.authenticationdomain = authenticationdomain
        profile.authenticationlevel = authenticationlevel
        authenticationauthnprofile.add(client, profile)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_logaction(name, serverip):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.audit.auditnslogaction import auditnslogaction
        action = auditnslogaction()
        action.name = name
        action.serverip = serverip
        action.loglevel = 'ERROR'
        auditnslogaction.add(client, action)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_dbprofile(name):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.db.dbdbprofile import dbdbprofile
        profile = dbdbprofile()
        profile.name = name
        dbdbprofile.add(client, profile)
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_dbuser(username, password):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.db.dbuser import dbuser
        user = dbuser()
        user.username = username
        user.password = password
        dbuser.add(client, user)
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e

def make_vpnvserver(name,ipaddress):
    client = get_nitro_client()
    try:
        from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnvserver import vpnvserver
        vserver = vpnvserver()
        vserver.name = name
        vserver.ipv46 = ipaddress
        vserver.servicetype = 'SSL'
        vpnvserver.add(client, vserver)
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        print(msg)
        raise e


def ensure_teardown_cpx(name):
    retval = subprocess.check_call('docker stop %s' % name, shell=True)
    retval = subprocess.check_call('docker rm %s' % name, shell=True)

    print(retval)

def copy_sslcertificate_to_cpx():
    transport = paramiko.Transport(DOCKER_IP, 22)
    transport.connect(username='root', password='linux')
    sftp = paramiko.SFTPClient.from_transport(transport)
    here = os.path.dirname(os.path.realpath(__file__))
    for file in ['server.crt', 'server.key', 'server2.key', 'server2.crt']:
        sftp.put(os.path.join(here, 'datafiles', file), os.path.join('/nsconfig/ssl', file))

def get_service_monitor_bindings_list(client, service_name):
    from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
    try:
        bindings = service_lbmonitor_binding.get(client, service_name)
        return [ item.monitor_name for item in bindings]
    except nitro_exception as e:
        if e.errorcode == 344:
            return []
        else:
            raise e

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
