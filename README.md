# Citrix NetScaler Ansible modules

This repository provides [Ansible](https://www.ansible.com)  modules for configuring [Citrix NetScaler](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix NetScaler are supported.

The code here should be considered alpha quality and may be broken at times due to experiments and refactoring. Tagged releases should be stable. The most stable version will be availble with Ansible automatically.

Documentation is hosted at [readthedocs](http://netscaler-ansible.readthedocs.io/).

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
* netscaler\_gslb\_vserver. Configure GSLB vserver
* netscaler\_gslb\_service. Configure GSLB service
* netscaler\_gslb\_site. Configure GSLB sites


## Pre-requisites

* NITRO Python SDK (available from https://www.citrix.com/downloads/netscaler-adc/sdks/netscaler-sdk-release-110.html)
* Ansible       
* Python 2.7 or 3.x

## Installation

### Using `virtualenv` (recommended)
Use of a python virtualenv during installation is recommended.

* Activate the virtualenv (`source bin/activate`)
* Install all dependencies by running ```pip install -r requirements.test.txt``` from the project checkout.
* Install the netscaler modules using ```python install.py```

### Global install
* Install Ansible (`sudo pip install ansible`)
* Install NetScaler SDK (`sudo python install_nitro_sdk.py`)
* Install NetScaler modules (`sudo python install.py`). It tries to find the ansible installation directory and then copies the module files to the appropriate places.

If the ansible installation is on a dirctory that requires root access, the install script should be run with root privileges.
If the isntallation script fails and you know where ansible is located on your system you can do a manual installation.
Just copy the contents of the ansible-modules directory to the extras module directory and the netscaler.py file to the module_utils directory of ansible.

### Backport for Ansible 2.4.x

The modules are developed against the latest development version of ansible.

Some changes made by the core ansible developers caused the modules to lose backwards portability to ansible 2.4.

If you need the latest version of the modules present in this repository and are restricted to using ansible 2.4 you can use
the backport branch [backport_2.4](https://github.com/citrix/netscaler-ansible-modules/tree/backport_2.4) which
contains the fixes needed for the modules to run under ansible 2.4 while also containing the latest changes.

This branch will be kept up to date with the master branch.

## Usage

All modules are intended to be run on the ansible control machine or a jumpserver with access to the Citrix NetScaler appliance.
To do this you need to use the `local_action` or the `delegate_to` options in your playbooks.

There are sample playbooks in the `samples` directory.

Detailed documentation for each module can be found in the htmldoc directory.

Documentation regarding the Citrix NetScaler appliance configuration in general can be found at the following link, http://docs.citrix.com/en-us/netscaler/11-1.html

### MAS proxied calls

There is also the ability to proxy module NITRO calls through a MAS to a target Netscaler.

In order to do that you need to follow these 2 steps.

1. First acquire a nitro authentication token with the use of the ```netscaler_nitro_request```  ```mas_login``` operation.
2. Next all subsequent module invocations should have the ```mas_proxy_call``` option set to ```true``` , replace the ```nitro_user``` and ```nitro_pass``` authentication options with the ```nitro_auth_token``` acquired from the previous step and finally include the ```instance_ip``` option to instruct MAS to which netscaler to proxy the calls.

A  sample playbook is provided in the samples directory. [mas_proxied_server.yaml](https://github.com/citrix/netscaler-ansible-modules/blob/master/samples/mas_proxied_server.yaml)

## Directory structure

* `ansible-modules.` Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* `tests.` Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* `samples.` Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* `htmldoc.` Contains the html documentation for each module.

* `utils.` Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* `documentation_fragments.` Contains the Citrix NetScaler specific documentation files for ansible.

* `run_tests.py`. Top level script to run all the tests.

## LICENSE
**GPL V3**
See [LICENSE](./LICENSE)

## COPYRIGHT

**COPYRIGHT 2017 CITRIX Systems Inc**

## Contributions
Pull requests and issues are welcome. 
