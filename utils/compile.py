#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os.path
import json
import inspect
import __builtin__

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
            choice_set = frozenset([ choice.lower() for choice in property['choices']])
            if choice_set == frozenset(['yes', 'no']):
                # Overwrite type to bool
                entry['type'] = 'bool'
                entry['transforms'] = ['bool_yes_no']
            elif choice_set == frozenset(['on', 'off']):
                # Overwrite type to bool
                entry['type'] = 'bool'
                entry['transforms'] = ['bool_on_off']
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
        if 'mutable' in property and property['mutable'] == False and property['readonly'] == False:
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
        #entry['description'] = [ split_description_line(line) for line in property['description_lines']]
        entry['description'] = []

        bool_choice_sets = (
            frozenset(['yes', 'no']),
            frozenset(['on', 'off']),
        )

        if 'choices' in property:
            choice_set = frozenset([choice.lower() for choice in property['choices']])
            print('choice set is %s' % choice_set)
            if choice_set not in bool_choice_sets:
                entry['choices'] = [str(choice) for choice in property['choices']]

            # Append lines rejecting possible values lines
            for line in property['description_lines']:
                if line.startswith('Possible values'):
                    continue
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
        #trim_blocks=True,
        #lstrip_blocks=True,
    )

    # Compile the json schemata

    from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
    from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
    from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_servicegroup_binding import lbvserver_servicegroup_binding
    from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbmonitor import lbmonitor

    from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
    from nssrc.com.citrix.netscaler.nitro.resource.config.basic.server import server
    from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup import servicegroup
    from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding

    from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
    from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
    from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csaction import csaction

    from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey

    from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
    from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
    from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver

    schemata = {
        'basic_service' : {
            'json_file': 'basic_service.json',
            'class' : service,
        },
        'basic_server' : {
            'json_file': 'basic_server.json',
            'class' : server,
        },
        'basic_servicegroup': {
            'json_file' : 'basic_servicegroup.json',
            'class' : servicegroup,
        },
        'basic_servicegroup_servicegroupmember_binding': {
            'json_file' : 'basic_servicegroup_servicegroupmember_binding.json',
            'class' : servicegroup_servicegroupmember_binding,
        },
        'lb_lbvserver' : {
            'json_file': 'load-balancing_lbvserver.json',
            'class' : lbvserver,
        },
        'lb_lbvserver_service_binding' : {
            'json_file': 'load-balancing_lbvserver_service_binding.json',
            'class' : lbvserver_service_binding,
        },
        'lb_lbvserver_servicegroup_binding' : {
            'json_file': 'load-balancing_lbvserver_servicegroup_binding.json',
            'class' : lbvserver_servicegroup_binding,
        },
        'lb_monitor' : {
            'json_file': 'load-balancing_lbmonitor.json',
            'class' : lbmonitor,
        },
        'cs_vserver' : {
            'json_file': 'content-switching_csvserver.json',
            'class' : csvserver,
        },
        'cs_policy' : {
            'json_file': 'content-switching_cspolicy.json',
            'class' : cspolicy,
        },
        'cs_action' : {
            'json_file': 'content-switching_csaction.json',
            'class' : csaction,
        },
        'ssl_certkey' : {
            'json_file': 'ssl_sslcertkey.json',
            'class' : sslcertkey,
        },
        'gslb_site' : {
            'json_file': 'global-server-load-balancing_gslbsite.json',
            'class' : gslbsite,
        },
        'gslb_service' : {
            'json_file': 'global-server-load-balancing_gslbservice.json',
            'class' : gslbservice,
        },
        'gslb_vserver' : {
            'json_file': 'global-server-load-balancing_gslbvserver.json',
            'class' : gslbvserver,
        },
    }

    # Iterate and produce module arguments dicts
    # and argument_options documentation entries
    module_arguments = {}
    argument_options = {}
    readonly_attrs = {}
    readwrite_attrs = {}
    immutable_attrs = {}
    transforms = {}
    for key, schema in schemata.items():
        print('Processing %s' % key)
        json_file = os.path.join(here, 'source/scrap', schema['json_file'])
        with open(json_file, 'rb') as fh:
            json_doc = json.load(fh)

        # Get properties of config_class
        sdk_property_list = []
        for member in inspect.getmembers(schema['class']):
            # We are interested only in property instances
            if isinstance(member[1], __builtin__.property):
                sdk_property_list.append(member[0])

        # Show diffs
        scrap_properties_set = set([v['name'] for v in json_doc ])
        sdk_properties_set = set(sdk_property_list)

        not_in_sdk = list(scrap_properties_set - sdk_properties_set)
        if len(not_in_sdk) > 0:
            print('Properties present in scrapped but not found in sdk object %s' % not_in_sdk)

        not_in_properties = list(sdk_properties_set - scrap_properties_set)
        if len(not_in_properties) > 0:
            print('Properties present in sdk but not in scrapped' % not_in_sdk)

        # module arguments
        module_arguments[key] = produce_module_arguments_from_json_schema(json_doc, skip_attrs=not_in_sdk)

        # readwrite attrs
        readwrite_attrs[key] = produce_readwrite_attrs_list(json_doc)

        # options for documentation block
        argument_options[key] = produce_module_argument_documentation(json_doc, schema['class'], skip_attrs=not_in_sdk)

        # read only attributes
        readonly_attrs[key] = produce_readonly_attrs_list(json_doc)

        immutable_attrs[key] = produce_immutables_list(json_doc)

        transforms[key] = {}
        for entry in module_arguments[key]:
            if entry['transforms'] != []:
                transform_key = entry['key']
                transforms[key][transform_key] = entry['transforms']

    # Do the instantiation of the templates
    for key in schemata.keys():
        template = env.get_template('generic_module.template')
        stream = template.stream(
            argument_options=argument_options[key],
            module_arguments=module_arguments[key],
            readonly_attrs=readonly_attrs[key],
            readwrite_attrs=readwrite_attrs[key],
            immutable_attrs=immutable_attrs[key],
            transforms=transforms[key],
        )
        output_file = 'netscaler_%s.py' % key
        stream.dump(
            os.path.join('output', output_file),
            encoding='utf-8'
        )


if __name__ == '__main__':
    main()
