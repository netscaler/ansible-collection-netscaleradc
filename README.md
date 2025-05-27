# NetScaler ADC Collection

## Description

The collection provides Ansible modules to configure and manage NetScaler ADC appliances. The modules are written using the [NITRO API](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release.html). The modules are idempotent and can be used to configure the NetScaler ADC appliances in a declarative manner.


## Requirements

### Ansible version compatibility

Tested with Ansible Core >=2.15 versions.

### Python version compatibility

Tested with Python >=3.11

## Installation

### via Ansible-galaxy

The netscaler.adc collection can be installed with the Ansible Galaxy command-line tool:

```bash
ansible-galaxy collection install netscaler.adc
```

### via Github (to have the latest updated which are yet to be released in ansible-galaxy)

```bash
ansible-galaxy collection install "git+https://github.com/netscaler/ansible-collection-netscaleradc.git" [--force]
```

 > `--force` option is required if you have already installed the collection via ansible-galaxy. This will overwrite the existing collection with the latest collection from github.

To verify the installation, run the following command:

```bash
ansible-galaxy collection list netscaler.adc
```

The above command should display the below output:

```text

# /Users/netscaleruser/.ansible/collections/ansible_collections
Collection    Version
------------- -------
netscaler.adc 2.8.x
```
## Usecases

The modules can be called by their Fully Qualified Collection Name (FQCN) such as `netscaler.adc.lbvserver`, or by their short name `netscaler.adc` if the collection is listed under the playbook's `collections` attribute:

### Usecase by FQCN

```yaml
---
- name: Sample lbvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lbvserver
      delegate_to: localhost
      netscaler.adc.lbvserver:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        nitro_protocol: "{{ nitro_protocol }}"
        validate_certs: false
        save_config: false
        state: present
        name: lb_dns_01
        servicetype: HTTP
```

### Usecase by declaring collection

```yaml
---
- name: Sample lbvserver playbook
  hosts: demo_netscalers
  gather_facts: false
  collections:
      - netscaler.adc
  tasks:
    - name: Configure lbvserver
      delegate_to: localhost
      lbvserver:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        nitro_protocol: "{{ nitro_protocol }}"
        validate_certs: false
        save_config: false
        name: lb_dns_01
        servicetype: HTTP

```

### Usecase by `netscaler.adc.module_default` group

```yaml
---
- name: Sample Playbook to use module_defaults to specify common arguments
  hosts: localhost
  gather_facts: false
  module_defaults:
    group/netscaler.adc.default_args:
      nsip: 10.10.10.10
      nitro_user: nsroot
      nitro_pass: verysecretpassword
      nitro_protocol: http
      validate_certs: false
      save_config: false
  tasks:
    - name: Sample Task | ipset
      delegate_to: localhost
      netscaler.adc.lbvserver:
        name: lb_dns_01
        servicetype: HTTP
```
### NetScaler Console (ADM) as a Proxy Server

The collection supports configuring NetScaler Console as a proxy server. This is useful when you have multiple NetScaler ADC appliances and you want to manage them using a single NetScaler Console.

An example can be found in [examples/netscaler_console_as_proxy_server.yaml](https://github.com/netscaler/ansible-collection-netscaleradc/blob/main/examples/netscaler_console_as_proxy_server.yaml).

Refer to the [NetScaler ADM as an API proxy server](https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software/current-release/adm-as-api-proxy-server.html) for more details.

### Examples and playbook anatomy
Refer to the [sample_playboook](https://github.com/netscaler/ansible-collection-netscaleradc/tree/main/examples) and [playbook_anatomy.md](https://github.com/netscaler/ansible-collection-netscaleradc/blob/main/playbook_anatomy.md). 


### SSH_connections 

Refer to [SSH_connections examples](https://github.com/netscaler/ansible-collection-netscaleradc/tree/main/examples/ssh_connections) to know how `ansible.builtins.` plugins can be used to configure the NetScaler ADC. 

### Authentication

#### Authenticate to NetScaler via username and password

Every module in the collection requires the user to authenticate to the NetScaler ADC appliance. To authenticate, provide the `nsip`, `nitro_user` and `nitro_pass` parameters directly or set them using environment variables `NETSCALER_NSIP`, `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`.

Refer to the [playbook_anatomy.md](https://github.com/netscaler/ansible-collection-netscaleradc/blob/main/playbook_anatomy.md) and [sessionid_based_authentication_via_login_logout.yaml](https://github.com/netscaler/ansible-collection-netscaleradc/blob/main/examples/sessionid_based_authentication_via_login_logout.yaml) example playbook.

> `login` module requires `username` and `password` parameters to be passed. If you do not wish to pass the username and password, refer below.

You can use the below `curl` command to generate the token. The token can be passed to other modules using the `nitro_auth_token` parameter. The `nitro_auth_token` parameter can also be passed as environment variable `NETSCALER_NITRO_AUTH_TOKEN`. The token is valid for 60 minutes.

The below command also uses `jq` to parse the JSON output and store the `sessionid` in the `NETSCALER_NITRO_AUTH_TOKEN` environment variable, so that it can be used by other modules.

> Note: Change the `NETSCALER_NSIP`, `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`. Install `jq` util if not already installed.

```bash
export NETSCALER_NITRO_AUTH_TOKEN=$(curl -X POST -H "Content-Type:application/json" --insecure --silent https://NETSCALER_NSIP/nitro/v1/config/login -d '{"login":{"username":"NETSCALER_NITRO_USER", "password":"NETSCALER_NITRO_PASS"}}' | jq .sessionid)
echo $echo $NETSCALER_NITRO_AUTH_TOKEN
```

### Invocation

The credentials of the netscaler can be provided either in the playbook by hardcoding or defining in a inventory.ini file.

#### Execution command when hosts are declared in playbook:

```bash
ansible-playbook playbook.yaml [--verbose]
```

#### Execution command hosts are declared in an inventory file:

```bash
ansible-playbook playbook.yaml -i inventory.ini [--verbose]
```

## Testing

The collection is tested using Github Actions. To know more about testing, please refer the [link]([https://github.com/netscaler/ansible-collection-netscaleradc/.github/workflow) to know more.

## Contributing

For external contributions, refer the [guidelines](https://github.com/netscaler/ansible-collection-netscaleradc/blob/c8c77cb4cb3905af8b90992bc55519f9a513ed08/CONTRIBUTING.md#L4).

## Support

For issues : https://github.com/netscaler/ansible-collection-netscaleradc/issues

For discussions or feature requests: https://github.com/netscaler/ansible-collection-netscaleradc/discussions

## Release Notes

Please refer to the [link](https://github.com/netscaler/ansible-collection-netscaleradc/blob/0438f3253b2eca084760984b6564a0a7964a128d/CHANGELOG.md) for the release notes.


## License Information

The collection uses MIT license. You can refer the [link](https://github.com/netscaler/ansible-collection-netscaleradc/blob/0438f3253b2eca084760984b6564a0a7964a128d/LICENSE) to view license information.
