#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os.path
import pprint as pp
import json
import inspect
import re
import __builtin__

type_conversions = {
    'string' : 'str',
    'integer' : 'int',
    'boolean' : 'bool',
    'object' : 'dict',
}

def produce_module_arguments_from_json_schema(json_doc, skip_attrs):
    module_arguments = list()
    for property in json_doc:
        # Skip readonly attributes
        if property['readonly'] == True:
            continue

        # Skip attributes in skip_attrs
        if property['name'] in skip_attrs:
            continue

        entry = {}

        # Convert json type to ansible module argument type declaration
        entry['type'] = property['type']

        # Add choices if applicable
        if 'choices' in property:
            entry['choices'] = property['choices']
        entry['key'] = property['name']

        # Add to ansible modules argument
        module_arguments.append(entry)

    return module_arguments

def produce_readwrite_attrs_list(json_doc):
    readonly_list = list()
    for property in json_doc:
        # Add only readonly attributes
        if property['readonly'] == False:
            readonly_list.append(property['name'])
    return readonly_list

def produce_readonly_attrs_list(json_doc):
    readonly_list = list()
    for property in json_doc:
        # Add only readonly attributes
        if property['readonly'] == True:
            readonly_list.append(property['name'])
    return readonly_list

def produce_module_argument_documentation(json_doc, config_class, skip_attrs):

    # json schema for getting the name, readonly and enum of values
    # config_class for getting the actual docstring from the config object


    options_list = []
    for property in json_doc:

        # Skip attributes in skip list
        if property['name'] in skip_attrs:
            continue

        entry = {}
        entry['option_name'] = property['name']
        entry['readonly'] = property['readonly']

        # Fallthrough
        entry['description'] = [str(line) for line in property['description_lines']]

        if 'choices' in property:
            entry['choices'] = [ str(choice) for choice in property['choices'] ]

        options_list.append(entry)


    return options_list

def main():
    here = os.path.dirname(os.path.realpath(__file__))
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(os.path.join(here, 'source', 'templates'))
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
        }
    }

    # Iterate and produce module arguments dicts
    # and argument_options documentation entries
    module_arguments = {}
    argument_options = {}
    readonly_attrs = {}
    readwrite_attrs = {}
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

    # Do the instantiation of the templates
    template_list = [
        'netscaler.py.template',
        'netscaler_service.py.template',
        'netscaler_server.py.template',
        'netscaler_lb_vserver.py.template',
        'netscaler_servicegroup.py.template',
        'netscaler_lb_monitor.py.template',
        'netscaler_cs_vserver.py.template',
        'netscaler_cs_policy.py.template',
        'netscaler_cs_action.py.template',
    ]
    for template_file in template_list:
        template = env.get_template(template_file)
        stream = template.stream(
            argument_options=argument_options,
            module_arguments=module_arguments,
            readonly_attrs=readonly_attrs,
            readwrite_attrs=readwrite_attrs,
        )
        output_file= re.sub(r'\.template$', '', template_file)
        stream.dump(
            os.path.join('output', output_file),
            encoding='utf-8'
        )




if __name__ == '__main__':
    main()
