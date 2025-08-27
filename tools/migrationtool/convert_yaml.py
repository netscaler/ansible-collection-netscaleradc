# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

import argparse
import yaml
from utils import (
    netscaler_login_specifics,
    play_level_keys_list,
    resource_map,
    state_map,
    task_level_keys_list,
)


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


def get_play_level_keys(play_data, verbose):
    play_level_keys = {}
    try:
        play_level_keys["name"] = play_data.get("name", "Sample converted playbook")
        if verbose:
            print(f"Getting play level details for {play_level_keys['name']} ")

        play_level_keys["hosts"] = play_data.get("hosts", "localhost")

        play_level_keys["gather_facts"] = play_data.get("gather_facts", False)

        for key in play_data:
            if key in play_level_keys_list:
                play_level_keys[key] = play_data[key]
            elif key not in ["name", "hosts", "tasks"]:
                print(f"key: {key} is invalid in {play_level_keys['name']}")
    except Exception as e:
        print(f"Error processing play data: {e}")
        return {}
    return play_level_keys


def get_task_level_keys(task_data, verbose):
    task_level_keys = {}
    try:

        task_level_keys["name"] = task_data.get("name", "Sample converted task")
        if verbose:
            print(f"Getting task level details for {task_level_keys['name']} ")

        task_level_keys["delegate_to"] = task_data.get("delegate_to", "localhost")
        for key in task_data:
            if key in task_level_keys_list:
                task_level_keys[key] = task_data[key]
            elif (
                isinstance(key, str)
                and key.split(".")[-1] not in resource_map
                and key not in ["citrix_adc_nitro_request"]
            ):
                print(f"key: {key} is invalid in {task_level_keys['name']}")
    except Exception as e:
        print(f"Error processing task data: {e}")
        return {}
    if verbose:
        print(
            f"Final task level details for {task_level_keys['name']}: {task_level_keys}"
        )
    return task_level_keys


def get_cred_attributes(plugindata, verbose):
    logincreds = {}
    if verbose:
        print("getting nitro credentials")
    try:
        for key in netscaler_login_specifics:
            if key in plugindata:
                logincreds[key] = plugindata[key]
    except Exception as e:
        print(f"Error processing login credentials: {e}")
        return {}
    return logincreds


def convert_yaml_file(input_file, output_file, template_file, verbose):

    # Convert input file (citrix.adc) to output file (citrix.adc.yaml) using template
    with open(input_file, "r") as infile:
        data = yaml.safe_load(infile)
    task_only = False
    # Handle both list and dict formats
    try:

        if isinstance(data, list):
            # If data is a list, assume it's a list of plays/tasks
            if len(data) == 1 and isinstance(data[0], dict) and "tasks" in data[0]:
                # Take the first item if it's a dictionary but not a single task
                play_data = data[0]
            else:
                # If it's a list of tasks
                task_only = True
                play_data = {"tasks": data}
        elif isinstance(data, dict):
            play_data = data
        else:
            raise ValueError(
                f"Unsupported YAML structure. Expected dict or list, got {type(data)}"
            )
        if not task_only:
            # get play level keys in case of play
            play_level_keys = get_play_level_keys(play_data, verbose)

        tasks = play_data.get("tasks", [])

    except Exception as e:
        print(f"Error processing YAML file: {e}")
        return

    if verbose:
        print("tasks:", tasks)
    new_tasks = []
    try:
        for task in tasks:
            task_level_keys = get_task_level_keys(task, verbose)
            taskname = task_level_keys.get("name", "Unnamed Task")
            if isinstance(task, dict):
                new_task = None  # Initialize to track if task was processed

                for pluginkey, pluginvalue in task.items():
                    if pluginkey in task_level_keys_list:
                        continue
                    if verbose:
                        print(f"Module: {pluginkey}, Parameters: {pluginvalue}")

                    if pluginkey.split(".")[-1] in resource_map:
                        new_resource_name = resource_map[pluginkey.split(".")[-1]]
                        if verbose:
                            print(f"Remapped {pluginkey} to {new_resource_name}")
                        new_task = {
                            **task_level_keys,
                            new_resource_name: pluginvalue,
                        }

                    elif pluginkey == "citrix_adc_nitro_request":
                        newplugin = {}
                        if verbose:
                            print(f"Processing citrix_adc_nitro_request for {taskname}")
                        operation = pluginvalue.get("operation", "present")
                        if operation == "action":
                            operation = pluginvalue.get("action", "")
                        state = state_map[operation]
                        resource = pluginvalue.get("resource", "")
                        entityname = pluginvalue.get("name", "")
                        if resource == "":
                            print(f"Resource not found for {pluginkey}, skipping")
                            continue
                        attributeslist = pluginvalue.get("attributes", {})
                        if "name" not in attributeslist:
                            attributeslist["name"] = entityname
                        login_attributes = get_cred_attributes(pluginvalue, verbose)
                        newplugin["state"] = state
                        if login_attributes != {}:
                            newplugin.update(login_attributes)

                        # Handle attributes first
                        if attributeslist != {}:
                            if verbose:
                                print(f"attribute list: {attributeslist}")
                            newplugin.update(attributeslist)
                        else:
                            newplugin["name"] = entityname

                        new_task = {
                            **task_level_keys,
                            f"netscaler.adc.{resource}": newplugin,
                        }

                    else:
                        # Keep original name if no mapping found
                        print(
                            f"No mapping found for {pluginkey}, keeping original name"
                        )
                        # TODO: what to do in these cases ?
                        # new_task = {
                        #     **task_level_keys,
                        #     pluginkey : pluginvalue,
                        # }

                # Only append if a task was successfully created
                if new_task is not None:
                    new_tasks.append(new_task)

        # Playbook struct
        if task_only:
            playbook = new_tasks
        else:
            playbook = [{**play_level_keys, "tasks": new_tasks}]

        # Write the playbook directly as YAML without template
        with open(output_file, "w") as outfile:
            outfile.write("---\n")
            yaml.dump(
                playbook,
                outfile,
                default_flow_style=False,
                sort_keys=False,
                Dumper=CustomDumper,
                indent=2,
            )

    except Exception as e:
        print(f"Error occurred during conversion: {e}")
        return
    print(f"Output written to: {output_file}")
    print("YAML conversion completed")


def main():
    parser = argparse.ArgumentParser(description="Convert YAML files for migration")
    parser.add_argument("-i", "--input", required=True, help="Input YAML file")
    parser.add_argument("-o", "--output", required=False, help="Output YAML file")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    input_file = args.input
    print(f"Input file: {input_file}")
    output_file = args.output if args.output else "output.yaml"
    template_file = "./template.j2"
    verbose = args.verbose

    print("Starting YAML conversion process...")
    convert_yaml_file(input_file, output_file, template_file, verbose)


if __name__ == "__main__":
    main()
