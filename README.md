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

## Examples

Refer to the [examples](examples) directory for the sample playbooks.

Also refer [playbook_anatomy.md](playbook_anatomy.md) for the anatomy of a playbook.

### Authenticate to NetScaler via username and password

Every module in the collection requires the user to authenticate to the NetScaler ADC appliance. The authentication can be done using the `nitro_user` and `nitro_pass` parameters. These parameters can also be passed as environment variables `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`.

Refer to the [playbook_anatomy.md](playbook_anatomy.md) and [examples](examples) directory for the sample playbooks.

### Authenticate to NetScaler via token (passwordless)

The collection also supports authentication to NetScaler ADC appliance via token. The token can be generated using the `login` module. The token can be passed to other modules using the `nitro_auth_token` parameter. The `nitro_token` parameter can also be passed as environment variable `NETSCALER_NITRO_AUTH_TOKEN`.

Refer to the [playbook_anatomy.md](playbook_anatomy.md) and [sessionid_based_authentication_via_login_logout.yaml](examples/sessionid_based_authentication_via_login_logout.yaml) example playbook.

> `login` module requres `username` and `password` parameters to be passed. If you do not wish to pass the username and password, refer below.

You can use the below `curl` command to generate the token. The token can be passed to other modules using the `nitro_auth_token` parameter. The `nitro_auth_token` parameter can also be passed as environment variable `NETSCALER_NITRO_AUTH_TOKEN`. The token is valid for 60 minutes.

The below command also uses `jq` to parse the JSON output and store the `sessionid` in the `NETSCALER_NITRO_AUTH_TOKEN` environment variable, so that it can be used by other modules.

> change the `NETSCALER_NSIP`, `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`

> Install `jq` util if not already installed.

```bash
export NETSCALER_NITRO_AUTH_TOKEN=$(curl -X POST -H "Content-Type:application/json" --insecure --silent https://NETSCALER_NSIP/nitro/v1/config/login -d '{"login":{"username":"NETSCALER_NITRO_USER", "password":"NETSCALER_NITRO_PASS"}}' | jq .sessionid)
echo $NETSCALER_NITRO_AUTH_TOKEN
```

## Supported Ansible Versions

TODO: Update the supported ansible versions. Test with ansible versions 2.9+

## Features of `netscaler.adc` collection

Refer to the [features_v2.md](features_v2.md) file for the features of the `netscaler.adc` collection.

## Migrating from `citrix.adc` collection to `netscaler.adc` collection

> Both `citrix.adc` and `netscaler.adc` can be used in the same Ansible playbook. However, it is recommended to migrate to `netscaler.adc` collection.

Refer to the [migrating_from_v1_v2.md](migrating_from_v1_v2.md) file for the migration steps.

## Supported Modules in `netscaler.adc` collection

Refer to the [supported_modules_matrix.md](supported_modules_matrix.md) file for the list of supported modules in `netscaler.adc` collection.

## Todo list for `netscaler.adc` collection

- [x] Support for `nitro_auth_token` parameter in all modules.
- [ ] Update supported matrix to have documentation links
- [ ] Test modules against all NetScaler ADC versions.
- [ ] Test modules againsts ansible versions 2.9+
- [ ] Configure GitHub Actions to automate the collection build and release process.
- [ ] Configure GitHub Actions to automate the collection documentation build and release process.
- [ ] Add more examples.
- [ ] Add appropriate license to the collection.
