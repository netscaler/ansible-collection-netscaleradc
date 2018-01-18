# Development process

This document describes the practices used for developing the modules
that are not evident by the structure of the repository.

It is assumed that you have already read Ansible's module development
[guide][3].

## Development Utilities

Under the utils/ directory there exists a number of scripts and data files
that aid in the development process.

Be advised that the state of the scripts is always in flux, so this documentation page may
lag behind the actual implementation at times.

### Developing a new module

There is a lot of boilerplate code that goes into each module since the workflow
is roughly similar for configuring a resource using a singular NITRO object.

To aid with this there are some scripts under utils/ to aid with the generation of
this code.

The parts that are not covered by the boilerplate generation code is peculiarities of each
NITRO object. For example having to use a different nitro object to add/update the resource and
a different object to determine its existance and configuration parameters.

Also when adding bindings to an object there is some manual work to be done to configure
how the bindings tie in with the main object and to maintain the correct control flow of
the module. Still in this cases generating a module file for the binding may be beneficial
since some parts of the generated module can be copied to the more complex one that uses
that object combined with that module's main nitro object.

### Getting the spec of a nitro object

To get the specification of a nitro object there is a script named scrape.py.

This script scrapes the nitro reference web site for each object defined
in its arguments.

A sample invocation for lbvserver would be

	python scrape.py --nitro-url 'https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/12.0/configuration/load-balancing/lbvserver/lbvserver/'

This will output a json file containing information about the properties of the nitro object
and is used by subsequent scripts.

The operation of `scrape.py` is based on parsing the HTML DOM for each page and
may fail for some nitro objects.

### Generating the boilerplate

To generate the boilerplate the script compile.py has to be called.

It accepts command line arguments to define the json source file, the nitro configuration
section and nitro object names. These parameters are used to find the actual nitro object
and also to name the output file.

For each nitro object the json data file which was obtained
by the `scrape.py` script and the actual class of the Python NITRO SDK that corresponds
to this object are compared. The Python SDK must be importable when this script is run.

The script checks if there are differences between the attributes defined in the SDK
and the attributes from the scraped json and will output warnings for each attribute
missing. The attributes that will go into the generated code will be the ones present
in both the SDK object and the json data file.

The generated code contains the documentation for the attributes of the nitro object,
the instantiation of a ConfigProxy object for the object and the control flow statements
for the main module execution. Placeholders are marked by a single underscore "\_"
or names that start with a single underscore.

Replacing the placeholders, implementing the object bindings if there are any, and
verifying and correcting the control flow are the most common manual steps that follow.

## Patches

To have a comprehensive history of the changes made to the NetScaler
modules all development must be done through [this][1] repository.

New code should always come in the form of a pull request. Even
changes that could be applied by a simple fast forward merge should
be done with a pull request as this clearly indicates the time at
which the change was applied to the modules' code and also groups
together the commits to a cohesive series.

## Setting up ansible

The preferred way to deploy ansible for use in module testing is to
make a checkout of the core ansible [repository][2].

Then source the env-setup script to setup the ansible paths.

	source $ANSIBLE_CHEKCOUT/hacking/env-setup

This should modify the current shell environment to run ansible
directly from the checkout repository.

If the environment was setup correctly all ansible scripts should be
accessible. To quick check this fact run:

	ansible --version

## Installing the modules

It is recommended to use a python virtual environment to install
the dependencies needed to run the NetScaler modules.

To install the modules to the ansible checkout use the `install.py`
script. This will install the NetScaler modules and unit test files
to the ansible installation path.

The `install.py` script needs to run inside a shell environment that
has been setup as described in the previous section.

Also note that the `install.py` script needs to be updated in case the
ansible directory layout changes in the future.

After running the installation script the modules are copied
to correct path to be used by ansible. You can run them
by invoking playbooks that reference them.


## Unit testing

We use ansible's infrastructure to run the modules unit tests.

This means that in order to run the unit tests we have to name
and install the unit test files as ansible expects it.

The naming convention is that unit tests for `netscaler_module_foo`
are in a file named `test_netscaler_module_foo.py`. These files are
under the `test/units` path in this repository.

Installation is performed by the `install.py` script.

To run unit tests utilize the `utils/run_units.sh` bash script.
This scripts run all the unit tests for the module given as first
argument under all supported python versions.

## Integration testing

The integration tests are run as normal ansible playbooks.

There exists a top level playbook `test/integration/netscaler.yaml`
which includes all subsequent playbooks that implement the integration
tests for each module.

To run all integration tests for NetScaler run

	ansible-playbook -i inventory.txt test/integration/netscaler.yaml

To limit integration tests to a single module (e.g. netscaler\_server) run

	ansible-playbook -i inventory.txt test/integration/netscaler.yaml -e 'limit_to=netscaler_server'

To further limit integration tests to a single testcase inside a single module run

	ansible-playbook -i inventory.txt test/integration/netscaler.yaml -e 'limit_to=netscaler_server' -e 'testcase=server_ipv6'

The file inventory.txt should be an ansible inventory file which under the section `[netscaler]` should
include the target NetScaler. A sample can be found in `test/integration/inventory.txt`

## Use of tox in integration testing

We utilize tox to help with integration testing when we need to run the integration tests
under many different Netscaler versions and different python versions.

Running

	tox -l

will give you the list of environments defined.

To run all possible environments you need to have the corresponding
Netscaler deployments.

To run all the test just run

	tox

To run tests for a particular environment run

	tox -e py27-VPX-12.0

You will need to modify the `tox.ini` file with the correct
ip addresses for you particular NetScaler deployments.


## Ansbile pull request

Merging the changes made to the NetScaler ansible modules with the Ansible
repository follows the normal rules for github pull requests.

You need to fork the official ansible repository and then on a new branch
introduce your changes which you will submit back to the ansible repository
as a new pull request.

The changes submitted need not follow the same structure as when submitted to
the Netscaler modules repository. You may aggregate several Netscaler modules
pull requests to one Ansbile pull request if that is more convenient.

For the Netscaler modules we have utilized [this][4] repository as a staging
area for the Ansible pull request.

Bring the repository up to date with the current ansible devel branch and
then create a new branch on which you will add the modifications to submit to
ansible.

To run the ansible integration test hooks before submitting the changes
you can run the `utils/pr_check.sh` script. This script runs some of the
integration tests run by the official ansible repository CI. It can save you
some time since there is no wait period for the ansible CI tools to run the tests.

When the PR is submitted the ansible CI will run the full set of tests. Make sure to correct
any errors that arise since this is a requirement for the PR to proceed and
receive attention by a maintainer.

## Backport branch

We maintain a backport branch `backport_2.4` which is rebased on top of master on
every change merged.

This branch applies a patch needed to succesfully import the NetScaler module utils
for each module since there was a directory reorganization in Ansible 2.5 for the
network modules.

The purpose of this branch is to accommodate users who are restricted to using ansible 2.4
but also want the latest changes for the netscaler modules.


[1]: https://github.com/citrix/netscaler-ansible-modules
[2]: https://github.com/ansible/ansible
[3]: http://docs.ansible.com/ansible/latest/dev_guide/developing_modules.html
[4]: https://github.com/citrix/ansible
