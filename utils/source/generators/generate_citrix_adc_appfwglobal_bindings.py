import os
import copy
import json
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

    template = env.get_template('citrix_adc_appfwglobal_bindings.template')
    stream = template.stream(**kwargs)

    #output_file = 'citrix_adc_appfw_profile.py'
    output_file = os.path.join(HERE, '..', '..', '..', 'ansible-modules', 'citrix_adc_appfw_global_bindings.py')
    stream.dump(
        output_file,
        encoding='utf-8'
    )

def main():

    # Find template dir
    template_dir = os.path.join(HERE, '..', 'templates', 'appfw')
    if not os.path.exists(template_dir):
        raise Exception('Cannot find template dir')

    # Find nscli json data dir
    json_dir = os.path.join(HERE, '..', 'nitro_api_defines/kamet/appfw')
    if not os.path.exists(json_dir):
        raise Exception('Cannot find json dir')

    attributes_config_list = []

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
        binding_dict['doc_list'] = doc_list
        bindings.append(binding_dict)
        attributes_config_list.append(binding_dict['attributes_config_list'])

    # FIXME appfw policy bindings seem not to work on the NITRO level
    append_bindings(
        json_file=os.path.join(json_dir, 'appfwglobal_appfwpolicy_binding.json'),
        binding_dict={
            'binding_key': 'appfwpolicy_bindings',
            'binding_object': 'appfwglobal_appfwpolicy_binding',
            },
    )

    append_bindings(
        json_file=os.path.join(json_dir, 'appfwglobal_auditnslogpolicy_binding.json'),
        binding_dict={
            'binding_key': 'auditnslogpolicy_bindings',
            'binding_object': 'appfwglobal_auditnslogpolicy_binding',
            },
    )

    append_bindings(
        json_file=os.path.join(json_dir, 'appfwglobal_auditsyslogpolicy_binding.json'),
        binding_dict={
            'binding_key': 'auditsyslogpolicy_bindings',
            'binding_object': 'appfwglobal_auditsyslogpolicy_binding',
            },
    )

    print(json.dumps(attributes_config_list, indent=4))

    # Populate the template
    populate_template(
        template_dir,
        attributes_config_list=attributes_config_list,
        bindings=bindings,
    )



if __name__ == '__main__':
    main()
