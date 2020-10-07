# Copyright (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
# Copyright 2015 Abhijit Menon-Sen <ams@2ndQuadrant.com>
# Copyright 2017 Toshio Kuratomi <tkuratomi@ansible.com>
# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    connection: ssh_citrix_adc
    short_description: connect via ssh client binary with Citrix ADC bypassing the cli
    description:
        - This connection plugin allows ansible to communicate to the target machines via normal ssh command line.
        - Ansible does not expose a channel to allow communication between the user and the ssh process to accept
          a password manually to decrypt an ssh key when using this connection plugin (which is the default). The
          use of ``ssh-agent`` is highly recommended.
    author: Sergios Lenis (sergios.lenis@citrix.com)
    version_added: "2.8"
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
                version_added: '2.5'
          env:
              - name: ANSIBLE_HOST_KEY_CHECKING
              - name: ANSIBLE_SSH_HOST_KEY_CHECKING
                version_added: '2.5'
          vars:
              - name: ansible_host_key_checking
                version_added: '2.5'
              - name: ansible_ssh_host_key_checking
                version_added: '2.5'
      password:
          description: Authentication password for the C(remote_user). Can be supplied as CLI option.
          vars:
              - name: ansible_password
              - name: ansible_ssh_pass
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
                version_added: '2.7'
      ssh_common_args:
          description: Common extra args for all ssh CLI tools
          ini:
              - section: 'ssh_connection'
                key: 'ssh_common_args'
                version_added: '2.7'
          env:
              - name: ANSIBLE_SSH_COMMON_ARGS
                version_added: '2.7'
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
          #const: ANSIBLE_SSH_EXECUTABLE
          version_added: "2.2"
          vars:
              - name: ansible_ssh_executable
                version_added: '2.7'
      sftp_executable:
          default: sftp
          description:
            - This defines the location of the sftp binary. It defaults to ``sftp`` which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SFTP_EXECUTABLE}]
          ini:
          - {key: sftp_executable, section: ssh_connection}
          version_added: "2.6"
          vars:
              - name: ansible_sftp_executable
                version_added: '2.7'
      scp_executable:
          default: scp
          description:
            - This defines the location of the scp binary. It defaults to `scp` which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SCP_EXECUTABLE}]
          ini:
          - {key: scp_executable, section: ssh_connection}
          version_added: "2.6"
          vars:
              - name: ansible_scp_executable
                version_added: '2.7'
      scp_extra_args:
          description: Extra exclusive to the ``scp`` CLI
          vars:
              - name: ansible_scp_extra_args
          env:
            - name: ANSIBLE_SCP_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: scp_extra_args
              section: ssh_connection
              version_added: '2.7'
      sftp_extra_args:
          description: Extra exclusive to the ``sftp`` CLI
          vars:
              - name: ansible_sftp_extra_args
          env:
            - name: ANSIBLE_SFTP_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: sftp_extra_args
              section: ssh_connection
              version_added: '2.7'
      ssh_extra_args:
          description: Extra exclusive to the 'ssh' CLI
          vars:
              - name: ansible_ssh_extra_args
          env:
            - name: ANSIBLE_SSH_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: ssh_extra_args
              section: ssh_connection
              version_added: '2.7'
      retries:
          # constant: ANSIBLE_SSH_RETRIES
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
                version_added: '2.7'
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
            #- name: ANSIBLE_SSH_PIPELINING
          ini:
            - section: defaults
              key: pipelining
            #- section: ssh_connection
            #  key: pipelining
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
            version_added: '2.7'
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
            version_added: '2.7'
      sftp_batch_mode:
        default: 'yes'
        description: 'TODO: write it'
        env: [{name: ANSIBLE_SFTP_BATCH_MODE}]
        ini:
        - {key: sftp_batch_mode, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_sftp_batch_mode
            version_added: '2.7'
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
            version_added: '2.7'
      use_tty:
        version_added: '2.5'
        default: 'yes'
        description: add -tt to ssh commands to force tty allocation
        env: [{name: ANSIBLE_SSH_USETTY}]
        ini:
        - {key: usetty, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_ssh_use_tty
            version_added: '2.7'
'''

import os
import time
import codecs

from functools import wraps
from ansible import constants as C
from ansible.errors import AnsibleError, AnsibleConnectionFailure, AnsibleFileNotFound
from ansible.errors import AnsibleOptionsError
from ansible.compat import selectors
from ansible.module_utils.six import PY3, text_type, binary_type
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.module_utils.parsing.convert_bool import BOOLEANS, boolean
from ansible.plugins.connection import ConnectionBase, BUFSIZE
from ansible.utils.path import unfrackpath, makedirs_safe
from ansible.plugins.connection.ssh import Connection as ConnectionSsh
from ansible.plugins.loader import become_loader

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


SSHPASS_AVAILABLE = None


class AnsibleControlPersistBrokenPipeError(AnsibleError):
    ''' ControlPersist broken pipe '''
    pass


def _ssh_retry(func):
    """
    Decorator to retry ssh/scp/sftp in the case of a connection failure

    Will retry if:
    * an exception is caught
    * ssh returns 255
    Will not retry if
    * remaining_tries is <2
    * retries limit reached
    ######
    patched to remove the output of the citrix adc cli
    ######

    """
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        import re

        remaining_tries = int(C.ANSIBLE_SSH_RETRIES) + 1
        cmd_summary = "%s..." % args[0]
        for attempt in range(remaining_tries):
            cmd = args[0]
            if attempt != 0 and self._play_context.password and isinstance(cmd, list):
                # If this is a retry, the fd/pipe for sshpass is closed, and we need a new one
                self.sshpass_pipe = os.pipe()
                cmd[1] = b'-d' + to_bytes(self.sshpass_pipe[0], nonstring='simplerepr', errors='surrogate_or_strict')

            try:
                try:
                    ##################################
                    # override to remove/intersept 'Done' of citrix adc
                    return_tuple = func(self, *args, **kwargs)
                    return_tuple = list(return_tuple)
                    subst = ""
                    regex = r"(\r\n|\r|\n|)( Done)(\r\n|\r|\n)+"
                    return_tuple[1] = re.sub(regex, subst, codecs.decode(return_tuple[1]), 0, re.UNICODE)
                    return_tuple = tuple(return_tuple)
                    # end
                    ###############################
                    display.vvv(return_tuple, host=self.host)

                    # 0 = success
                    # 1-254 = remote command return code
                    # 255 = failure from the ssh command itself
                    #
                except (AnsibleControlPersistBrokenPipeError) as e:
                    # Retry one more time because of the ControlPersist broken pipe (see #16731)
                    display.vvv(u"RETRYING BECAUSE OF CONTROLPERSIST BROKEN PIPE")
                    return_tuple = func(self, *args, **kwargs)

                if return_tuple[0] != 255:
                    break
                else:
                    raise AnsibleConnectionFailure("Failed to connect to the host via ssh: %s" % to_native(return_tuple[2]))
            except (AnsibleConnectionFailure, Exception) as e:
                if attempt == remaining_tries - 1:
                    raise
                else:
                    pause = 2 ** attempt - 1
                    if pause > 30:
                        pause = 30

                    if isinstance(e, AnsibleConnectionFailure):
                        msg = "ssh_retry: attempt: %d, ssh return code is 255. cmd (%s), pausing for %d seconds" % (attempt, cmd_summary, pause)
                    else:
                        msg = "ssh_retry: attempt: %d, caught exception(%s) from cmd (%s), pausing for %d seconds" % (attempt, e, cmd_summary, pause)

                    display.vv(msg, host=self.host)

                    time.sleep(pause)
                    continue

        return return_tuple
    return wrapped


class Connection(ConnectionSsh):
    ''' ssh based connections '''

    transport = 'ssh_citrix_adc'
    has_pipelining = True
    become_methods = frozenset([method.name for method in become_loader.all()]).difference(['runas'])
    name = 'ssh_citrix_adc'

    def __init__(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)

    @_ssh_retry
    def _run(self, cmd, in_data, sudoable=True, checkrc=True):
        """Wrapper around _bare_run that retries the connection
        """
        return self._bare_run(cmd, in_data, sudoable, checkrc)

    def exec_command(self, cmd, in_data=None, sudoable=True):
        ''' run a command on the remote host '''

        # Adding the 'shell' command for the citrix adc cli
        if cmd.startswith('ssh_citrix_adc'):
            cmd = cmd.replace('ssh_citrix_adc', '')
        else:
            cmd = type(cmd)("shell ") + cmd

        # we can only use tty when we are not pipelining the modules. piping
        # data into /usr/bin/python inside a tty automatically invokes the
        # python interactive-mode but the modules are not compatible with the
        # interactive-mode ("unexpected indent" mainly because of empty lines)

        ssh_executable = self._play_context.ssh_executable
        msg = u"ESTABLISH SSH CONNECTION WITH ssh_citrix_adc FOR USER: {0}, cmd: {1}".format(self._play_context.remote_user, cmd)
        display.vvv(msg, host=self._play_context.remote_addr)

        # -tt can cause various issues in some environments so allow the user
        # to disable it as a troubleshooting method.
        use_tty = self.get_option('use_tty')

        if not in_data and sudoable and use_tty:
            args = (ssh_executable, '-tt', self.host, cmd)
        else:
            args = (ssh_executable, self.host, cmd)

        cmd = self._build_command(*args)
        (returncode, stdout, stderr) = self._run(cmd, in_data, sudoable=sudoable)

    ##################################
        # Removing the stdout 'Done' from citrix adc cli
        # that can cause errors in calling scp with Done/ as
        # first folder.

        stdout = stdout.replace(" Done\n", '')
    #################################
        return (returncode, stdout, stderr)
