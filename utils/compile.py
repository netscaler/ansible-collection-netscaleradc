#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os.path
import json
import inspect
import argparse
import sys
if sys.version_info[0] == 2:
    import __builtin__
elif sys.version_info[0] == 3:
    import builtins as __builtin__

type_conversions = {
    'string': 'str',
    'integer': 'int',
    'boolean': 'bool',
    'object': 'dict',
}


def produce_module_arguments_from_json_schema(json_doc, skip_attrs):
    module_arguments = list()
    for property in json_doc:
        # Skip readonly attributes
        if property['readonly'] is True:
            continue

        # Skip attributes in skip_attrs
        if property['name'] in skip_attrs:
            continue

        key = property['name']
        entry = {}
        entry['key'] = key
        entry['transforms'] = []

        # Convert json type to ansible module argument type declaration

        entry['type'] = property['type']

        # Add choices if applicable
        if 'choices' in property:
            choice_set = frozenset([choice.lower() for choice in property['choices']])
            if choice_set == frozenset(['yes', 'no']):
                # Overwrite type to bool
                entry['type'] = 'bool'
                entry['transforms'] = ['bool_yes_no']
            elif choice_set == frozenset(['on', 'off']):
                # Overwrite type to bool
                entry['type'] = 'bool'
                entry['transforms'] = ['bool_on_off']
            elif choice_set == frozenset(['enabled', 'disabled']):
                entry['choices'] = ['enabled', 'disabled']
            else:
                entry['choices'] = property['choices']

        # Add to ansible modules argument
        module_arguments.append(entry)

    return module_arguments


def produce_readwrite_attrs_list(json_doc):
    readonly_list = list()
    for property in json_doc:
        # Add only readonly attributes
        if property['readonly'] is False:
            readonly_list.append(property['name'])
    return readonly_list


def produce_readonly_attrs_list(json_doc):
    readonly_list = list()
    for property in json_doc:
        # Add only readonly attributes
        if property['readonly'] is True:
            readonly_list.append(property['name'])
    return readonly_list


def produce_immutables_list(json_doc):
    immutables_list = []
    for property in json_doc:
        # Add only readonly attributes
        if 'mutable' in property and not property['mutable'] and not property['readonly']:
            immutables_list.append(property['name'])
    return immutables_list


def produce_module_argument_documentation(json_doc, config_class, skip_attrs):

    # json schema for getting the name, readonly and enum of values
    # config_class for getting the actual docstring from the config object
    def split_description_line(line, width=100):
        line = str(line)
        if len(line) <= width:
            # Escape double quotes
            line = line.replace('"', r'\\"')
            # Put double quotes around line to avoid yaml
            # invalid characters breaking the documentation redering
            return ''.join(['"', line, '"'])

        words = line.split()
        line_splits = []
        line = []
        for word in words:
            if len(' '.join(line)) + len(word) > width:
                line_splits.append(' '.join(line))
                line = []
            line.append(word)
        if len(line) > 0:
            line_splits.append(' '.join(line))

        return line_splits

    options_list = []
    for property in json_doc:

        # Skip attributes in skip list
        if property['name'] in skip_attrs:
            continue

        entry = {}
        entry['option_name'] = property['name']
        entry['readonly'] = property['readonly']

        # Skip readonly attributes
        if entry['readonly']:
            continue

        # Fallthrough
        # entry['description'] = [ split_description_line(line) for line in property['description_lines']]
        entry['description'] = []

        bool_choice_sets = (
            frozenset(['yes', 'no']),
            frozenset(['on', 'off']),
        )

        enabled_disabled_set = (
            frozenset(['enabled', 'disabled']),
        )

        if 'choices' in property:
            choice_set = frozenset([choice.lower() for choice in property['choices']])
            print('choice set is %s' % choice_set)
            if choice_set not in (bool_choice_sets + enabled_disabled_set):
                entry['choices'] = [str(choice) for choice in property['choices']]
            elif choice_set in enabled_disabled_set:
                entry['choices'] = list(enabled_disabled_set[0])
            elif choice_set in bool_choice_sets:
                entry['type'] = 'bool'

            # Append lines rejecting possible values lines
            for line in property['description_lines']:
                if line.startswith('Possible values'):
                    continue
                if choice_set in enabled_disabled_set:
                    lines = split_description_line(line)
                    if isinstance(lines, list):
                        lines = [line.replace('ENABLED', 'enabled') for line in lines]
                        lines = [line.replace('DISABLED', 'disabled') for line in lines]
                    else:
                        lines = lines.replace('ENABLED', 'enabled')
                        lines = lines.replace('DISABLED', 'disabled')
                    entry['description'].append(lines)
                else:
                    entry['description'].append(split_description_line(line))
        else:
            # pass all lines to description
            entry['description'] = [split_description_line(line) for line in property['description_lines']]

        options_list.append(entry)

    return options_list


def main():
    here = os.path.dirname(os.path.realpath(__file__))
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(os.path.join(here, 'source', 'templates')),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    parser = argparse.ArgumentParser(description='Produce boilerplate module from attributes json description')
    parser.add_argument('--json-data', help='Json input file', required=True)
    parser.add_argument('--nitro-section', help='Section of NITRO API to use', required=True)
    parser.add_argument('--nitro-object', help='NITRO class to use', required=True)

    args = parser.parse_args()

    # Iterate and produce module arguments dicts
    # and argument_options documentation entries
    # print('Processing %s' % key)
    # json_file = os.path.join(here, 'source/scrap', schema['json_file'])
    json_file = args.json_data
    with open(json_file, 'r') as fh:
        json_doc = json.load(fh)

    # Get properties of config_class
    nitro_module = __import__(
        'nssrc.com.citrix.netscaler.nitro.resource.config.%s.%s' % (args.nitro_section, args.nitro_object),
        globals(),
        locals(),
        [args.nitro_object],
    )

    nitro_class = getattr(nitro_module, args.nitro_object)
    sdk_property_list = []
    # for member in inspect.getmembers(schema['class']):
    for member in inspect.getmembers(nitro_class):
        # We are interested only in property instances
        if isinstance(member[1], __builtin__.property):
            sdk_property_list.append(member[0])

    # Show diffs
    scrap_properties_set = set([v['name'] for v in json_doc])
    sdk_properties_set = set(sdk_property_list)

    not_in_sdk = list(scrap_properties_set - sdk_properties_set)
    if len(not_in_sdk) > 0:
        print('Properties present in scrapped but not found in sdk object %s' % not_in_sdk)

    not_in_properties = list(sdk_properties_set - scrap_properties_set)
    if len(not_in_properties) > 0:
        print('Properties present in sdk but not in scrapped' % not_in_properties)

    # module arguments
    module_arguments = produce_module_arguments_from_json_schema(json_doc, skip_attrs=not_in_sdk)

    # readwrite attrs
    readwrite_attrs = produce_readwrite_attrs_list(json_doc)

    # options for documentation block
    argument_options = produce_module_argument_documentation(json_doc, nitro_class, skip_attrs=not_in_sdk)

    # read only attributes
    readonly_attrs = produce_readonly_attrs_list(json_doc)

    immutable_attrs = produce_immutables_list(json_doc)

    transforms = {}
    for entry in module_arguments:
        if entry['transforms'] != []:
            transform_key = entry['key']
            transforms[transform_key] = entry['transforms']

    # Do the instantiation of the templates
    template = env.get_template('generic_module.template')
    stream = template.stream(
        argument_options=argument_options,
        module_arguments=module_arguments,
        readonly_attrs=readonly_attrs,
        readwrite_attrs=readwrite_attrs,
        immutable_attrs=immutable_attrs,
        transforms=transforms,
    )
    output_file = 'netscaler_%s_%s.py' % (args.nitro_section, args.nitro_object)
    stream.dump(
        output_file,
        encoding='utf-8'
    )
    print('Wrote to file %s' % output_file)


if __name__ == '__main__':
    main()
