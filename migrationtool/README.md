# NetScaler ADC Ansible Collection Migration Tool

This tool helps migrate existing Ansible playbooks from the legacy `citrix.adc` collection to the new `netscaler.adc` collection format.

## Overview

The migration tool converts YAML playbooks that use:
- Legacy `citrix.adc` modules 
- `citrix_adc_nitro_request` generic module

Into playbooks that use the new `netscaler.adc` collection modules.

## Features

- **Module Mapping**: Automatically maps legacy module names to new collection modules
- **State Conversion**: Converts NITRO request operations to appropriate state values
- **Credential Handling**: Preserves and converts authentication parameters
- **YAML Structure Preservation**: Maintains playbook structure, variables, and task organization

## Usage

### Basic Usage

```bash
python3 convert_yaml.py -i input_playbook.yaml -o output_playbook.yaml
```

### Arguments

- `-i, --input`: (Required) Path to the input YAML playbook
- `-o, --output`: (Optional) Path for the output file. Defaults to `output.yaml`

### Example

```bash
python convert_yaml.py -i legacy_playbook.yml -o migrated_playbook.yml
```

## Supported Conversions

### Legacy Module Mappings
The tool uses `resource_map` to convert legacy module names to new collection modules:
- `citrix.adc.lbvserver` → `netscaler.adc.lbvserver`
- `lbvserver` → `netscaler.adc.lbvserver`

### NITRO Request Conversion
Converts `citrix_adc_nitro_request` tasks to specific resource modules:

**Before:**
```yaml
- name: Configure LB vserver
  citrix_adc_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: present
    resource: lbvserver
    name: my_lb_vserver
    attributes:
      servicetype: HTTP
      ipv46: 10.10.10.10
      port: 80
```

**After:**
```yaml
- name: Configure LB vserver
  netscaler.adc.lbvserver:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    state: present
    name: my_lb_vserver
    servicetype: HTTP
    ipv46: 10.10.10.10
    port: 80
```

### State Mapping
- `add` → `present`
- `update` → `present`
- `delete` → `absent`
- `present` → `present`
- `absent` → `absent`
- `action` → Uses the action value from the task

## Files

- `convert_yaml.py`: Main conversion script
- `resourcelist.py`: Contains `resource_map` and `state_map` mappings
- `template.j2`: Jinja2 template (if used)

## Requirements

- Python 3.x
- PyYAML
- Jinja2

## Installation

```bash
pip install pyyaml jinja2
```

## Input Format Support

The tool supports various YAML input formats:
- Single playbook dictionary
- List of plays
- List of tasks (automatically wrapped in a play structure)

## Output

The tool generates a properly formatted YAML playbook with:
- Converted module names
- Updated authentication parameters  
- Preserved task names and structure
- Proper indentation and formatting

## Troubleshooting

### Common Issues

1. **Resource not found**: Check if the resource type exists in `resource_map`
2. **Missing name field**: Ensure the original task has a `name` parameter for NITRO requests
3. **Authentication errors**: Verify credential parameters are correctly set

### Debug Output

The tool provides console output showing:
- Module mappings being applied
- NITRO request processing details
- Tasks being converted

## Contributing

To add support for new modules:
1. Update `resource_map` in `resourcelist.py`
2. Add appropriate state mappings if needed
3. Test with sample playbooks
