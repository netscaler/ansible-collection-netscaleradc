# Achieve aplus-certified apps via Citrix ADC and Ansible

## Usage

### Prerequisites

Refer to our [Citrix ADC Ansible Modules Github page](https://github.com/citrix/citrix-adc-ansible-modules#pre-requisites) for prequisites.

### Steps

1. change the directory to the directory of this file
2. fill in the variables in the [inventory.txt](./inventory.txt) and [example_varfile.yaml](./example_varfile.yaml)
3. To configure the ADC, run the following command:
   1. `ansible-playbook -i inventory.txt ssl-aplus.yaml --extra-vars="@example_varfile.yaml"`

4. To remove the configuration, run the following command:
   1. `ansible-playbook -i inventory.txt ssl-aplus.yaml --extra-vars="@example_varfile.yaml" -e "state=absent"`
