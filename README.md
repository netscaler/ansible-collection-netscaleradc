# NetScaler Ansible Collection `version2` - netscaler.adc


> ⚠️ Note:
> The earlier `citrix.adc` ansible collection is replaced with the new `netscaler.adc` ansible collection.
> The `citrix.adc` ansible collection is backed up by a seperate branch [citrix.adc](https://github.com/netscaler/ansible-collection-netscaleradc/tree/citrix.adc)


## Vision

The vision of the `netscaler.adc` collection is to provide a complete declarative interface to configure and manage NetScaler ADC.

If you need any feature or flexibility that is not available in the collection, please raise issues/enhancement-requests/recommendations at <https://github.com/netscaler/ansible-collection-netscaleradc/issues>

> :envelope: For any immediate issues or help , reach out to us at <NetScaler-AutomationToolkit@cloud.com> !

## About `version1` and `version2` of the collection

We refer the earlier `citrix.adc` ansible collection as `version1` and the new `netscaler.adc` as `version2`.

This is the `version2` of the NetScaler Ansible Collection. It is a complete rewrite of the collection. The collection is not backward compatible with the `version1` of the collection.

`citrix.adc` collection will be deprecated soon and will not be maintained further. Please migrate to `netscaler.adc` of the collection.

## About the collection (version2)

The collection provides Ansible modules to configure and manage NetScaler ADC appliances. The modules are written using the NITRO API. The modules are idempotent and can be used to configure the NetScaler ADC appliances in declarative manner.

## Installation

### ansible-galaxy

```bash
ansible-galaxy collection install netscaler.adc
```

### via github (to have the latest updated which are yet to be released in ansible-galaxy)


```bash
git clone --single-branch https://github.com/netscaler/ansible-collection-netscaleradc.git /tmp/ansible-collection-netscaleradc && ansible-galaxy collection install /tmp/ansible-collection-netscaleradc --force
```


### Verify the installation

```bash
ansible-galaxy collection list | grep netscaler.adc
```

The above command should display the following output:

```text
netscaler.adc 2.x.x
```

## Collection Modules Documentation

<https://netscaler.github.io/ansible-collection-netscaleradc/>

> Click on the desired module name in the [supported_modules_matrix.md](supported_modules_matrix.md) file to go to the specific module documentation

## Examples

Refer to the [examples](examples) directory for the sample playbooks.

Also refer [playbook_anatomy.md](playbook_anatomy.md) for the anatomy of a playbook.

## :key: Authentication

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

This collection supports Ansible version 2.14 and above.

> Please raise issues at <https://github.com/netscaler/ansible-collection-netscaleradc/issues> if you face any issues with the collection.

## Features of `netscaler.adc` collection

Refer to the [features_v2.md](features_v2.md) file for the features of the `netscaler.adc` collection.

## Migrating from `citrix.adc` collection to `netscaler.adc` collection

> Both `citrix.adc` and `netscaler.adc` can be used in the same Ansible playbook. However, it is recommended to migrate to `netscaler.adc` collection.

Refer to the [migrating_from_v1_v2.md](migrating_from_v1_v2.md) file for the migration steps.

## Supported Modules in `netscaler.adc` collection

Refer to the [supported_modules_matrix.md](supported_modules_matrix.md) file for the list of supported modules in `netscaler.adc` collection.

## Todo list for `netscaler.adc` collection

- [x] Support for `nitro_auth_token` parameter in all modules.
- [x] Update supported matrix to have documentation links
- [x] Add appropriate license to the collection.
- [x] Upload the collection to Ansible Galaxy.
- [ ] Support configuring ADC with ADM as proxy. Refer to [NetScaler ADM as an API proxy server](https://docs.netscaler.com/en-us/citrix-application-delivery-management-software/current-release/adm-as-api-proxy-server.html) for more details.
- [ ] Implement SSH connection module
- [ ] Support for generic modules similar to `citrix.adc.nitro_request` and `citrix.adc.nitro_resource`?
- [ ] migration tool to convert `citrix.adc` playbooks (including generic `citrix.adc.nitro_request` and `citrix.adc.nitro_resource` modules) to `netscaler.adc` modules
- [ ] Add more examples
- [ ] Write a python script which converts examples/playbook.yaml to module's EXAMPLE documentation
- [ ] SSH Connection module
- [ ] Run `ansible-test` on the collection.
- [ ] Run `ansible-lint` on the collection for Python 2.7, 3.6, 3.7, 3.8 and 3.9.
- [ ] Test modules against all NetScaler ADC versions.
- [ ] Test modules againsts ansible versions 2.9+
- [ ] Configure GitHub Actions to automate the collection build and release process.
- [ ] Configure GitHub Actions to automate the collection documentation build and release process.
- [ ] Configure GitHub Actions to automate the collection testing process.
- [ ] Configure GitHub Actions to automate the collection linting process.
- [x] Collect NetScaler info (version, etc) and store it in the `facts` dictionary
