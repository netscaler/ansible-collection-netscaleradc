# Netscaler Ansible modules

Ansible modules for configuring Netscaler instances with ease.


Currently the following modules are implemented

* netscaler\_cs\_action. Configure content switching actions.
* netscaler\_cs\_policy. Configure content switching policies
* netscaler\_cs\_vserver. Configure content swtiching virtual servers.
* netscaler\_lb\_monitor. Configure load balancing monitors.
* netscaler\_lb\_vserver. Configure load balancing virtual servers.
* netscaler\_server. Configure server instances.
* netscaler\_service. Configure netscaler services.
* netscaler\_servicegroup. Configure netscaler service groups.


## Installation

There is an install script in the top level directory ```install.py```.

It tries to find the ansible installation directory and then copies the module files to the appropriate places.

If the ansible installation is on a dirctory that requires root access, the install script should be run with root priviledges.

If the isntallation script fails and you know where ansible is located on your system you can do a manual installation.
Just copy the contents of the ansible-modules directory to the extras module directory and the netscaler.py file to the module_utils directory of ansible.

The modules depend on the nitro python sdk. You can download it for the 11.0 version of netscaler from the following link. https://www.citrix.com/downloads/netscaler-adc/sdks/netscaler-sdk-release-110.html

## Usage

All modules are intended to be run on the ansible control machine or a jumserver with access to the netscaler appliance.
To do this you need to use the "local_action" or the "delegate_to" options in your playbooks.

There are sample playbooks in the samples directory.

Detailed documentation for each module can be found in the htmldoc directory.

Documentation regarding the Netscaler appliance configuration in general can be found at the following link, http://docs.citrix.com/en-us/netscaler/11-1.html


## Directory structure

* ansible-modules. Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* tests. Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* samples. Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* htmldoc. Contains the html documentation for each module.

* utils. Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* documentation_fragments. Contains the netscaler specific documentation files for ansible.

* run_tests.py. Top level script to run all the tests.
