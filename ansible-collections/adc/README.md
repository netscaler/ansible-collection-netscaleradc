# citrix.adc

This collection contains the Citrx ADC modules for ansible. It also contains playbooks plugins and roles.

## Requirements

 - ansible >= 2.9

## Installation

To install in ansible default or defined paths use:
```bash
ansible-galaxy collection install citrix.adc
```

## Example Usage


To use a module from a collection, reference the full collection namespace.

```yaml
---
- name: Configure ADC
  hosts: citrix_adc

  tasks:
    - name: Set server
      delegate_to: localhost
      citrix.adc
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"

        state: present

        name: server_1
        ipaddress: 10.80.0.1

```

Or use the collections playbook parameter to search for unquallified module names

```yaml
---
- name: Configure ADC
  hosts: citrix_adc
  collections:
    - citrix.adc

  tasks:
    - name: Set server
      delegate_to: localhost
      citrix_adc_server:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"

        state: present

        name: server_1
        ipaddress: 10.80.0.1

```

## Author Information

Citrix
[Citrix](https://www.citrix.com)
