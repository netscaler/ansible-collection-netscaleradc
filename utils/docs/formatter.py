import os
import argparse
from jinja2 import Environment, FileSystemLoader
import importlib
import sys
import yaml
import json
import re

HERE = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
HEAD1_CHAR = '+'
HEAD2_CHAR = '-'
HEAD3_CHAR = '~'
INDENT = '    '

def populate_template(module_name, **kwargs):
    env = Environment(
        # keep python templates valid python
        #block_start_string='#{%',
        loader=FileSystemLoader(HERE),
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template('module.rst.j2')
    stream = template.stream(**kwargs)

    #output_file = 'citrix_adc_appfw_profile.py'
    output_file = os.path.join(args.output_dir, module_name)
    stream.dump(
        output_file,
        encoding='utf-8'
    )

def get_document_fragments():
    fragments_dir = os.path.abspath(os.path.join(HERE, '../../documentation_fragments'))
    sys.path.append(fragments_dir)
    module = importlib.import_module('netscaler')
    fragments_doc = module.ModuleDocFragment.DOCUMENTATION
    sys.path = sys.path[:-1]
    data = yaml.load(fragments_doc)
    return data['options']


def extract_module_title(module):
    data = module['documentation_data']
    title_lines = []
    title_lines.append(' - '.join([data['module'], data['short_description']]))
    title_lines.append(HEAD1_CHAR * len(title_lines[0]))
    return '\n'.join(title_lines)

def extract_module_synopsis(module):
    data = module['documentation_data']
    synopsis_lines = []
    if isinstance(data['description'], str):
        return '- %s' % data['description']
    
    # Fallthrough
    for line in data['description']:
        synopsis_lines.append('- %s' % line)
    ret_val = '\n'.join(synopsis_lines)
    return ret_val

def extract_module_requirements(module):
    data = module['documentation_data']
    requirements = data.get('requirements')
    if requirements is None:
        return None
    else:
        lines = []
        for requirement in requirements:
            lines.append('- %s' % requirement)
        return '\n'.join(lines)


def extract_module_parameters(module):
    data = module['documentation_data']
    parameters = data.get('options', {})
    docfrag = data.get('extends_documentation_fragment')
    if docfrag is not None:
        parameters.update(FRAGMENTS)

    header = '\n'.join([
    '.. list-table::',
    '%s:widths: 10 10 60' % INDENT,
    '%s:header-rows: 1\n' % INDENT,
    '%s* - Parameter' % INDENT,
    '%s  - Choices/Defaults' % INDENT,
    '%s  - Comment' % INDENT,
    ])

    rows = []
    for key in sorted(parameters.keys()):
        rows.append(process_parameter_row(parameters, key, module))

    return ''.join([header, '\n', ''.join(rows)])

def process_parameter_row(parameters, key, module):
    parameter_cell = generate_parameter_cell(parameters, key, module)
    choices_cell = generate_choices_cell(parameters, key, module)
    comment_cell = generate_comment_cell(parameters, key, module)

    return ''.join([
        parameter_cell,
        choices_cell,
        comment_cell,
    ])


def generate_parameter_cell(parameters, key, module, indlvl=1):
    #print('parameters %s' % json.dumps(parameters, indent=4))

    data = module['documentation_data']
    module_version_added = data['version_added']

    key = key
    type = parameters[key].get('type')

    parameter_version_added = parameters[key].get('version_added')

    cell_lines = []
    cell_lines.extend([
        '%s* - %s\n' % (INDENT * indlvl, key),
    ])
    if type is not None:
        cell_lines.extend([
            '\n',
            '%s    *(%s)*\n' % (INDENT * indlvl, type), 
        ])

    if parameter_version_added is not None:
        if parameter_version_added != module_version_added:
            cell_lines.extend([
                '\n',
                '%s    *(added in %s)*\n' % (INDENT * indlvl, parameter_version_added), 
            ])


    key_cell = ''.join(cell_lines)

    return key_cell

def generate_choices_cell(parameters, key, module, indlvl=1):
    data = parameters[key]
    choices = data.get('choices')
    default = data.get('default')

    cell_lines = []

    def process_choices():
        cell_lines.extend([
            '%s  - Choices:\n' % (INDENT * indlvl),
            '\n',
        ])
        for choice in choices:
            if choice == default:
                cell_lines.extend([
                    '%s  - %s (*default*)\n' % (INDENT * (indlvl + 1), choice),
                ])
            else:
                cell_lines.extend([
                    '%s  - %s\n' % (INDENT * (indlvl + 1), choice),
                ])

    def process_default():
        if default is not None:
            cell_lines.extend([
                '%s  - Default:\n' % INDENT * indlvl,
                '\n',
                '%s    *%s*\n' % (INDENT * indlvl, default),
            ])
        else:
            cell_lines.extend([
                '%s  -\n' % (INDENT * indlvl),
            ])

    if choices is not None:
        process_choices()
    else:
        process_default()

    return ''.join(cell_lines)


def generate_comment_cell(parameters, key, module, indlvl=1):
    description = parameters[key].get('description')
    if description is None:
        return '%s  -\n' % INDENT * indlvl

    # Fallthrough
    if isinstance(description, str):
        return '%s  - %s\n' % (INDENT * indlvl, process_comment_text(description))

    # Fallthrough
    cell_lines = []

    
    # First line
    cell_lines.extend([
        '%s  - %s\n' % (INDENT * indlvl, process_comment_text(description[0]))
    ])

    # Rest of lines
    for descline in description[1:]:
        cell_lines.extend([
            '\n',
            '%s    %s\n' % (INDENT * indlvl, process_comment_text(descline))
        ])

    retval = ''.join(cell_lines)

    if 'suboptions' in parameters[key]:
        suboptions = process_suboptions(parameters, key, module)
        #suboptions = 'suboptionshere'
        retval = ''.join([
            '%s' % retval,
            '\n',
            '%s' % suboptions,
        ])

    return retval

def process_suboptions(parameters, key, module):

    header = ''.join([
    '%s.. list-table::\n' % (INDENT * 2),
    '%s:widths: 10 10 60\n' % (INDENT * 3),
    '%s:header-rows: 1\n' % (INDENT * 3),
    '\n',
    '%s* - Suboption\n' % (INDENT * 3),
    '%s  - Choices/Defaults\n' % (INDENT * 3),
    '%s  - Comment\n' % (INDENT * 3),
    '\n'
    ])

    suboption_lines = []
    for suboption in sorted(parameters[key]['suboptions']):
        suboption_key = suboption
        suboption_parameters = parameters[key]['suboptions']
        parameter_cell = generate_parameter_cell(suboption_parameters, suboption_key, module, indlvl=3)
        choices_cell = generate_choices_cell(suboption_parameters, suboption_key, module, indlvl=3)
        comment_cell = generate_comment_cell(suboption_parameters, suboption_key, module, indlvl=3)
        suboption_lines.append(''.join([parameter_cell, choices_cell, comment_cell]))

    return ''.join([header, ''.join(suboption_lines), '\n'])

def process_comment_text(text):
    if type(text) != str:
        print('processing text (%s) "%s"' % (type(text), text))
        raise Exception('Cannot process description line "%s"' % text)

    def repl(m):
        if m.group(1) in 'ULM':
            return ' %s' % m.group(2)
        elif m.group(1) in 'CI':
            return ' ``%s``' % m.group(2)
        else:
            raise Exception('Cannot handle replacement "%s"' % m.group(1))

    pattern = r' ([LUICM])\(([^)]*)\)'
    text = re.sub(pattern, repl, text)

    return text

def extract_module_examples(module):
    data = module['examples']
    output_lines = []
    output_lines.append('.. code-block:: yaml+jinja')
    for line in data.splitlines():
        output_lines.append('%s%s' % (INDENT, line))
    return '\n'.join(output_lines)

def extract_module_return_values(module):
    data = module['return']
    if data is None:
        return ''

    # Fallthrough


    output_lines = []
    for key in sorted(data.keys()):
        row = process_return_value_row(data, key)
        output_lines.append(row)

    header = '\n'.join([
    '.. list-table::',
    '%s:widths: 10 10 60' % INDENT,
    '%s:header-rows: 1\n' % INDENT,
    '%s* - Key' % INDENT,
    '%s  - Returned' % INDENT,
    '%s  - Description' % INDENT,
    ])
    body = ''.join(output_lines)
    return ''.join([header,'\n', body])

def process_return_value_row(data, key):
    key = key
    type = data[key]['type']

    key_cell = ''.join([
        '%s* - %s\n' % (INDENT, key),
        '\n',
        '%s    *(%s)*\n' % (INDENT, type), 
    ])

    returned_text = data[key]['returned']
    returned_cell = ''.join([
        '%s  - %s\n' % (INDENT, returned_text),
    ])

    description = data[key]['description']
    description_cell_list = [
        '%s  - %s\n' % (INDENT, description),
    ]

    sample = data[key].get('sample')
    if sample is not None:
        description_cell_list.append(''.join([
                '\n',
                '%s    **%s**\n' % (INDENT, 'Sample:'),
                '\n',
                '%s    %s\n' % (INDENT, sample),
            ])
        )

    description_cell = ''.join(description_cell_list)
    row = ''.join([key_cell, returned_cell, description_cell])
    return row

def extract_module_version_added(module):
    data = module['documentation_data']
    return data['version_added']

def extract_module_reference(module_dict):
    module_name = module_dict['documentation_data']['module']
    return '.. _%s_module:' % module_name

def extract_documentation(module):
    module_dict = {}
    module_dict['documentation_data'] = yaml.load(module.DOCUMENTATION)
    module_dict['examples'] =  module.EXAMPLES
    module_dict['return'] =  yaml.load(module.RETURN)

    module_template_dict = {}

    module_template_dict['module_reference'] = extract_module_reference(module_dict)
    module_template_dict['module_title'] = extract_module_title(module_dict)
    module_template_dict['module_version_added'] = extract_module_version_added(module_dict)
    module_template_dict['module_synopsis'] = extract_module_synopsis(module_dict)
    module_template_dict['module_requirements'] = extract_module_requirements(module_dict)
    module_template_dict['module_parameters'] = extract_module_parameters(module_dict)
    module_template_dict['module_examples'] = extract_module_examples(module_dict)
    module_template_dict['module_return_values'] = extract_module_return_values(module_dict)

    documentation = module_dict['documentation_data']
    module_name = '%s_module.rst' % documentation['module']
    populate_template(module_name, **module_template_dict)




def process_module(module_file):
    if module_file.startswith('__') or module_file == 'netscaler.py':
        print('Skipping processing of file %s' % module_file)
        return
    print('processing module file %s' % module_file)

    ALL_MODULES.append(module_file)

    module_name = os.path.splitext(module_file)[0]

    module = importlib.import_module(module_name)
    extract_documentation(module)

def process_modules():
    global ALL_MODULES
    ALL_MODULES = []
    modules_dir = os.path.abspath(os.path.join(HERE, '../../ansible-modules'))
    sys.path.append(modules_dir)
    for module_file in os.listdir(modules_dir):
        process_module(module_file)
    sys.path = sys.path[:-1]

    generate_module_indexes()

def generate_module_indexes():
    refs = []

    for module_file in sorted(ALL_MODULES):
        ref = '  * :ref:`%s_module`\n' % os.path.splitext(module_file)[0]
        refs.append(ref)

    all_modules_header = ''.join([
        '.. _all_modules:\n',
        '\n',
        'All modules\n',
        '```````````\n',
        '\n\n\n',
    ])

    network_modules_header = ''.join([
        '.. _network_modules:\n',
        '\n',
        'Network modules\n',
        '```````````\n',
        '\n\n\n',
    ])

    list_of_all_modules_path = os.path.join(args.output_dir, 'list_of_all_modules.rst')
    list_of_network_modules_path = os.path.join(args.output_dir, 'list_of_network_modules.rst')

    with open(list_of_all_modules_path, 'w') as fh:
        content = ''.join([
            all_modules_header,
            ''.join(refs)
        ])
        fh.write(content)

    with open(list_of_network_modules_path, 'w') as fh:
        content = ''.join([
            network_modules_header,
            ''.join(refs)
        ])
        fh.write(content)

def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    global FRAGMENTS
    FRAGMENTS = get_document_fragments()

    process_modules()

if __name__ == '__main__':
    main()
