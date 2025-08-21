import yaml
import argparse
import jinja2
from resourcelist import (
    resource_map,
    state_map
)

from collections import OrderedDict

class CustomDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)

def represent_custom_object(dumper, data):
    try:
        return dumper.represent_dict(data.__dict__)
    except AttributeError:
        raise yaml.representer.RepresenterError("cannot represent an object", data)

# Register the custom representer
CustomDumper.add_representer(object, represent_custom_object)

def get_state_attributes(plugin_key):
    logincreds ={}
    logincreds["nsip"] = plugin_key.get("nsip", None)
    logincreds["nitro_user"] = plugin_key.get("nitro_user", None)
    logincreds["nitro_pass"] = plugin_key.get("nitro_pass", None)
    logincreds["validate_certs"] = plugin_key.get("validate_certs", "no")
    logincreds["nitro_protocol"] = plugin_key.get("nitro_protocol", "http")
    
    return logincreds

def convert_yaml_file(input_file, output_file, template_file, verbose):

    # Convert input file (citrix.adc) to output file (citrix.adc.yaml) using template
    with open(input_file, 'r') as infile:
        data = yaml.safe_load(infile)
    
    # Handle both list and dict formats
    if isinstance(data, list):
        # If data is a list, assume it's a list of plays/tasks
        if len(data) > 0 and isinstance(data[0], dict):
            # Take the first item if it's a dictionary
            play_data = data[0]
        else:
            # If it's a list of tasks, wrap it in a play structure
            play_data = {"tasks": data}
    elif isinstance(data, dict):
        play_data = data
    else:
        raise ValueError(f"Unsupported YAML structure. Expected dict or list, got {type(data)}")

    hosts = play_data.get("hosts", "localhost")
    vars_data = play_data.get("vars", {})
    tasks = play_data.get("tasks", [])
    name = play_data.get("name", "sample converted playbook")
    gather_facts = play_data.get("gather_facts", False)
    if verbose:
        print("tasks:", tasks)
    new_tasks = []
    for task in tasks:
        taskname = task.get("name", "")
        delegate_to = task.get("delegate_to", "localhost")
        register = task.get("register", None)
        if isinstance(task, dict):
            for pluginkey, pluginvalue in task.items():
                # Skip non-module keys like 'name' and 'delegate_to'
                if pluginkey in ['name', 'delegate_to']:
                    continue
                if verbose:
                    print(f"Module: {pluginkey}, Parameters: {pluginvalue}")
                if pluginkey.split('.')[-1] in resource_map:
                    new_resource_name = resource_map[pluginkey.split('.')[-1]]
                    if verbose:
                        print(f"Remapped {pluginkey} to {new_resource_name}")
                    new_task = {
                        "name": taskname,
                        "delegate_to": delegate_to,
                        new_resource_name: pluginvalue,
                    }
                elif pluginkey == "citrix_adc_nitro_request":
                    newplugin = {}
                    if verbose:
                        print(f"Processing citrix_adc_nitro_request for {taskname}")
                    operation = pluginvalue.get("operation", "present")
                    if operation == "action":
                        operation = pluginkey.get("action", "")
                    state = state_map[operation]
                    resource = pluginvalue.get("resource", None)
                    entityname = pluginvalue.get("name", "")
                    if resource is None:
                        print(f"Resource not found for {pluginkey}, skipping")
                        continue
                    attributeslist = pluginvalue.get("attributes", [])
                    
                    login_attributes = get_state_attributes(pluginvalue)
                    newplugin["state"] = state
                    newplugin.update(login_attributes)
                    
                    # Handle attributes first
                    if attributeslist != []:
                        if verbose:
                            print(f'attribute list: {attributeslist}')
                        newplugin.update(attributeslist)
                    else:
                        newplugin["name"] = entityname
                    
                    new_task = {
                        "name": taskname,
                        "delegate_to": delegate_to,
                        f'netscaler.adc.{resource}': newplugin,
                    }
                    
                else:
                    # Keep original name if no mapping found
                    new_resource_name = pluginkey
                    print(f"No mapping found for {pluginkey}, keeping original name")


                new_tasks.append(new_task)
    
    # Playbook struct
    playbook = [{
        "name": name,
        "hosts": hosts,
        "gather_facts": gather_facts,
        "vars": vars_data,
        "tasks": new_tasks
    }]
    
    # Write the playbook directly as YAML without template
    with open(output_file, 'w') as outfile:
        yaml.dump(playbook, outfile, default_flow_style=False, sort_keys=False, Dumper=CustomDumper, indent=2)

    print(f"Output written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert YAML files for migration")
    parser.add_argument("-i", "--input", required=True, help="Input YAML file")
    parser.add_argument("-o", "--output", required=False, help="Output YAML file")
    parser.add_argument("-v", "--verbose", required=False, help="verbose mode")
    args = parser.parse_args()
    
    input_file = args.input
    print(f"Input file: {input_file}")
    output_file = args.output if args.output else "output.yaml"
    template_file = "./template.j2"
    verbose = args.verbose
    
    print("Starting YAML conversion process...")
    convert_yaml_file(input_file, output_file, template_file, verbose)
    print("Conversion completed successfully!")

if __name__ == "__main__":
    main()