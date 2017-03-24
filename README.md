# Netscaler Ansible modules

Ansible modules for configuring Netscaler instances with ease


This a work in progress


To run the modules or the playbooks follow these steps

*  Have the nitro python sdk installed
*  Have the ansible framework installed
*  Copy the netscaler.py file from output to the module_utils folder of the ansible instllation you are using
*  Run the playbooks or modules directing ansible to the path of the output directory

E.g. ``` ansible-playbook -M /path/to/netscaler-modules/ansible playbook.yml```
