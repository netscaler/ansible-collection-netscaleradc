# NetScaler Ansible Collection `version2` - netscaler.adc

## About `version1` and `version2` of the collection

We refer the earlier `citrix.adc` ansible collection as `version1` and the new `netscaler.adc` as `version2`.

This is the `version2` of the NetScaler Ansible Collection. It is a complete rewrite of the collection. The collection is not backward compatible with the `version1` of the collection.

`citrix.adc` collection will be deprecated soon and will not be maintained further. Please migrate to `netscaler.adc` of the collection.

## About the collection (version2)

The collection provides Ansible modules to configure and manage NetScaler ADC appliances. The modules are written using the NITRO API. The modules are idempotent and can be used to configure the NetScaler ADC appliances in declarative manner.

## :warning: Warning and disclaimer for `version2` (`netscaler.adc`) of the collection

The collection is in `alpha` testing stage. It is not recommended to use the collection in production environment.

Please raise issues at <https://github.com/citrix/citrix-adc-ansible-modules/issues> and help us improve the collection.

## Installation

```bash
git clone --branch v2.0.0-alpha --single-branch https://github.com/citrix/citrix-adc-ansible-modules.git /tmp/citrix-adc-ansible-modules-v2.0.0-alpha
ansible-galaxy collection install /tmp/citrix-adc-ansible-modules-v2.0.0-alpha --force
```

### Verify the installation

```bash
ansible-galaxy collection list | grep netscaler.adc
```

The above command should display the following output:

```text
netscaler.adc                 2.0.0-alpha
```

## Collection Modules Documentation

<https://netscaler-ansible.readthedocs.io/en/v2.0.0-alpha/>

## Features of `netscaler.adc` collection

Refer to the [features_v2.md](features_v2.md) file for the features of the `netscaler.adc` collection.

## Migrating from `citrix.adc` collection to `netscaler.adc` collection

> Both `citrix.adc` and `netscaler.adc` can be used in the same Ansible playbook. However, it is recommended to migrate to `netscaler.adc` collection.

Refer to the [migrating_from_v1_v2.md](migrating_from_v1_v2.md) file for the migration steps.

## Supported Modules in `netscaler.adc` collection

Refer to the [supported_modules_matrix.md](supported_modules_matrix.md) file for the list of supported modules in `netscaler.adc` collection.
