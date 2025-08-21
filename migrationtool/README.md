# NetScaler ADC Ansible Collection Migration Tool

Migrates Ansible playbooks from legacy `citrix.adc` collection to new `netscaler.adc` collection format.

## Usage

```bash
python3 convert_yaml.py -i input_playbook.yaml -o output_playbook.yaml
```

**Arguments:**
- `-i, --input`: (Required) Input YAML playbook
- `-o, --output`: (Optional) Output file (defaults to `output.yaml`)
- `-v, --verbose`: (Optional) Enable verbose output

## What it converts

1. **Legacy modules**: `citrix.adc.lbvserver` → `netscaler.adc.lbvserver`
2. **NITRO requests**: `citrix_adc_nitro_request` → specific resource modules

### Example Conversion

**Before:**
```yaml
- name: Configure LB vserver
  citrix_adc_nitro_request:
    operation: present
    resource: lbvserver
    name: my_lb_vserver
    attributes:
      servicetype: HTTP
      port: 80
```

**After:**
```yaml
- name: Configure LB vserver
  netscaler.adc.lbvserver:
    state: present
    name: my_lb_vserver
    servicetype: HTTP
    port: 80
```

## Requirements

```bash
pip install pyyaml jinja2
```

## Files

- `convert_yaml.py`: Main conversion script
- `resourcelist.py`: Module and state mappings
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
