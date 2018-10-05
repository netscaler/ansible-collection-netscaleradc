# Integration-Test-Suite Generator Tool for Citrix NetScaler Ansible Modules #
This document describes the purpose, usage and directory structure of Integration-Test Generator Tool for Citrix NetScaler Ansible Modules (Henceforth referred as "TOOL" in this document)


## Pre-requisites ##
A running setup of ansible with Netscaler is required. Please refer [README.md](https://github.com/citrix/netscaler-ansible-modules/blob/master/README.md) file for the same.

The TOOL is intended to be run on the ansible control machine with access to the Citrix NetScaler appliance.

The TOOL is present in `utils/generate_integration_tests/` directory. Please refer the below [Directory Structure](#directory-structure) to know more about the contents of this directory.


## Usage ##
	$ python generate_integration_test.py -h
	usage: generate_integration_test.py [-h]
	                                    [--test-type {netscaler_direct_calls,mas_proxied_calls}]
	                                    --module MODULE [MODULE ...]
	                                    [--dir-path DIR_PATH]
	
	Netscaler Ansible Integration Tests Generator
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --test-type {netscaler_direct_calls,mas_proxied_calls}
	                        Integration Test Type (default: netscaler_direct_calls)
	  --module MODULE [MODULE ...]
	  --dir-path DIR_PATH   Directory path to where the integration tests to be
	                        generated

Suppose the required module is `netscaler_xyz` to which the Integration-Test-Suite needs to be generated, the following steps are to be followed

1. Select the `test-type` between `netscaler_direct_calls`(default) and `mas_proxied_calls`

2. Change directory to `utils/generate_integration_tests/`

3. Run the `generate_integration_test.py` as below:
`python generate_integration_test.py --test-type netscaler_direct_calls --module netscaler_xyz`


> Note: More than one modules' integration-test-suite can be generated, by separating the module names with space after `--module` argument.


## Directory Structure ##
- `generate_integration_test.py` This is the TOOL to be run to generate Integration-Test-Suite
- `BaseIntegrationModule.py` Contains class which handles adding testbeds and operations
- `input_template.py` An example input template file which shows how a input template is to be written
- `file_operations.py` Module contains file operations
- `IntegrationTest.py` Contains class which handles creating required directory-structure and filling the default files specific to the module
- `netscaler_*.py` Modules which has Integration-Test-Suite support
- `template_yaml.py` Contains default yaml files
