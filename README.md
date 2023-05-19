# Citrix ADC & Citrix ADM Ansible modules

This repository contains [two collections](https://github.com/citrix/citrix-adc-ansible-modules/tree/master/ansible-collections) - Citrix ADC ansible modules and Citrix ADM ansible modules.

Citrix ADC Ansible modules provides [Ansible](https://www.ansible.com) modules for configuring [Citrix ADC](https://www.citrix.com/products/netscaler-adc/) instances. It uses the [NITRO REST API](https://docs.citrix.com/en-us/netscaler/11/nitro-api.html). All form factors of Citrix ADC are supported.

Citrix ADM Ansible modules provides modules for configuring [Citrix ADM](https://docs.citrix.com/en-us/citrix-application-delivery-management-service/overview.html).It uses Citrix ADM APIs to configure or invoke ADM capabilities.

Learn more about Citrix ADC Automation [here](https://docs.citrix.com/en-us/citrix-adc/current-release/deploying-vpx/citrix-adc-automation.html)

> :round_pushpin: For deploying Citrix ADC in Public Cloud - AWS and Azure, check out cloud scripts in github repo [terraform-cloud-scripts](https://github.com/citrix/terraform-cloud-scripts).

> :envelope: For any immediate issues or help , reach out to us at NetScaler-AutomationToolkit@cloud.com !

-----------

# Contents
## Ansible Modules Documentation
 * [Directory structure](#directory-structure)
 * [Pre-requisites](#pre-requisites)
 * [Installation](#installation)
    * [Setting up prerequisites](#setting-up-prerequisites)
    * [Using `virtualenv` (recommended)](#using-virtualenv-recommended)
    * [Global environment](#global-environment)
    * [Installing ADC and ADM modules and plugins](#installing-adc-and-adm-modules-and-plugins)
 * [List of ADC Use-cases supported](#list-of-adc-use-cases-supported)
    * [ADC modules](#adc-modules)
    * [ADM modules](#adm-modules)
    * [`citrix_adc_nitro_resource` workflows list](#citrix_adc_nitro_resource-workflows-list)
 * [How to use Ansible modules ?](#how-to-use-ansible-modules-)
    * [Secure variable storage](#secure-variable-storage)
    * [NITRO API TLS](#nitro-api-tls)
    * [Citrix ADM proxied calls](#citrix-adm-proxied-calls)
    * [Citrix ADM service calls](#citrix-adm-service-calls)
    * [Configure CPX (docker)](#configure-cpx-via-ansible)
  * [What if there is no module for your configuration?](#what-if-there-is-no-module-for-your-configuration)
    * [Use the citrix\_adc\_nitro\_request module.](#use-the-citrix_adc_nitro_request-module)
    * [Use the citrix\_adc\_nitro\_resource module.](#use-the-citrix_adc_nitro_resource-module)
    * [Use the connection plugin with the `shell` Ansible module](#use-the-connection-plugin-with-the-shell-ansible-module)
  * [Citrix ADC connection plugin](#citrix-adc-connection-plugin)
    * [Installation](#installation-1)
    * [Usage](#usage)
    * [Security notice](#security-notice)
    * [Citrix ADC and standard Ansible modules in a single playbook](#citrix-adc-and-standard-ansible-modules-in-a-single-playbook)
  * [Module renaming](#module-renaming)
  * [Extended Documentation](#extended-documentation)
  * [LICENSE](#license)
  * [COPYRIGHT](#copyright)
  * [Contributions](#contributions)

## Beginners Guide to usign ADC Ansible Modules
* [Hands-On Lab for ADC Automation with Ansible](#hands-on-lab-for-adc-automation-with-ansible)
*  [Getting Started with Ansible and ADC collection installation](#getting-started-with-ansible-and-adc-collection-installation)
*  [Make your first Configuration on ADC with Ansible](#make-your-first-configuration-on-adc-with-ansible)
*  [General Guidelines on creating Ansible playbooks](#general-guidelines-on-creating-ansible-playbooks)
*  [Nitro Request - Generic Module to execute Nitro API operations via Ansible](#nitro-request---generic-module-to-execute-nitro-api-operations-via-ansible)
*  [Nitro Resource - Generic module to create any ADC entity using Ansible](#nitro-resource---generic-module-to-create-any-adc-entity-using-ansible)
*  [Nitro Info - Generic module to emulate show commands](#nitro-info---generic-module-to-emulate-show-commands)
*  [Proxy your ADC Nitro API calls via ADM](#proxy-your-adc-nitro-api-calls-via-adm)

## Beginners Guide to using ADM Ansible Modules

*  [Getting Started with ADM Ansible modules](#getting-started-with-adm-ansible-modules)
*  [Creating Stylebooks with ADM Ansible modules](#creating-stylebooks-with-adm-ansible-modules)
*  [Applying ADC config via Configpacks through ADM Ansible Modules](#applying-adc-config-via-configpacks-through-adm-ansible-modules)
*  [Updating Config-Packs to new Stylebooks via ADM Ansible Modules](#updating-config-packs-to-new-stylebooks-via-adm-ansible-modules)

-------------
# Ansible Modules Documentation

## Directory structure

* `ansible-modules.` Contains all the ansible modules available. These are the files that must be installed on an ansible control node in order for the functionality to be present

* `ansible-plugins.` Contains all the ansible plugins available.

* `tests.` Contains the test suite for the modules. It requires some extra dependencies than the plain modules in order to run.

* `sample_playbook.` Contains some sample playbooks that combine more than one modules together to achieve a desired configuration.
Examples of the modules' usage are also contained in the EXAMPLES section of the modules themselves.

* `htmldoc.` Contains the html documentation for each module.

* `utils.` Contains utilities mainly used for the authoring of the modules and are not relevant to the end user.

* `documentation_fragments.` Contains the Citrix ADC specific documentation files for ansible.

* `run_tests.py`. Top level script to run all the tests.

## Pre-requisites

* NITRO Python SDK
* Ansible (<=5.5.0) | ansible-core (<=2.12.9)
* Python 2.7 or 3.x

> The modules are not test for `ansible>=5.5.0` (OR `ansible-core>=2.12.9`) and may break.

## Installation

### Setting up prerequisites

#### Using `virtualenv` (recommended)
Use of a python virtualenv during installation is recommended.

* Activate the virtualenv (`source bin/activate`)
* Install all dependencies by running ```pip install -r requirements.test.txt``` from the project checkout.

#### Global environment
* Install Ansible (`sudo pip install ansible==5.5.0`)
* Install NetScaler SDK (`pip install deps/nitro-python-1.0_kamet.tar.gz`)

### Installing ADC and ADM modules and plugins

To install the available collections from the repository directly:

> Minimum `ansible` version should be *2.10* to install collections directory from the repository (https://github.com/ansible/ansible/pull/69154)

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

|**ADC Module**|**Description**|**Documentation**|**Example Playbook**|
|--|--|--|--|
| citrix_adc_appfw_confidfield                | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_confidfield_module.rst)                | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_fieldtype                  | Configuration for application firewall form field type resource | [HERE](./docs/modules/citrix_adc_appfw_fieldtype_module.rst)                  | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_global_bindings            | Define global bindings for AppFW                                | [HERE](./docs/modules/citrix_adc_appfw_global_bindings_module.rst)            | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_htmlerrorpage              | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_htmlerrorpage_module.rst)              | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_jsoncontenttype            | Configuration for JSON content type resource                    | [HERE](./docs/modules/citrix_adc_appfw_jsoncontenttype_module.rst)            | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_learningsettings           | Configuration for learning settings resource                    | [HERE](./docs/modules/citrix_adc_appfw_learningsettings_module.rst)           | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_policy                     | Manage Citrix ADC Web Application Firewall policies             | [HERE](./docs/modules/citrix_adc_appfw_policy_module.rst)                     | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_policylabel                | Manage Citrix ADC Web Application Firewall policy labels        | [HERE](./docs/modules/citrix_adc_appfw_policylabel_module.rst)                | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_profile                    | Manage Citrix ADC Web Application Firewall profiles             | [HERE](./docs/modules/citrix_adc_appfw_profile_module.rst)                    | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_settings                   | Manage Citrix ADC Web Application Firewall settings             | [HERE](./docs/modules/citrix_adc_appfw_settings_module.rst)                   | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_signatures                 | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_signatures_module.rst)                 | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_wsdl                       | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_wsdl_module.rst)                       | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_xmlcontenttype             | Configuration for XML Content type resource                     | [HERE](./docs/modules/citrix_adc_appfw_xmlcontenttype_module.rst)             | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_xmlerrorpage               | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_xmlerrorpage_module.rst)               | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_appfw_xmlschema                  | Configuration for configured confidential form fields resource  | [HERE](./docs/modules/citrix_adc_appfw_xmlschema_module.rst)                  | [HERE](./sample_playbooks/citrix_adc/appfw/) |
| citrix_adc_cs_action                        | Manage content switching actions                                | [HERE](./docs/modules/citrix_adc_cs_action_module.rst)                        | [HERE](./sample_playbooks/citrix_adc/content_switching/) |
| citrix_adc_cs_policy                        | Manage content switching policy                                 | [HERE](./docs/modules/citrix_adc_cs_policy_module.rst)                        | [HERE](./sample_playbooks/citrix_adc/content_switching/) |
| citrix_adc_cs_vserver                       | Manage content switching vserver                                | [HERE](./docs/modules/citrix_adc_cs_vserver_module.rst)                       | [HERE](./sample_playbooks/citrix_adc/content_switching/) |
| citrix_adc_dnsnsrec                         | Configuration for name server record resource                   | [HERE](./docs/modules/citrix_adc_dnsnsrec_module.rst)                         | [HERE](./sample_playbooks/citrix_adc/dns/) |
| citrix_adc_gslb_service                     | Manage gslb service entities in Citrix ADC                      | [HERE](./docs/modules/citrix_adc_gslb_service_module.rst)                     | [HERE](./sample_playbooks/citrix_adc/gslb/) |
| citrix_adc_gslb_site                        | Manage gslb site entities in Citrix ADC                         | [HERE](./docs/modules/citrix_adc_gslb_site_module.rst)                        | [HERE](./sample_playbooks/citrix_adc/gslb/) |
| citrix_adc_gslb_vserver                     | Configure gslb vserver entities in Citrix ADC                   | [HERE](./docs/modules/citrix_adc_gslb_vserver_module.rst)                     | [HERE](./sample_playbooks/citrix_adc/gslb/) |
| citrix_adc_lb_monitor                       | Manage load balancing monitors                                  | [HERE](./docs/modules/citrix_adc_lb_monitor_module.rst)                       | [HERE](./sample_playbooks/citrix_adc/load_balancing/) |
| citrix_adc_lb_vserver                       | Manage load balancing vserver configuration                     | [HERE](./docs/modules/citrix_adc_lb_vserver_module.rst)                       | [HERE](./sample_playbooks/citrix_adc/load_balancing/) |
| citrix_adc_nitro_info                       | Retrieve information from various NITRO API endpoints           | [HERE](./docs/modules/citrix_adc_nitro_info_module.rst)                       | [HERE](./sample_playbooks/citrix_adc/special_citrix_adc_modules/) |
| citrix_adc_nitro_request                    | Issue Nitro API requests to a Citrix ADC instance               | [HERE](./docs/modules/citrix_adc_nitro_request_module.rst)                    | [HERE](./sample_playbooks/citrix_adc/special_citrix_adc_modules/) |
| citrix_adc_nitro_resource                   | Create, update, delete resources on Citrix ADC                  | [HERE](./docs/modules/citrix_adc_nitro_resource_module.rst)                   | [HERE](./sample_playbooks/citrix_adc/special_citrix_adc_modules/) |
| citrix_adc_password_reset                   | Perform default password reset                                  | [HERE](./docs/modules/citrix_adc_password_reset_module.rst)                   | [HERE](./sample_playbooks/citrix_adc/password_reset/) |
| citrix_adc_save_config                      | Save Citrix ADC configuration                                   | [HERE](./docs/modules/citrix_adc_save_config_module.rst)                      | [HERE](./sample_playbooks/citrix_adc/basic/) |
| citrix_adc_server                           | Manage server configuration                                     | [HERE](./docs/modules/citrix_adc_server_module.rst)                           | [HERE](./sample_playbooks/citrix_adc/basic/) |
| citrix_adc_service                          | Manage service configuration in Citrix ADC                      | [HERE](./docs/modules/citrix_adc_service_module.rst)                          | [HERE](./sample_playbooks/citrix_adc/basic/) |
| citrix_adc_servicegroup                     | Manage service group configuration in Citrix ADC                | [HERE](./docs/modules/citrix_adc_servicegroup_module.rst)                     | [HERE](./sample_playbooks/citrix_adc/basic/) |
| citrix_adc_ssl_certkey                      | Manage ssl certificate keys                                     | [HERE](./docs/modules/citrix_adc_ssl_certkey_module.rst)                      | [HERE](./sample_playbooks/citrix_adc/ssl/) |
| citrix_adc_sslcipher                        | Manage custom SSL ciphers                                       | [HERE](./docs/modules/citrix_adc_sslcipher_module.rst)                        | [HERE](./sample_playbooks/citrix_adc/ssl/) |
| citrix_adc_sslcipher_sslciphersuite_binding | Manage SSL cipher and SSL ciphersuite bindings                  | [HERE](./docs/modules/citrix_adc_sslcipher_sslciphersuite_binding_module.rst) | [HERE](./sample_playbooks/citrix_adc/ssl/) |
| citrix_adc_sslprofile_sslcipher_binding     | Manage SSL profile and SSL cipher bindings                      | [HERE](./docs/modules/citrix_adc_sslprofile_sslcipher_binding_module.rst)     | [HERE](./sample_playbooks/citrix_adc/ssl/) |
| citrix_adc_system_file                      | upload systemfile to adc                                        | [HERE](./docs/modules/citrix_adc_system_file_module.rst)                      | [HERE](./sample_playbooks/citrix_adc/system/) |

### ADM modules

Included in the `citrix.adm` collection

|**ADM Module**|**Description**|**Documentation**|**Example Playbook**|
|--|--|--|--|
| citrix_adm_application      | Manage applications on Citrix ADM                                  | [HERE](./docs/modules/citrix_adm_application_module.rst)      | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_configpack       | Creates a configpack from a stylebook                              | TBD                                                           | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_dns_domain_entry | Manage Citrix ADM domain names                                     | [HERE](./docs/modules/citrix_adm_dns_domain_entry_module.rst) | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_login            | Login to a Citrix ADM instance                                     | [HERE](./docs/modules/citrix_adm_login_module.rst)            | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_logout           | Logout from a Citrix ADM instance                                  | [HERE](./docs/modules/citrix_adm_logout_module.rst)           | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_mpsgroup         | Manage Citrix ADM user groups                                      | [HERE](./docs/modules/citrix_adm_mpsgroup_module.rst)         | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_mpsuser          | Manage Citrix ADM users                                            | [HERE](./docs/modules/citrix_adm_mpsuser_module.rst)          | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_ns_facts         | Retrieve facts about Citrix ADM managed instances                  | [HERE](./docs/modules/citrix_adm_ns_facts_module.rst)         | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_poll_instances   | Force the poll instances network function on the target Citrix ADM | [HERE](./docs/modules/citrix_adm_poll_instances_module.rst)   | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_rba_policy       | Manage Citrix ADM rba policies                                     | [HERE](./docs/modules/citrix_adm_rba_policy_module.rst)       | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_rba_role         | Manage Citrix ADM rba roles                                        | [HERE](./docs/modules/citrix_adm_rba_role_module.rst)         | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_stylebook        | Create or delete Citrix ADM stylebooks                             | [HERE](./docs/modules/citrix_adm_stylebook_module.rst)        | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |
| citrix_adm_tenant_facts     | Retrieve facts about Citrix ADM tenants                            | [HERE](./docs/modules/citrix_adm_tenant_facts_module.rst)     | [ADM-OnPrem](./sample_playbooks/citrix_adm_onprem/) • [ADM-Service](./sample_playbooks/citrix_adm_service/) |

## `citrix_adc_nitro_resource` workflows list

The following NITRO API endpoints have their workflow dictionaries available for use with the `citrix_adc_nitro_resource` module.

> The workflows yaml file can be found [here](deps/workflows.yaml).

- authentication_epaaction
- csvserver_rewritepolicy_binding
- dnssoarec
- lbgroup
- lbgroup_lbvserver_binding
- lbmetrictable
- lbmetrictable_metric_binding
- lbmonitor
- lbmonitor_metric_binding
- lbmonitor_sslcertkey_binding
- lbprofile
- lbroute
- lbroute6
- lbvserver
- lbvserver_analyticsprofile_binding
- lbvserver_appflowpolicy_binding
- lbvserver_appfwpolicy_binding
- lbvserver_appqoepolicy_binding
- lbvserver_auditnslogpolicy_binding
- lbvserver_auditsyslogpolicy_binding
- lbvserver_authorizationpolicy_binding
- lbvserver_cachepolicy_binding
- lbvserver_capolicy_binding
- lbvserver_cmppolicy_binding
- lbvserver_contentinspectionpolicy_binding
- lbvserver_csvserver_binding
- lbvserver_dnspolicy64_binding
- lbvserver_feopolicy_binding
- lbvserver_filterpolicy_binding
- lbvserver_pqpolicy_binding
- lbvserver_responderpolicy_binding
- lbvserver_rewritepolicy_binding
- lbvserver_scpolicy_binding
- lbvserver_service_binding
- lbvserver_servicegroup_binding
- lbvserver_servicegroupmember_binding
- lbvserver_spilloverpolicy_binding
- lbvserver_transformpolicy_binding
- lbvserver_videooptimizationdetectionpolicy_binding
- lbvserver_videooptimizationpacingpolicy_binding
- nsacl
- ntpparam
- ntpserver
- policypatset
- policypatset_pattern_binding
- rewriteaction
- rewritepolicy
- server
- service
- service_lbmonitor_binding
- servicegroup
- servicegroup_lbmonitor_binding
- snmpmanager
- spilloverpolicy
- sslparameter
- sslprofile
- sslprofile_sslcipher_binding
- sslvserver
- sslvserver_sslcertkey_binding
- systemuser
- transformaction
- transformpolicy
- transformprofile


## How to use Ansible modules ?

All modules are intended to be run on the ansible control machine or a jumpserver with access to the Citrix ADC appliance.
To do this you need to use the `local_action` or the `delegate_to` options in your playbooks.

There are sample playbooks in the `sample_playbooks` directory.

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

A  sample playbook is provided in the sample_playbooks directory. [mas_proxied_server.yaml](./sample_playbooks/citrix_adm_onprem_as_proxy/mas_proxied_server.yaml)

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

You can find examples in this [folder](sample_playbooks/citrix_adm_service_as_proxy).

### Citrix ADM service calls

There is the option for citrix_adm modules to be executed targetting the ADM service instead of an on prem ADM.

This mode of execution relies on first getting a `nitro_auth_token` by logging in the ADM service and using this
token for all subsequent module calls.

Also the option `is_cloud: true` must be set as well as having the `adm_ip: adm.cloud.com`.

Examples can be found in this [folder](sample_playbooks/citrix_adm_service).

### Configure CPX via Ansible

If you are running a NetScaler CPX on the same host where you are executing the playbook:

```bash
$ docker port cpx 80
32773

$ cat inventory.txt
[netscaler]
127.0.0.1 nsip=127.0.0.1:32773 nitro_user=nsroot nitro_pass=nsroot validate_certs=no

$ cat lb_vserver.yml

      local_action:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
```

## In the playbook

```yaml
      local_action:
        nsip: 127.0.0.1:32773
        nitro_user: nsroot
        nitro_pass: nsroot
```

## What if there is no module for your configuration?

When there is no module that covers the ADC configuration you want to apply there are
a few options that will allow you to still apply the configuration through an ansible playbook.

### Use the citrix\_adc\_nitro\_request module.

This a module that is a thin wrapper around the NITRO REST API.
It provides a number of operations which it then translates into HTTP requests
and provides the resulting NITRO API response in a well defined return value.

You can find examples of using the module in this [folder](sample_playbooks/citrix_adc/special_citrix_adc_modules/nitro_request)

### Use the citrix\_adc\_nitro\_resource module.

The `citrix_adc_nitro_resource` module can be used to create, update and delete
NITRO objects.

It has the same base parameters as the other modules for connecting to the ADC.

Its most important attributes are the `workflow` parameter which determines
the execution of the module with respect to how the NITRO object will be created, updated
or deleted and the `resource` parameter which contains the actual attributes
for the NITRO resource.

The workflows dictionaries published so far can be found [here](deps/workflows.yaml).

Examples can be found in this [folder](sample_playbooks/citrix_adc/special_citrix_adc_modules/nitro_resource).

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

Examples can be found in this [folder](sample_playbooks/citrix_adc/citrix_adc_connection_plugin)


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


You can find usage sample_playbooks in this [folder](sample_playbooks/citrix_adc/citrix_adc_connection_plugin).

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

* Have a single playbook with multiple plays ( [sample_playbook](sample_playbooks/citrix_adc/citrix_adc_connection_plugin/multiple_plays.yaml) ).
* Have a single play configured for standard Ansible modules and define the neeeded overrides in the Citrix ADC specific tasks ( [sample](sample_playbooks/citrix_adc/citrix_adc_connection_plugin/override_citrix_adc_tasks.yaml) ).
* Have a single play configured for Citrix ADC specific modules and define the needed overrides for the generic Ansible tasks ( [sample](sample_playbooks/citrix_adc/citrix_adc_connection_plugin/override_generic_tasks.yaml) ).

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

## License
**MIT License**
See [LICENSE](./LICENSE)

## Copyright

**COPYRIGHT 2017 CITRIX Systems Inc**

## Contributions

3rd party contributions are not accepted as of today. You can reach out to us at **NetScaler-AutomationToolkit@cloud.com** ! for quick response or create GitHub issues.

-----

# Beginners guide to ADC Automation with Ansible

## Hands-On Lab for ADC Automation with Ansible
Try out the [lab](https://forum.developer.cloud.com/s/netscaler-labs?labId=000001069) that takes you through the ADC Automation journey with Ansible

## Getting Started with Ansible and ADC collection installation
Refer the Steps 1 and Steps 2 in the [Get Started with ADC Automation using Ansible](https://forum.developer.cloud.com/s/article/Get-Started-with-NetScaler-Automation-using-Ansible)

## Make your first Configuration on ADC with Ansible
Refer the Steps 3 and Steps 4 in the [Get Started with ADC Automation using Ansible](https://forum.developer.cloud.com/s/article/Get-Started-with-NetScaler-Automation-using-Ansible)

## General Guidelines on creating Ansible playbooks
Refer the [How to use Ansible Modules section ?](#how-to-use-ansible-modules) for usage guidelines on ADC Ansible playbooks.

To create Ansible playbooks for your specfic ADC use-cases/entities refer the [Ansible modules documenation](https://github.com/citrix/citrix-adc-ansible-modules/tree/master/docs/modules) and the [NITRO API documentation](https://developer-docs.citrix.com/projects/citrix-adc-nitro-api-reference/en/latest/configuration/configuration/) for understanding of endpoint, parameters etc.

##  Nitro Request - Generic Module to execute Nitro API operations via Ansible

**citrix_adc_nitro_request** which doesn’t target a particular endpoint instead can be used to perform NITRO API operations on various endpoints.

Learn more about its usage [here](https://forum.developer.cloud.com/s/article/Ansible-for-NetScaler-Nitro-API-operations).
You can find its example [here](./sample_playbooks/citrix_adc/special_citrix_adc_modules/nitro_request/).

##  Nitro Resource - Generic module to create any ADC entity using Ansible

**citrix_adc_nitro_resource** implements the CRUD operations in a generic manner applicable to multiple endpoints. You can use generic module citrix_adc_nitro_resource if you dont find a dedicated module for the usecase you are targeting.

Learn more about its usage [here](https://forum.developer.cloud.com/s/article/Generic-NetScaler-Ansible-module).
You can find its example [here](./sample_playbooks/citrix_adc/special_citrix_adc_modules/nitro_resource/).

##  Nitro Info - Generic module to emulate show commands

**citrix_adc_nitro_info** modules is to emulate show commands in Netscaler.It returns a list or dictionary for each endpoint it is invoked for.
You can find usage example [here](./sample_playbooks/citrix_adc/special_citrix_adc_modules/nitro_info/).


##  Proxy your ADC Nitro API calls via ADM

ADC Ansible modules invoke Nitro API calls internally to configure your ADC. You can proxy all those Nitro API calls via ADM on-prem or ADM Service.

Learn more about using ADM as API Proxy Server [here](https://docs.citrix.com/en-us/citrix-application-delivery-management-software/current-release/adm-as-api-proxy-server.html). You can find the usage example for ADM on-prem [here](./sample_playbooks/citrix_adm_onprem_as_proxy/mas_proxied_server.yaml) and ADM Service [here](./sample_playbooks/citrix_adm_service_as_proxy/)






---------
# Beginners guide to ADM Automation with Ansible

##  Getting Started with ADM Ansible modules

Here are the playbooks to get started with ADM Ansible modules:
1. [Login to ADM On-prem](./sample_playbooks/citrix_adm_onprem/citrix_adm_login.yaml)
2. [Add Netscaler instance to ADM on-prem](./sample_playbooks/citrix_adm_onprem/citrix_adm_managed_device.yaml)

For ADM Service
1. [Login to ADM Service](./sample_playbooks/citrix_adm_service/citrix_adm_service_login.yaml)


##  Creating Stylebooks with ADM Ansible modules

ADM On-Prem - [Creating Stylebook via Ansible on ADM On-Prem](./sample_playbooks/citrix_adm_onprem/citrix_adm_stylebook_admonprem.yaml)

ADM Service - [Creating Stylebook via Ansible on ADM On-Prem](./sample_playbooks/citrix_adm_service/citrix_adm_stylebook_admservice.yaml)

##  Applying ADC config via Configpacks through ADM Ansible Modules

ADM On_Prem - [Applying configs to ADC via ADM Configpacks through Ansible](./sample_playbooks/citrix_adm_onprem/citrix_adm_configpack_admonprem.yaml)

ADM Service - [Applying configs to ADC via ADM Configpacks through Ansible](./sample_playbooks/citrix_adm_service/citrix_adm_configpack_admservice.yaml)

##  Updating Config-Packs to new Stylebooks via ADM Ansible Modules

**change_stylebook** param in **citrix_adm_configpack** when set to **true** can be used to upgrade your existing config-pack to new Stylebook version.

```
change_stylebook: true # true when we need to change the stylebook associated to this configpack
old_stylebook: # old_stylebook will be considered only when change_stylebook is true
   name: basic-lb-config
   namespace: com.example.stylebooks
   version: "0.1"
```

Use the below playbooks and set **change_stylebook** as **true** :

ADM On_Prem - [Applying configs to ADC via ADM Configpacks through Ansible](./sample_playbooks/citrix_adm_onprem/citrix_adm_configpack_admonprem.yaml)

ADM Service - [Applying configs to ADC via ADM Configpacks through Ansible](./sample_playbooks/citrix_adm_service/citrix_adm_configpack_admservice.yaml)


> :envelope: For any immediate issues or help , reach out to us at NetScaler-AutomationToolkit@cloud.com !
