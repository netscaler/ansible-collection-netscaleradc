from collections import OrderedDict
import copy
import re

def calculate_transforms_for_attribute(attribute):

    # Check for ON, OFF
    choice_set = set(attribute.get('choices',[]))
    #print(choice_set)
    if set(choice_set) == set(['on', 'off']):
        return "lambda v: 'ON' if v else 'OFF'"
    elif set(choice_set) == set(['ON', 'OFF']):
        return "lambda v: 'ON' if v else 'OFF'"
    elif set(choice_set) == set(['yes', 'no']):
        return "lambda v: 'YES' if v else 'NO'"
    elif set(choice_set) == set(['YES', 'NO']):
        return "lambda v: 'YES' if v else 'NO'"
    elif set(choice_set) == set(['ENABLED', 'DISABLED']):
        return 'lambda v: v.upper()'


def split_description_line(line, width=100):
    line = str(line)
    if len(line) <= width:
        # Escape double quotes
        line = line.replace('"', r'\\"')
        # Put double quotes around line to avoid yaml
        # invalid characters breaking the documentation rendering
        return ''.join(['"', line, '"'])

    else:
        words = line.split()
        line_splits = []
        line = []
        for word in words:
            if len(' '.join(line)) + len(word) > width:
                line_splits.append(' '.join(line))
                line = []
            else:
                line.append(word)

        if len(line) > 0:
            line_splits.append(' '.join(line))

        return line_splits



def calculate_doc_list(attribute_list, skip_attributes=[]):
    doc_list = []
    for attribute in attribute_list:

        # Skip attribute
        if attribute['option_name'] in skip_attributes:
            continue

        # Make new entry
        doc_item = {}
        doc_item['option_name'] = attribute['option_name']

        # Special choices
        choice_set = set(attribute.get('choices',[]))
        if choice_set == set(['ON', 'OFF']):
            doc_item['choices'] = ['on', 'off']
        elif choice_set == set(['YES', 'NO']):
            doc_item['choices'] = ['yes', 'no']
        elif choice_set == set(['ENABLE', 'DISABLE']):
            doc_item['choices'] = ['enable', 'disable']
        elif choice_set == set(['ENABLED', 'DISABLED']):
            doc_item['choices'] = ['enabled', 'disabled']
        elif 'choices' in attribute:
            doc_item['choices'] = attribute['choices']

        # Catch non existant description
        description = attribute.get('description')
        if description is None:
            raise Exception('Cannot find description for attribute %s' % attribute['option_name'])
        else:
            description = process_raw_description_lines(description)
            doc_item['description'] = [split_description_line(line) for line in description]

        # Copy type
        attribute_type = attribute.get('type')
        if doc_item.get('choices') == ['on', 'off']:
            doc_item['type'] = 'bool'
            del doc_item['choices']
        elif doc_item.get('choices') == ['yes', 'no']:
            doc_item['type'] = 'bool'
            del doc_item['choices']
        elif attribute_type == 'float':
            doc_item['type'] = 'str'
        else:
            doc_item['type'] = attribute.get('type')

        doc_list.append(doc_item)

    return doc_list

def process_raw_description_lines(description_lines):
    ret_val = []
    for line in description_lines:
        # Skip possible values lines
        # Documentation will contain the choices option as parsed from the NITRO xml
        if line.startswith('Possible values'):
            continue

        # Skip default value lines
        if line.startswith('Default value'):
            continue

        outline = copy.deepcopy(line)
        # Try to eclose minimum values in C()
        if line.startswith('Minimum value'):
            m = re.match(r'Minimum value *= *(\d+) *', line)
            if m is None:
                raise Exception('Could not parse minimum value for line "{}"'.format(line))
            outline = 'Minimum value = C({})'.format(m.group(1))

        # Try to eclose maximum values in C()
        if line.startswith('Maximum value'):
            m2 = re.match(r'Maximum value *= *(\d+) *', line)
            if m2 is None:
                raise Exception('Could not parse maximum value for line "{}"'.format(line))
            outline = 'Maximum value = C({})'.format(m2.group(1))

        ret_val.append(outline)
    return ret_val


def calculate_attributes_config_dict(resource_name, attribute_list, skip_attributes=[]):
    attributes_config_dict = {}
    attributes_config_dict['resource_name'] = resource_name
    #attributes_config_dict['attributes'] = [item['option_name'] for item in attribute_list]
    attributes_config_dict['attributes'] = []

    attributes_config_dict['transforms'] = OrderedDict()
    for attribute in attribute_list:

        # Skip attribute
        if attribute['option_name'] in skip_attributes:
            continue

        attributes_config_dict['attributes'].append(attribute['option_name'])
        transform = calculate_transforms_for_attribute(attribute)
        if transform is not None:
            key = attribute['option_name']
            attributes_config_dict['transforms'][key] = transform

    attributes_config_dict['get_id_attributes'] = [item['option_name'] for item in attribute_list if item['is_get_id']]
    attributes_config_dict['delete_id_attributes'] = [item['option_name'] for item in attribute_list if item['is_delete_id']]

    return attributes_config_dict
