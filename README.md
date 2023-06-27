# NetScaler Ansible Collection `version2` - netscaler.adc

## About `version1` and `version2` of the `netscaler.adc` collection

`version1` of the collection was also called `citrix.adc` collection.

This is the `version2` of the NetScaler Ansible Collection. It is a complete rewrite of the collection. The collection is not backward compatible with the `version1` of the collection. The `version1` of the collection is available at <TBD>.

`version1` of the collection will be deprecated soon and will not be maintained further. Please migrate to `version2` of the collection.

## About the collection

The collection provides Ansible modules to configure and manage NetScaler ADC appliances. The modules are written using the NITRO API. The modules are idempotent and can be used to configure the NetScaler ADC appliances in declarative manner.

## :warning: Warning and disclaimer for `version2` of the collection

The collection is in `alpha` stage. It is not recommended to use the collection in production environment.

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

## Collection Documentation

<https://netscaler-ansible.readthedocs.io/en/v2.0.0-alpha/>
