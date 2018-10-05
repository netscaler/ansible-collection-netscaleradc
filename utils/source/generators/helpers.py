

def calculate_transforms_for_attribute(attribute):

    # Check for ON, OFF
    choice_set = set(attribute.get('choices',[]))
    print(choice_set)
    if set(choice_set) == set(['on', 'off']):
        return "lambda v: 'ON' if v else 'OFF'"
    elif set(choice_set) == set(['ON', 'OFF']):
        return "lambda v: 'ON' if v else 'OFF'"
    elif set(choice_set) == set(['ENABLED', 'DISABLED']):
        return 'lambda v: v.upper()'

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
        elif choice_set == set(['ENABLE', 'DISABLE']):
            doc_item['choices'] = ['enable', 'disable']
        elif 'choices' in attribute:
            doc_item['choices'] = attribute['choices']

        # Catch non existant description
        description = attribute.get('description')
        if description is None:
            raise Exception('Cannot find description for attribute %s' % attribute['option_name'])
        else:
            doc_item['description'] = attribute['description']

        # Copy type
        attribute_type = attribute.get('type')
        if doc_item.get('choices') == ['on', 'off']:
            doc_item['type'] = 'bool'
            del doc_item['choices']
        elif attribute_type == 'float':
            doc_item['type'] = 'str'
        else:
            doc_item['type'] = attribute.get('type')

        doc_list.append(doc_item)

    return doc_list

def calculate_attributes_config_dict(resource_name, attribute_list, skip_attributes=[]):
    attributes_config_dict = {}
    attributes_config_dict['resource_name'] = resource_name
    attributes_config_dict['attributes'] = [item['option_name'] for item in attribute_list]

    attributes_config_dict['transforms'] = {}
    for attribute in attribute_list:

        # Skip attribute
        if attribute['option_name'] in skip_attributes:
            continue

        transform = calculate_transforms_for_attribute(attribute)
        if transform is not None:
            key = attribute['option_name']
            attributes_config_dict['transforms'][key] = transform

    attributes_config_dict['get_id_attributes'] = [item['option_name'] for item in attribute_list if item['is_get_id']]
    attributes_config_dict['delete_id_attributes'] = [item['option_name'] for item in attribute_list if item['is_delete_id']]

    return attributes_config_dict
