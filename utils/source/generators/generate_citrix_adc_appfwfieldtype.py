import os
import copy
import json
from jinja2 import Environment, FileSystemLoader
import yaml

from helpers import calculate_transforms_for_attribute, calculate_doc_list, calculate_attributes_config_dict


HERE = os.path.abspath(os.path.dirname(__file__))

def populate_template(template_dir, **kwargs):
    env = Environment(
        # keep python templates valid python
        block_start_string='#{%',
        loader=FileSystemLoader(template_dir),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template('citrix_adc_appfwfieldtype.template')
    stream = template.stream(**kwargs)

    #output_file = 'citrix_adc_appfw_profile.py'
    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adc_appfw_fieldtype.py')
    stream.dump(
        output_file,
        encoding='utf-8'
    )

def main():
    with open(os.path.join(HERE, 'generator_options.yaml'), 'r') as fh:
        options = yaml.load(fh)

    # Find template dir
    template_dir = os.path.join(HERE, '..', 'templates', 'appfw')
    if not os.path.exists(template_dir):
        raise Exception('Cannot find template dir')

    # Find nscli json data dir
    nitro_api_defines = 'nitro_api_defines/mana_41_28'
    json_dir = os.path.join(HERE, options['nitro_api_defines'])
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')

    main_json_file = os.path.join(json_dir, 'appfwfieldtype.json')
    with open(main_json_file, 'r') as fh:
        main_object_attributes = json.load(fh)

    main_object_doc_list = calculate_doc_list(main_object_attributes, skip_attributes=['newname'])

    attributes_config_list = []
    attributes_config_list.append(
        calculate_attributes_config_dict('appfwfieldtype', main_object_attributes, skip_attributes=['newname'])
    )

    print(json.dumps(attributes_config_list, indent=4))

    # Populate the template
    populate_template(
        template_dir,
        main_object_doc_list=main_object_doc_list,
        main_nitro_class='appfwfieldtype',
        main_object_put_id='name',
        attributes_config_list=attributes_config_list,
    )



if __name__ == '__main__':
    main()
