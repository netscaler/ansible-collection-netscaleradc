import os
import copy
import json
import yaml
from jinja2 import Environment, FileSystemLoader

from helpers import calculate_transforms_for_attribute, calculate_doc_list, calculate_attributes_config_dict


HERE = os.path.abspath(os.path.dirname(__file__))

def calculate_non_updateable_attributes(attributes):
    non_updateable = []
    for attribute in attributes:
        if not attribute['is_updateable']:
            non_updateable.append(attribute['option_name'])
    return non_updateable

def populate_template(template_dir, **kwargs):
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(template_dir),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template('citrix_adc_servicegroup.template')
    stream = template.stream(**kwargs)

    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adc_servicegroup.py')
    stream.dump(
        output_file,
        encoding='utf-8'
    )


def main():
    with open(os.path.join(HERE, 'generator_options.yaml'), 'r') as fh:
        options = yaml.load(fh)

    # Find template dir
    template_dir = os.path.join(HERE, '..', 'templates', 'basic')
    if not os.path.exists(template_dir):
        raise Exception('Cannot find template dir')

    # Find nscli json data dir
    json_dir = os.path.join(HERE, options['nitro_api_defines'])
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')

    main_json_file = os.path.join(json_dir, 'servicegroup.json')
    with open(main_json_file, 'r') as fh:
        main_object_attributes = json.load(fh)

    main_object_doc_list = calculate_doc_list(main_object_attributes, skip_attributes=['newname', 'state'])

    # Revert clttimeout and srvtimeout to int
    for doc_item in main_object_doc_list:
        if doc_item['option_name'] in ('clttimeout', 'svrtimeout'):
            doc_item['type'] = 'int'

    attributes_config_list = []
    attributes_config_list.append(
        calculate_attributes_config_dict('servicegroup', main_object_attributes, skip_attributes=['newname', 'state'])
    )
    attributes_config_list[-1]['non_updateable_attributes'] = calculate_non_updateable_attributes(main_object_attributes)
    #print(attributes_config_list[0]['non_updateable_attributes'])

    # Add the bindings objects
    bindings = []

    def append_bindings(json_file, binding_dict):
        with open(json_file, 'r') as fh:
            attributes = json.load(fh)

        key = binding_dict['binding_key']
        binding_dict.update({
            'attributes_config_list': calculate_attributes_config_dict(key, attributes),
        })
        doc_list = copy.deepcopy(binding_dict['attributes_config_list']['attributes'])
        doc_list.remove(binding_dict['link_to_main']['bind_key'])
        binding_dict['doc_list'] = calculate_doc_list(attributes)
        binding_dict
        bindings.append(binding_dict)
        attributes_config_list.append(binding_dict['attributes_config_list'])


    # Process servicemembers
    json_file=os.path.join(json_dir, 'servicegroup_servicegroupmember_binding.json')
    with open(json_file, 'r') as fh:
        attributes = json.load(fh)

    servicemembers = {}
    servicemembers['doc_list'] = calculate_doc_list(attributes, skip_attributes=['servicegroupname'])
    servicemembers['attributes_config'] = calculate_attributes_config_dict('servicemembers', attributes, skip_attributes=['servicegroupname'])
    #print(json.dumps(servicemembers, indent=4))

    if 'weight' in servicemembers['attributes_config']['transforms']:
        raise Exception('Cannot override transform for weight in servicemembers')
    servicemembers['attributes_config']['transforms']['weight'] = 'lambda v: str(v)'

    # Process monitor bindings
    json_file=os.path.join(json_dir, 'servicegroup_lbmonitor_binding.json')
    with open(json_file, 'r') as fh:
        attributes = json.load(fh)

    monitor_bindings = {}
    monitor_bindings['doc_list'] = calculate_doc_list(attributes, skip_attributes=['servicegroupname'])
    monitor_bindings['attributes_config'] = calculate_attributes_config_dict('monitor_bindings', attributes, skip_attributes=['servicegroupname'])
    print(json.dumps(monitor_bindings, indent=4))

    if 'weight' in monitor_bindings['attributes_config']['transforms']:
        raise Exception('Cannot override transform for weight in monitor_bindings')
    monitor_bindings['attributes_config']['transforms']['weight'] = 'lambda v: str(v)'

    populate_template(
        template_dir,
        main_object_doc_list=main_object_doc_list,
        main_nitro_class='servicegroup',
        main_object_put_id='servicegroupname',
        attributes_config_list=attributes_config_list,
        servicemembers=servicemembers,
        monitor_bindings=monitor_bindings,
    )



if __name__ == '__main__':
    main()
