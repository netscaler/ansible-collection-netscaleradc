# Citrix NetScaler Ansible modules

This repository provides [Ansible](https://www.ansible.com)  modules for configuring [Citrix NetScaler](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix NetScaler are supported.

The code here should be considered alpha quality and may be broken at times due to experiments and refactoring. Tagged releases should be stable. The most stable version will be availble with Ansible automatically.


Currently the following modules are implemented

* netscaler\_cs\_action. Configure content switching actions.
* netscaler\_cs\_policy. Configure content switching policies
* netscaler\_cs\_vserver. Configure content swtiching virtual servers.
* netscaler\_lb\_monitor. Configure load balancing monitors.
* netscaler\_lb\_vserver. Configure load balancing virtual servers.
* netscaler\_server. Configure server instances.
* netscaler\_service. Configure NetScaler services.
* netscaler\_servicegroup. Configure NetScaler service groups.
* netscaler\_ssl\_cert\_key. Configure NetScaler ssl certs


## Pre-requisites

* NITRO Python SDK (available from https://www.citrix.com/downloads/netscaler-adc/sdks/netscaler-sdk-release-110.html)
* Ansible       
* Python 2.7 or 3.x

## Installation

There is an install script in the top level directory ```install.py```.

It tries to find the ansible installation directory and then copies the module files to the appropriate places.

If the ansible installation is on a dirctory that requires root access, the install script should be run with root priviledges.

If the isntallation script fails and you know where ansible is located on your system you can do a manual installation.
Just copy the contents of the ansible-modules directory to the extras module directory and the netscaler.py file to the module_utils directory of ansible.

The modules depend on the NITRO Python SDK. You can download it for the 11.0 version of Citrix NetScaler from the following link. https://www.citrix.com/downloads/netscaler-adc/sdks/netscaler-sdk-release-110.html

Alternatively you can use the ```install_nitro_sdk.py``` script

Use of a python virtualenv during installation is recommended.

If using a python virtualenv you can install all dependencies by running ```pip install -r requirements.test.txt``` from the project checkout.


## Usage

All modules are intended to be run on the ansible control machine or a jumpserver with access to the Citrix NetScaler appliance.
To do this you need to use the "local_action" or the "delegate_to" options in your playbooks.

There are sample playbooks in the `samples` directory.

Detailed documentation for each module can be found in the htmldoc directory.

Documentation regarding the Citrix NetScaler appliance configuration in general can be found at the following link, http://docs.citrix.com/en-us/netscaler/11-1.html


## Directory structure

* ansible-modules. Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* tests. Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* samples. Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* htmldoc. Contains the html documentation for each module.

* utils. Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* documentation_fragments. Contains the Citrix NetScaler specific documentation files for ansible.

* run_tests.py. Top level script to run all the tests.

## LICENSE
**GPL V3**
See [LICENSE](./LICENSE)

## COPYRIGHT

**COPYRIGHT 2017 CITRIX Systems Inc**

## Contributions
Pull requests and issues are welcome. 
