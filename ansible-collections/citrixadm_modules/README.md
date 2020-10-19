# citrix.citrixadm_modules

This collection contains the Citrx ADM modules for ansible. It also contains playbooks.

## Requirements

 - ansible >= 2.9

## Installation

To install in ansible default or defined paths use:
```bash
ansible-galaxy collection install citrix.citrixadm_modules
```

## Example Usage


To use a module from a collection, reference the full collection namespace.

```yaml
---
- name: Login to Citrix ADM
  hosts: citrix_adm

  tasks:
    - name: Login to adm
      delegate_to: localhost
      citrix.citrixadm_modules.citrix_adm_login:
        mas_ip: "{{ mas_ip }}"
        mas_user: "{{ mas_user }}"
        mas_pass: "{{ mas_pass }}"

```

Or use the collections playbook parameter to search for unquallified module names

```yaml
---
- name: Configure ADC
  hosts: citrix_adc
  collections:
    - citrix.citrixadm_modules

  tasks:
    - name: Login to adm
      delegate_to: localhost
      citrix_adm_login:
        mas_ip: "{{ mas_ip }}"
        mas_user: "{{ mas_user }}"
        mas_pass: "{{ mas_pass }}"

```

## Author Information

Citrix
[Citrix](https://www.citrix.com)
