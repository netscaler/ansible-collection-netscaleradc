# Citrix ADC & Citrix ADM Ansible modules

This repository provides [Ansible](https://www.ansible.com)  modules for configuring [Citrix NetScaler](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix NetScaler are supported.

The code here should be considered alpha quality and may be broken at times due to experiments and refactoring. Tagged releases should be stable. The most stable version will be availble with Ansible automatically.

## Module renaming

Note that as of this [commit](https://github.com/citrix/netscaler-ansible-modules/commit/b53935432646741d9af27d9617480517a28aa86d)
all modules were renamed to match the new Citrix product names.

See [here](https://www.citrix.com/about/citrix-product-guide) for reference.

All modules which previously started with the `netscaler_` prefix have been renamed to
to start with the `citrix_adc_` prefix.

All new modules will follow this convention as well.

Until these changes are integrated into the Ansible distribution the Citrix ADC
module names will differ depending on where they were installed from.

## Documentation

Documentation is hosted at [readthedocs](http://netscaler-ansible.readthedocs.io/).

Currently the following modules are implemented

* citrix\_adc\_appfw\_confidfield - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_fieldtype - Configuration for application firewall form field type resource
* citrix\_adc\_appfw\_global\_bindings - Define global bindings for AppFW
* citrix\_adc\_appfw\_htmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_jsoncontenttype - Configuration for JSON content type resource
* citrix\_adc\_appfw\_learningsettings - Configuration for learning settings resource
* citrix\_adc\_appfw\_policy - Manage Netscaler Web Application Firewall policies
* citrix\_adc\_appfw\_policylabel - Manage Netscaler Web Application Firewall policy labels
* citrix\_adc\_appfw\_profile - Manage Netscaler Web Application Firewall profiles
* citrix\_adc\_appfw\_settings - Manage Netscaler Web Application Firewall settings
* citrix\_adc\_appfw\_signatures - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_wsdl - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlcontenttype - Configuration for XML Content type resource
* citrix\_adc\_appfw\_xmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlschema - Configuration for configured confidential form fields resource
* citrix\_adc\_cs\_action - Manage content switching actions
* citrix\_adc\_cs\_policy - Manage content switching policy
* citrix\_adc\_cs\_vserver - Manage content switching vserver
* citrix\_adc\_gslb\_service - Manage gslb service entities in Netscaler
* citrix\_adc\_gslb\_site - Manage gslb site entities in Netscaler
* citrix\_adc\_gslb\_vserver - Configure gslb vserver entities in Netscaler
* citrix\_adc\_lb\_monitor - Manage load balancing monitors
* citrix\_adc\_lb\_vserver - Manage load balancing vserver configuration
* citrix\_adc\_nitro\_request - Issue Nitro API requests to a Netscaler instance
* citrix\_adc\_save\_config - Save Netscaler configuration
* citrix\_adc\_server - Manage server configuration
* citrix\_adc\_service - Manage service configuration in Netscaler
* citrix\_adc\_servicegroup - Manage service group configuration in Netscaler
* citrix\_adc\_ssl\_certkey - Manage ssl cerificate keys
* citrix\_adm\_application - Manage applications on Citrix ADM
* citrix\_adm\_dns\_domain\_entry - Manage Citrix ADM domain names
* citrix\_adm\_login - Login to a Citrix ADM instance
* citrix\_adm\_mpsgroup - Manage Citrix ADM user groups
* citrix\_adm\_mpsuser - Manage Citrix ADM users
* citrix\_adm\_ns\_facts - Retrieve facts about Citrix ADM managed instances
* citrix\_adm\_poll\_instances - Force the poll instances network function on the target Citrix ADM
* citrix\_adm\_rba\_policy - Manage Citrix ADM rba policies
* citrix\_adm\_rba\_role - Manage Citrix ADM rba roles
* citrix\_adm\_stylebook - Create or delete Citrix ADM stylebooks
* citrix\_adm\_tenant\_facts - Retrieve facts about Citrix ADM tenants



## Pre-requisites

* NITRO Python SDK (available from https://www.citrix.com/downloads/netscaler-adc or from the "Downloads" tab of the Netscaler GUI)
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
* Install NetScaler SDK (`pip install deps/nitro-python-1.0_kamet.tar.gz`)
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

In order to do that you need a NITRO Python SDK that has the MAS proxy calls capability and also follow these 2 steps.

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
