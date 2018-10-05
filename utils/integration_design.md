# Design document for integration testing generation

## Aim of integration tests

Netscaler Ansible modules should be able to execute under different
versions of Netscaler software.

To ensure this is a fact we need to test each module against the
desired versions of Netscaler.

## Current status

Currently there are integration tests under `test/integration`.

These are separated into two folders one for directly executing
the modules against a Netscaler instance and one that executes the
modules through a MAS proxy.

The existing tests have all been written manually.

This is not sustainable for the future, since we aim to add more modules
and enhance existing modules.

There exists the need to have an automatic process which will parse
declarative definitions of the integration tests and produce functional
playbooks to be run against a Netscaler or a MAS proxy.

## Key features

* Use declarative statements to describe tests as terseley as possible.
* Produce the functional integration tests.
* Provide a way to run setup actions before the execution of the tests.
* Provide a way to run cleanup actions after the execution of the tests.
* Provide a way to define if idempotency and check mode should be checked on a case by case basis.
* Allow for versioning attributes of the NITRO API. (e.g. older versions of NITRO may not support some attributes)


## High level design

Conceptually we need to accumulate the configuration changes in a declarative format.

Then the functional code will be assemblem by one script or more that will produce the whole
interation test suite.

### An example

Taking as an example the `netscaler_server/tests/nitro/server.yaml` playbook that implements
a testcase for the `netscaler_server` module.

This playbook includes the playbooks in the server folder with this order.
1. setup.yaml
2. update.yaml
3. disable.yaml
4. remove.yaml

For each include there is a verification of the check mode working correctly
and also idempotency working correctly.

The essential data for this test is the series of configurations.

Ideally we would like to describe these transitions and if we need to check
idempotency and check\_mode for each.

```

states = 
[
  {
    'task_name': 'Setup basic server',
    'state': 'present',
    'name': 'test-server-1',
    'ipaddress': '10.10.10.10',
    'comment': 'comment for server',
    'VERIFY_CHECK_MODE': True,
    'VERIFY_IDEMPOTENCY': True,
  },

  {
    'task_name': 'Update basic server',
    'state': 'present',
    'name': 'test-server-1',
    'ipaddress': '11.11.11.11',
    'VERIFY_CHECK_MODE': True,
    'VERIFY_IDEMPOTENCY': True,
  },
  {
    'task_name': 'Disable basic server',
    'state': 'present',
    'name': 'test-server-1',
    'ipaddress': '11.11.11.11',
    'disabled': 'yes',
    'graceful': 'yes',
    'delay': '20',
    'VERIFY_CHECK_MODE': True,
    'VERIFY_IDEMPOTENCY': True,
  },
  {
    'task_name': 'Remove basic server',
    'state': 'absent'
    'name': 'test-server-1'
    'ipaddress': '10.10.10.10'
    'VERIFY_CHECK_MODE': True,
    'VERIFY_IDEMPOTENCY': True,
  }
]
```
This datastructure captures the state transitions and
verifications we need to do.

Then procedural code should construct the actual integration tests
that will look like what is actually already written.

Additionally we will need to define a datastructure that will
remove or append attributes according to the target Netscaler version.
