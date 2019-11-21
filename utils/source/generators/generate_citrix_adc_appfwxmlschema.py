import os
import copy
import json
import yaml
from jinja2 import Environment, FileSystemLoader

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

    template = env.get_template('citrix_adc_appfwxmlschema.template')
    stream = template.stream(**kwargs)

    #output_file = 'citrix_adc_appfw_profile.py'
    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adc_appfw_xmlschema.py')
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
    json_dir = os.path.join(HERE, options['nitro_api_defines'])
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')

    main_json_file = os.path.join(json_dir, 'appfwxmlschema.json')
    with open(main_json_file, 'r') as fh:
        main_object_attributes = json.load(fh)

    main_object_doc_list = calculate_doc_list(main_object_attributes)
    # Remove state attribute documentation
    # In its place the disabled attribute is included in the template
    main_object_doc_list = [item for item in main_object_doc_list if item['option_name'] != 'state']
    print('main_object_doc_list %s' % json.dumps(main_object_doc_list, indent=4))

    attributes_config_list = []
    attributes_config_list.append(
        calculate_attributes_config_dict('appfwxmlschema', main_object_attributes)
    )

    print('attributes_config_list: %s' % json.dumps(attributes_config_list, indent=4))

    # Populate the template
    populate_template(
        template_dir,
        main_object_doc_list=main_object_doc_list,
        main_nitro_class='appfwxmlschema',
        main_object_put_id='name',
        attributes_config_list=attributes_config_list,
    )



if __name__ == '__main__':
    main()
