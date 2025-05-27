# Copyright (c) 2025 Cloud Software Group, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
    name: ssh_netscaler_adc
    short_description: connect via ssh client binary with Netscaler ADC bypassing the cli
    description:
        - This connection plugin allows ansible to communicate to the target Netscaler ADC via normal ssh command line.
        - The only authentication method that works with this plugin is with ssh key file.
        - The input options supported by this connection plugin are the same as the ssh connection plugin of Ansible.
    author:
        - George Nikolopoulos (@giorgos-nikolopoulos)
        - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
    version_added: "2.7.0"
    options:
      host:
          description: Hostname/ip to connect to.
          default: inventory_hostname
          vars:
               - name: ansible_host
               - name: ansible_ssh_host
      host_key_checking:
          description: Determines if ssh should check host keys
          type: boolean
          ini:
              - section: defaults
                key: 'host_key_checking'
              - section: ssh_connection
                key: 'host_key_checking'
          env:
              - name: ANSIBLE_HOST_KEY_CHECKING
              - name: ANSIBLE_SSH_HOST_KEY_CHECKING
          vars:
              - name: ansible_host_key_checking
              - name: ansible_ssh_host_key_checking
      password:
          description: Authentication password for the C(remote_user). Can be supplied as CLI option.
          vars:
              - name: ansible_password
              - name: ansible_ssh_pass
      sshpass_prompt:
          description: Password prompt that sshpass should search for. Supported by sshpass 1.06 and up.
          default: ''
          ini:
              - section: 'ssh_connection'
                key: 'sshpass_prompt'
          env:
              - name: ANSIBLE_SSHPASS_PROMPT
          vars:
              - name: ansible_sshpass_prompt
      ssh_args:
          description: Arguments to pass to all ssh cli tools
          default: '-C -o ControlMaster=auto -o ControlPersist=60s'
          ini:
              - section: 'ssh_connection'
                key: 'ssh_args'
          env:
              - name: ANSIBLE_SSH_ARGS
          vars:
              - name: ansible_ssh_args
      ssh_common_args:
          description: Common extra args for all ssh CLI tools
          ini:
              - section: 'ssh_connection'
                key: 'ssh_common_args'
          env:
              - name: ANSIBLE_SSH_COMMON_ARGS
          vars:
              - name: ansible_ssh_common_args
      ssh_executable:
          default: ssh
          description:
            - This defines the location of the ssh binary. It defaults to ``ssh`` which will use the first ssh binary available in $PATH.
            - This option is usually not required, it might be useful when access to system ssh is restricted,
              or when using ssh wrappers to connect to remote hosts.
          env: [{name: ANSIBLE_SSH_EXECUTABLE}]
          ini:
          - {key: ssh_executable, section: ssh_connection}
          version_added: "2.0.0"
          vars:
              - name: ansible_ssh_executable
      sftp_executable:
          default: sftp
          description:
            - This defines the location of the sftp binary. It defaults to ``sftp`` which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SFTP_EXECUTABLE}]
          ini:
          - {key: sftp_executable, section: ssh_connection}
          version_added: "2.0.0"
          vars:
              - name: ansible_sftp_executable
      scp_executable:
          default: scp
          description:
            - This defines the location of the scp binary. It defaults to `scp` which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SCP_EXECUTABLE}]
          ini:
          - {key: scp_executable, section: ssh_connection}
          version_added: "2.0.0"
          vars:
              - name: ansible_scp_executable
      scp_extra_args:
          description: Extra exclusive to the ``scp`` CLI
          vars:
              - name: ansible_scp_extra_args
          env:
            - name: ANSIBLE_SCP_EXTRA_ARGS
          ini:
            - key: scp_extra_args
              section: ssh_connection
      sftp_extra_args:
          description: Extra exclusive to the ``sftp`` CLI
          vars:
              - name: ansible_sftp_extra_args
          env:
            - name: ANSIBLE_SFTP_EXTRA_ARGS
          ini:
            - key: sftp_extra_args
              section: ssh_connection
      ssh_extra_args:
          description: Extra exclusive to the 'ssh' CLI
          vars:
              - name: ansible_ssh_extra_args
          env:
            - name: ANSIBLE_SSH_EXTRA_ARGS
          ini:
            - key: ssh_extra_args
              section: ssh_connection
      retries:
          description: Number of attempts to connect.
          default: 3
          type: integer
          env:
            - name: ANSIBLE_SSH_RETRIES
          ini:
            - section: connection
              key: retries
            - section: ssh_connection
              key: retries
          vars:
              - name: ansible_ssh_retries
      reconnection_retries:
          description: Number of attempts to connect.
          default: 0
          type: integer
          env:
            - name: ANSIBLE_SSH_RETRIES
          ini:
            - section: connection
              key: retries
            - section: ssh_connection
              key: retries
          vars:
            - name: ansible_ssh_retries
      port:
          description: Remote port to connect to.
          type: int
          default: 22
          ini:
            - section: defaults
              key: remote_port
          env:
            - name: ANSIBLE_REMOTE_PORT
          vars:
            - name: ansible_port
            - name: ansible_ssh_port
      remote_user:
          description:
              - User name with which to login to the remote server, normally set by the remote_user keyword.
              - If no user is supplied, Ansible will let the ssh client binary choose the user as it normally
          ini:
            - section: defaults
              key: remote_user
          env:
            - name: ANSIBLE_REMOTE_USER
          vars:
            - name: ansible_user
            - name: ansible_ssh_user
      pipelining:
          default: ANSIBLE_PIPELINING
          description:
            - Pipelining reduces the number of SSH operations required to execute a module on the remote server,
              by executing many Ansible modules without actual file transfer.
            - This can result in a very significant performance improvement when enabled.
            - However this conflicts with privilege escalation (become).
              For example, when using sudo operations you must first disable 'requiretty' in the sudoers file for the target hosts,
              which is why this feature is disabled by default.
          env:
            - name: ANSIBLE_PIPELINING
          ini:
            - section: defaults
              key: pipelining
          type: boolean
          vars:
            - name: ansible_pipelining
            - name: ansible_ssh_pipelining
      private_key_file:
          description:
              - Path to private key file to use for authentication
          ini:
            - section: defaults
              key: private_key_file
          env:
            - name: ANSIBLE_PRIVATE_KEY_FILE
          vars:
            - name: ansible_private_key_file
            - name: ansible_ssh_private_key_file
      control_path:
        description:
          - This is the location to save ssh's ControlPath sockets, it uses ssh's variable substitution.
          - Since 2.3, if null, ansible will generate a unique hash. Use `%(directory)s` to indicate where to use the control dir path setting.
        env:
          - name: ANSIBLE_SSH_CONTROL_PATH
        ini:
          - key: control_path
            section: ssh_connection
        vars:
          - name: ansible_control_path
      control_path_dir:
        default: ~/.ansible/cp
        description:
          - This sets the directory to use for ssh control path if the control path setting is null.
          - Also, provides the `%(directory)s` variable for the control path setting.
        env:
          - name: ANSIBLE_SSH_CONTROL_PATH_DIR
        ini:
          - section: ssh_connection
            key: control_path_dir
        vars:
          - name: ansible_control_path_dir
      sftp_batch_mode:
        default: 'yes'
        description: 'TODO: write it'
        env: [{name: ANSIBLE_SFTP_BATCH_MODE}]
        ini:
        - {key: sftp_batch_mode, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_sftp_batch_mode
      ssh_transfer_method:
        description:
            - "Preferred method to use when transferring files over ssh"
            - Setting to 'smart' (default) will try them in order, until one succeeds or they all fail
            - Using 'piped' creates an ssh pipe with ``dd`` on either side to copy the data
        choices: ['sftp', 'scp', 'piped', 'smart']
        env: [{name: ANSIBLE_SSH_TRANSFER_METHOD}]
        ini:
            - {key: transfer_method, section: ssh_connection}
      scp_if_ssh:
        default: smart
        description:
          - "Prefered method to use when transfering files over ssh"
          - When set to smart, Ansible will try them until one succeeds or they all fail
          - If set to True, it will force 'scp', if False it will use 'sftp'
        env: [{name: ANSIBLE_SCP_IF_SSH}]
        ini:
        - {key: scp_if_ssh, section: ssh_connection}
        vars:
          - name: ansible_scp_if_ssh
      use_tty:
        version_added: '2.0.0'
        default: 'yes'
        description: add -tt to ssh commands to force tty allocation
        env: [{name: ANSIBLE_SSH_USETTY}]
        ini:
        - {key: usetty, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_ssh_use_tty
      timeout:
        default: 10
        description:
            - This is the default ammount of time we will wait while establishing an ssh connection
            - It also controls how long we can wait to access reading the connection once established (select on the socket)
        env:
            - name: ANSIBLE_TIMEOUT
            - name: ANSIBLE_SSH_TIMEOUT
        ini:
            - key: timeout
              section: defaults
            - key: timeout
              section: ssh_connection
        vars:
          - name: ansible_ssh_timeout
        cli:
          - name: timeout
        type: integer
      pkcs11_provider:
          description: PKCS11 SmartCard provider
          default: ''
          ini:
            - section: ssh_connection
              key: pkcs11_provider
          env:
            - name: ANSIBLE_PKCS11_PROVIDER
          vars:
            - name: ansible_pkcs11_provider
"""

import codecs

from functools import wraps
from ansible.errors import AnsibleError
from ansible.plugins.connection.ssh import Connection as ConnectionSsh

from ansible.utils.display import Display
from ansible.plugins.loader import become_loader

import re

display = Display()


SSHPASS_AVAILABLE = None


class AnsibleControlPersistBrokenPipeError(AnsibleError):
    ''' ControlPersist broken pipe '''
    pass


def _return_tuple_manipulate(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        return_tuple = func(self, *args, **kwargs)
        return_tuple = list(return_tuple)
        subst = ""
        regex = r"(\r\n|\r|\n|)( Done)(\r\n|\r|\n)+"
        return_tuple[1] = re.sub(regex, subst, codecs.decode(return_tuple[1]), 0, re.UNICODE)

        # Ansible needs some data from return_tuple[1](or stdout). So, we are returning the same to ansible
        regex2 = r'{.*}'
        try:
            return_tuple[1] = re.findall(regex2, str(return_tuple[1]))[0]
        except IndexError:
            pass
            # If no match, return the old `return_tuple[1]` (i.e., stdout)

        return_tuple = tuple(return_tuple)
        return return_tuple
    return wrapped


def _manipulate_cmd(func):

    @wraps(func)
    def wrapped(self, cmd, *args, **kwargs):
        # Adding the 'shell' command for the citrix adc cli
        if cmd.startswith('ssh_netscaler_adc'):
            cmd = cmd.replace('ssh_netscaler_adc', '')
        else:
            cmd = type(cmd)("shell ") + cmd
        returncode, stdout, stderr = func(self, cmd, *args, **kwargs)
        return (returncode, stdout, stderr)
    return wrapped


def calculate_become_methods():
    all_methods = []
    for item in become_loader.all():
        # Skip runas
        if item.name == 'runas':
            continue
        all_methods.append(item.name)

    return frozenset(all_methods)


class Connection(ConnectionSsh):
    ''' ssh based connections '''

    transport = 'ssh_netscaler_adc'
    has_pipelining = True
    become_methods = calculate_become_methods()
    name = 'ssh_netscaler_adc'

    def __init__(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)

    @_return_tuple_manipulate
    def _run(self, cmd, in_data, sudoable=True, checkrc=True):
        """Wrapper around _bare_run that retries the connection
        """
        return super(Connection, self)._run(cmd, in_data, sudoable=sudoable, checkrc=checkrc)

    @_manipulate_cmd
    def exec_command(self, cmd, in_data=None, sudoable=True):
        ''' run a command on the remote host '''

        return super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)
