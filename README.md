# Citrix ADC & Citrix ADM Ansible modules

This repository contains [two collections](https://github.com/citrix/citrix-adc-ansible-modules/tree/master/ansible-collections) - Citrix ADC ansible modules and Citrix ADM ansible modules. 

Citrix ADC Ansible modules provides [Ansible](https://www.ansible.com) modules for configuring [Citrix ADC](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix ADC are supported.

Citrix ADM Ansible modules provides modules for configuring [Citrix ADM](https://docs.citrix.com/en-us/citrix-application-delivery-management-service/overview.html).It uses Citrix ADM APIs to configure or invoke ADM capabilities.

Learn more about Citrix ADC Automation [here](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/citrix-adc-automation.html)

> :round_pushpin:For deploying Citrix ADC in Public Cloud - AWS and Azure, check out cloud scripts in github repo [terraform-cloud-scripts](https://github.com/citrix/terraform-cloud-scripts).

> :envelope: For any immediate issues or help , reach out to us at appmodernization@citrix.com !

-----------
## Ansible Modules Documentation
* [Directory structure](#directory-structure)
* [Pre-requisites](#pre-requisites)
* [Installation](#installation)
  - [Setting up prerequisites](#setting-up-prerequisites)
  - [Installing ADC and ADM modules and plugins](#installing-adc-and-adm-modules-and-plugins)
* [List of ADC Use-cases supported](#list-of-adc-use-cases-supported)
  - [ADC modules](#adc-modules)
  - [ADM modules](#adm-modules)
  - [`citrix_adc_nitro_resource` workflows list](#citrix_adc_nitro_resource-workflows-list)
* [How to use Ansible Modules ? ](#how-to-use-ansible-modules)
  - [Secure variable storage](#secure-variable-storage)
  - [Use cases supported by ADC and ADM modules](#use-cases-supported-by-adc-and-adm-modules)
  - [NITRO API TLS](#nitro-api-tls)
  - [Citrix ADM proxied calls](#citrix-adm-proxied-calls)
  - [Citrix ADM service calls](#citrix-adm-service-calls)
* [What if there is no module for your configuration?](#what-if-there-is-no-module-for-your-configuration)
  - [Use the citrix\_adc\_nitro\_request module](#use-the-citrix_adc_nitro_request-module)
  - [Use the citrix\_adc\_nitro\_resource module.](#use-the-citrix_adc_nitro_resource-module)
  - [Use the connection plugin with the `shell` Ansible module](#use-the-connection-plugin-with-the-shell-ansible-module)
* [Using standard Ansible modules like shell, fetch using Citrix ADC connection plugin](#citrix-adc-connection-plugin)
  - [Installation](#installation)
  - [Usage](#usage-1)
  - [Security notice](#security-notice)
  - [Citrix ADC and standard Ansible modules in a single playbook](#citrix-adc-and-standard-ansible-modules-in-a-single-playbook)
* [Extended Documentation](#extended-documentation)
* [Module renaming](#module-renaming)
* [LICENSE](#license)
* [COPYRIGHT](#copyright)

## Beginners Guide to usign ADC Ansible Modules
*  Getting Started with Ansible and ADC collection installation
*  Make your first Configuration on ADC with Ansible
*  General Guidelines on creating Ansible playbooks 
*  Nitro Request - Generic Module to execute Nitro API operations via Ansible
*  Nitro Resource - Generic module to create any ADC entity using Ansible
*  Nitro Info - Generic module to emulate show commands
*  Proxy your ADC Nitro API calls via ADM 

## Beginners Guide to using ADM Ansible Modules
*  Getting Started with ADM Ansible modules
*  Creating Stylebooks with ADM Ansible modules
*  Applying ADC config via Configpacks through ADM Ansible Modules
*  Updating Config-Packs to new Stylebooks via ADM Ansible Modules

-------------

## Directory structure

* `ansible-modules.` Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* `ansible-plugins.` Contains all the ansible plugins available.

* `tests.` Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* `samples.` Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* `htmldoc.` Contains the html documentation for each module.

* `utils.` Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* `documentation_fragments.` Contains the Citrix ADC specific documentation files for ansible.

* `run_tests.py`. Top level script to run all the tests.

## Pre-requisites

* NITRO Python SDK
* Ansible
* Python 2.7 or 3.x

## Installation

### Setting up prerequisites

#### Using `virtualenv` (recommended)
Use of a python virtualenv during installation is recommended.

* Activate the virtualenv (`source bin/activate`)
* Install all dependencies by running ```pip install -r requirements.test.txt``` from the project checkout.

#### Global environment
* Install Ansible (`sudo pip install ansible`)
* Install NetScaler SDK (`pip install deps/nitro-python-1.0_kamet.tar.gz`)

### Installing ADC and ADM modules and plugins

To install the available collections from the repository directly:

```bash
# ADC modules and connection plugin
ansible-galaxy collection install git+https://github.com/citrix/citrix-adc-ansible-modules.git#/ansible-collections/adc

# ADM modules
ansible-galaxy collection install git+https://github.com/citrix/citrix-adc-ansible-modules.git#/ansible-collections/adm
```

To install the available collections from a local checkout of the repository:

```bash
# ADC modules and connection plugin
cd ansible-collections/adc
ansible-galaxy collection build 
ansible-galaxy collection install citrix-adc-<semver>.tar.gz

# ADM modules
cd ansible-collections/adm
ansible-galaxy collection build 
ansible-galaxy collection install citrix-adm-<semver>.tar.gz
```

## List of ADC Use-cases supported

Currently the following modules are implemented

### ADC modules

Included in the `citrix.adc` collection

* citrix\_adc\_appfw\_confidfield - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_fieldtype - Configuration for application firewall form field type resource
* citrix\_adc\_appfw\_global\_bindings - Define global bindings for AppFW
* citrix\_adc\_appfw\_htmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_jsoncontenttype - Configuration for JSON content type resource
* citrix\_adc\_appfw\_learningsettings - Configuration for learning settings resource
* citrix\_adc\_appfw\_policy - Manage Citrix ADC Web Application Firewall policies
* citrix\_adc\_appfw\_policylabel - Manage Citrix ADC Web Application Firewall policy labels
* citrix\_adc\_appfw\_profile - Manage Citrix ADC Web Application Firewall profiles
* citrix\_adc\_appfw\_settings - Manage Citrix ADC Web Application Firewall settings
* citrix\_adc\_appfw\_signatures - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_wsdl - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlcontenttype - Configuration for XML Content type resource
* citrix\_adc\_appfw\_xmlerrorpage - Configuration for configured confidential form fields resource
* citrix\_adc\_appfw\_xmlschema - Configuration for configured confidential form fields resource
* citrix\_adc\_cs\_action - Manage content switching actions
* citrix\_adc\_cs\_policy - Manage content switching policy
* citrix\_adc\_cs\_vserver - Manage content switching vserver
* citrix\_adc\_dnsnsrec - Configuration for name server record resource
* citrix\_adc\_gslb\_service - Manage gslb service entities in Citrix ADC
* citrix\_adc\_gslb\_site - Manage gslb site entities in Citrix ADC
* citrix\_adc\_gslb\_vserver - Configure gslb vserver entities in Citrix ADC
* citrix\_adc\_lb\_monitor - Manage load balancing monitors
* citrix\_adc\_lb\_vserver - Manage load balancing vserver configuration
* citrix\_adc\_nitro\_info - Retrieve information from various NITRO API endpoints
* citrix\_adc\_nitro\_request - Issue Nitro API requests to a Citrix ADC instance
* citrix\_adc\_nitro\_resource - Create, update, delete resources on Citrix ADC
* citrix\_adc\_password\_reset - Perform default password reset
* citrix\_adc\_save\_config - Save Citrix ADC configuration
* citrix\_adc\_server - Manage server configuration
* citrix\_adc\_service - Manage service configuration in Citrix ADC
* citrix\_adc\_servicegroup - Manage service group configuration in Citrix ADC
* citrix\_adc\_ssl\_certkey - Manage ssl certificate keys
* citrix\_adc\_sslcipher - Manage custom SSL ciphers
* citrix\_adc\_sslcipher\_sslciphersuite\_binding - Manage SSL cipher and SSL ciphersuite bindings
* citrix\_adc\_sslprofile\_sslcipher\_binding - Manage SSL profile and SSL cipher bindings
* citrix\_adc\_system\_file - Upload systemfile to ADC


### ADM modules

Included in the `citrix.adm` collection

* citrix\_adm\_application - Manage applications on Citrix ADM
* citrix\_adm\_dns\_domain\_entry - Manage Citrix ADM domain names
* citrix\_adm\_login - Login to a Citrix ADM instance
* citrix\_adm\_logout - Logout from a Citrix ADM instance
* citrix\_adm\_mpsgroup - Manage Citrix ADM user groups
* citrix\_adm\_mpsuser - Manage Citrix ADM users
* citrix\_adm\_ns\_facts - Retrieve facts about Citrix ADM managed instances
* citrix\_adm\_poll\_instances - Force the poll instances network function on the target Citrix ADM
* citrix\_adm\_rba\_policy - Manage Citrix ADM rba policies
* citrix\_adm\_rba\_role - Manage Citrix ADM rba roles
* citrix\_adm\_stylebook - Create or delete Citrix ADM stylebooks
* citrix\_adm\_tenant\_facts - Retrieve facts about Citrix ADM tenants

## `citrix_adc_nitro_resource` workflows list

The following NITRO API endpoints have their workflow dictionaries available
for use with the `citrix_adc_nitro_resource` module.

The workflows yaml file can be found [here](deps/workflows.yaml).

csvserver\_rewritepolicy\_binding, dnssoarec, lbgroup, lbgroup\_lbvserver\_binding, lbmetrictable, lbmetrictable\_metric\_binding, lbmonitor, lbmonitor\_metric\_binding, lbmonitor\_sslcertkey\_binding, lbprofile, lbroute, lbroute6, lbvserver, lbvserver\_analyticsprofile\_binding, lbvserver\_appflowpolicy\_binding, lbvserver\_appfwpolicy\_binding, lbvserver\_appqoepolicy\_binding, lbvserver\_auditnslogpolicy\_binding, lbvserver\_auditsyslogpolicy\_binding, lbvserver\_authorizationpolicy\_binding, lbvserver\_cachepolicy\_binding, lbvserver\_capolicy\_binding, lbvserver\_cmppolicy\_binding, lbvserver\_contentinspectionpolicy\_binding, lbvserver\_csvserver\_binding, lbvserver\_dnspolicy64\_binding, lbvserver\_feopolicy\_binding, lbvserver\_filterpolicy\_binding, lbvserver\_pqpolicy\_binding, lbvserver\_responderpolicy\_binding, lbvserver\_rewritepolicy\_binding, lbvserver\_scpolicy\_binding, lbvserver\_service\_binding, lbvserver\_servicegroup\_binding, lbvserver\_servicegroupmember\_binding, lbvserver\_spilloverpolicy\_binding, lbvserver\_transformpolicy\_binding, lbvserver\_videooptimizationdetectionpolicy\_binding, lbvserver\_videooptimizationpacingpolicy\_binding, nsacl, ntpparam, ntpserver, policypatset, policypatset\_pattern\_binding, rewriteaction, rewritepolicy, server, service, service\_lbmonitor\_binding, servicegroup, servicegroup\_lbmonitor\_binding, snmpmanager, spilloverpolicy, sslparameter, sslprofile, sslprofile\_sslcipher\_binding, sslvserver, sslvserver\_sslcertkey\_binding, systemuser, transformaction, transformpolicy, transformprofile


## How to use Ansible modules ?

All modules are intended to be run on the ansible control machine or a jumpserver with access to the Citrix ADC appliance.
To do this you need to use the `local_action` or the `delegate_to` options in your playbooks.

There are sample playbooks in the `samples` directory.

Detailed documentation for each module can be found in the htmldoc directory.

Documentation regarding the Citrix ADC appliance configuration in general can be found at the following link, http://docs.citrix.com/en-us/netscaler/11-1.html

### Secure variable storage

Some input variables used by the Citrix ADC ansible modules contain sensitive data.

Most notably `nitro_pass`.

Other variables may also be considered security sensitive
depending on the use case. For example a user may not want to expose backend service
IPs since it gives an attacker insight into the network topology used.

In production environments it is recommended to keep the values of these variables encrypted until they are needed by the
playbook. Ansible offers the [ansible-vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) utility which
can be used to encrypt individual variables or entire files.

When the contents are needed the `ansible-playbook` command can take arguments which will point to the encrypted content
and decrypt it as needed.

For more information see the full [documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

### NITRO API TLS

By default the `nitro_protocol` parameter is set to `http`.
This leaves all NITRO API request and response data unencrypted and it is not recommended for production environments.

Set the `nitro_protocol` to `https` in order to have all NITRO API communication encrypted.

By default the Citrix ADC comes with a self signed TLS certificate.
If you intend to use https with this certificate you need to set the `validate_certs` parameter to `false`.

For production environments it is recommended to use trusted TLS certificate so that `validate_certs`
is set to `true`.

Please consult the [Citrix ADC secure deployment guide](https://docs.citrix.com/en-us/citrix-adc/citrix-adc-secure-deployment/secure-deployment-guide.html) where among other things the usage of trusted TLS certificates is documented.

### Citrix ADM proxied calls

There is also the ability to proxy module NITRO calls through a Citrix ADM to a target ADC.

In order to do that you need a NITRO Python SDK that has the MAS proxy calls capability and also follow these 2 steps.

1. First acquire a nitro authentication token with the use of the ```netscaler_nitro_request```  ```mas_login``` operation.
2. Next all subsequent module invocations should have the ```mas_proxy_call``` option set to ```true``` , replace the ```nitro_user``` and ```nitro_pass``` authentication options with the ```nitro_auth_token``` acquired from the previous step and finally include the ```instance_ip``` option to instruct MAS to which citrix ADC to proxy the calls.

A  sample playbook is provided in the samples directory. [mas_proxied_server.yaml](https://github.com/citrix/citrix-adc-ansible-modules/blob/master/samples/mas_proxied_server.yaml)

There is also the option to use the ADM service as a NITRO API proxy.

To do that you first need to get a bearer token using the ```citrix_adc_get_bearer_token``` module.

After that you need to include the following options with the module invocation:

1. `nitro_protocol`
2. `nsip`
3. `api_path`
4. `is_cloud`
5. `bearer_token`
6. `mas_proxy_call`

And one of:

1. `instance_ip`
2. `instance_id`
3. `instance_name`

You can find examples in this [folder](samples/adm_service_proxy).

### Citrix ADM service calls

There is the option for citrix_adm modules to be executed targetting the ADM service instead of an on prem ADM.

This mode of execution relies on first getting a `nitro_auth_token` by logging in the ADM service and using this
token for all subsequent module calls.

Also the option `is_cloud: true` must be set as well as having the `adm_ip: adm.cloud.com`.

Examples can be found in this [folder](samples/citrix_adm).

## What if there is no module for your configuration?

When there is no module that covers the ADC configuration you want to apply there are
a few options that will allow you to still apply the configuration through an ansible playbook.

### Use the citrix\_adc\_nitro\_request module.

This a module that is a thin wrapper around the NITRO REST API.
It provides a number of operations which it then translates into HTTP requests
and provides the resulting NITRO API response in a well defined return value.

You can find examples of using the module in this [folder](samples/nitro_request)

### Use the citrix\_adc\_nitro\_resource module.

The `citrix_adc_nitro_resource` module can be used to create, update and delete
NITRO objects.

It has the same base parameters as the other modules for connecting to the ADC.

Its most important attributes are the `workflow` parameter which determines
the execution of the module with respect to how the NITRO object will be created, updated
or deleted and the `resource` parameter which contains the actual attributes
for the NITRO resource.

The workflows dictionaries published so far can be found [here](deps/workflows.yaml).

Examples can be found in this [folder](samples/nitro_resource).

Extended documentation can be found [here](https://netscaler-ansible.readthedocs.io/en/latest/generic_modules/nitro_resource.html).

If an endpoint cannot be found in the existing workflows file please open an issue
so that we can investigate if this endpoint is covered by the existing workflows and publish its dictionary.


### Use the connection plugin with the `shell` Ansible module

As a last resort the user can user the `shell` Ansible module
along with the Citrix ADC connection plugin to issue `nscli` commands
to the target ADC.

This provides the least feedback but it is useful for one off
configuration steps or when nothing else is applicable.

> This requires password-less (SSH-key based) authentication. Follow [this article](https://docs.citrix.com/en-us/citrix-adc/current-release/system/authentication-and-authorization-for-system-user/ssh-key-based-authentication-for-system-users.html) to setup the ADC

Examples can be found in this [folder](samples/citrix_adc_connection_plugin)


## Citrix ADC connection plugin

The Citrix ADC connection plugin allows the use of standard Ansible modules, such as `shell` and `fetch`, with Citrix ADC.

### Installation

The connection plugin is included in the citrix.adc collection.

### Usage

In order for a standard Ansible module to work properly with the Citrix ADC connection plugin the following conditions must hold true.

* Modify the playbook so that it uses the connection plugin (`connection: ssh_citrix_adc`).
* Citrix ADC does not have the python interpreter path defined, so one should pass this path when defining the host group (`ansible_python_interpreter: /var/python/bin/python`).
* The plugin works only with ssh key based authentication. The remote Citrix ADC must have the public ssh key of the controlling machine in their authorized_keys file (`/flash/nsconfig/ssh/authorized_keys`).
* In the local [ansible.cfg](https://docs.ansible.com/ansible/latest/reference_appendices/config.html) file make sure the following lines exist:
```
[defaults]
host_key_checking = False

[ssh_connection]
scp_if_ssh = True
```


You can find usage samples in this [folder](samples/citrix_adc_connection_plugin).

### Security notice

With the connection plugin and the `shell` ansible module it is posssible to run nscli commands
as show in the example below.

```yaml
tasks:
  - name: Run nscli command
    shell: "nscli -s -U :nsroot:{{nitro_pass}} show ns ip"
    no_log: True
```

In order to not expose the actual nsroot password the following rules must be observed

* Do not hardcode the password in the command string.

  Use a variable which is retrieved from a secure storage.

* For the task that contains the password set the task option `no_log: True`

  This will hide log output from the specified task including the password.

### Citrix ADC and standard Ansible modules in a single playbook

There are some conflicting configuration options when using a standard Ansible module with a Citrix ADC specific module in the same playbook.

To have such a playbook execute correctly the following solutions are proposed.

* Have a single playbook with multiple plays ( [sample](samples/citrix_adc_connection_plugin/multiple_plays.yaml) ).
* Have a single play configured for standard Ansible modules and define the neeeded overrides in the Citrix ADC specific tasks ( [sample](samples/citrix_adc_connection_plugin/override_citrix_adc_tasks.yaml) ).
* Have a single play configured for Citrix ADC specific modules and define the needed overrides for the generic Ansible tasks ( [sample](samples/citrix_adc_connection_plugin/override_generic_tasks.yaml) ).

## Module renaming

Note that as of this [commit](https://github.com/citrix/netscaler-ansible-modules/commit/b53935432646741d9af27d9617480517a28aa86d)
all modules were renamed to match the new Citrix product names.

See [here](https://www.citrix.com/about/citrix-product-guide) for reference.

All modules which previously started with the `netscaler_` prefix have been renamed to
to start with the `citrix_adc_` prefix.

All new modules will follow this convention as well.

Until these changes are integrated into the Ansible distribution the Citrix ADC
module names will differ depending on where they were installed from.

## Extended Documentation

Extended documentation is hosted at [readthedocs](http://netscaler-ansible.readthedocs.io/).

## LICENSE
**MIT License**
See [LICENSE](./LICENSE)

## COPYRIGHT

**COPYRIGHT 2017 CITRIX Systems Inc**

## Contributions
3rd party contributions are not accepted as of today. You can reach out to us at appmodernization@citrix.com ! for quick response or create GitHub issues.
