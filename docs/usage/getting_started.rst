Getting Started
===============

This document will show you how to begin using the Netscaler Ansible modules.

First, obtain `Python 2.7`_ and `Ansible`_ if you do not already have them.

The version of Ansible that is required is at least 2.4.0.

Installing Ansible
------------------

Installing Ansible may be accomplished through the following methods.

Further documentation on installing Ansible  may be found in `github`_

.. _github: https://github.com/ansible/ansible

Using pip
+++++++++


.. code-block:: bash

   pip install ansible

Using your package manager
++++++++++++++++++++++++++

E.g. in a Debian based Linux distribution

.. code-block:: bash

   apt-get install ansible

Using a direct checkout
+++++++++++++++++++++++

.. code-block:: bash

   git clone https://github.com/ansible/ansible
   
   cd ansible
   
   source hacking/env-setup

Verifying the installation
++++++++++++++++++++++++++

Following any installation method you should be able to run the following
code which will print out the ansible version you will be using

.. code-block:: bash

   ansible --version



Installing Modules
------------------

To install the latest version of the Netscaler modules run the following commands

.. code-block:: bash

   git clone https://github.com/citrix/netscaler-ansible-modules
   
   cd netscaler-ansible-modules
   
   python install.py

The install script will detect where the ansible library is installed and will try
to copy the module files to the appropriate directories.

.. note:: The last step may require root priviledges depending on where ansible
          is installed.



Playbook
--------

Last we are going to see how to make a simple playbook. 

.. code-block:: yaml

   - name: Create a server
       delegate_to: localhost
       gather_facts: no

       netscaler_server:
           nsip: 172.18.0.2
           nitro_user: nsroot
           nitro_pass: nsroot

           state: present

           name: test-server-1
           ipaddress: 192.168.1.1





.. _Ansible: http://docs.ansible.com/ansible/intro_installation.html
.. _Python 2.7: http://www.python.org/
