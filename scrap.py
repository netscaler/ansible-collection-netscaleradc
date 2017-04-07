#!/usr/bin/env python


import requests
import re
import json
from lxml import html


def scrap_page(page):
    properties = []
    r = requests.get(page)
    htmltree = html.fromstring(r.content)
    tables = htmltree.xpath('''//table[@class='cx-table']''')
    if len(tables) > 1:
        raise Exception('Found too many documentation tables')

    rows = htmltree.xpath('''//table[@class='cx-table']/tbody//tr''')
    if len(rows) == 0:
        raise Exception('Could not find documentation table')

    for row in rows:
        entry = {}
        items = row.xpath('''./td/div/div[2]''')
        # Skip empty rows
        if items == []:
            continue
        entry['name'] = items[0].text_content().strip()
        type_text = items[1].text_content().strip()
        type_text = re.sub('^<','',type_text)
        type_text = re.sub('>$','',type_text)

        # Will throw KeyError if type text is not found in dict
        entry['type'] = {
            'String': 'str',
            'Integer': 'int',
            'Boolean': 'bool',
            'Double': 'float',
            'Double[]': 'list',
            'String[]': 'list',
        }[type_text]

        readonly_text = items[2].text_content().strip()
        if readonly_text == 'Read-only':
            entry['readonly'] = True
        elif readonly_text == 'Read-write':
            entry['readonly'] = False
        else:
            raise Exception('Got unexpected value for read only attribute "%s"' % readonly_text)

        # Description
        description_lines = []
        description_lines.append(items[3].text.strip())
        for br in items[3].getchildren():
            if br.tag != 'br':
                raise Exception('Got unexpected tag in description div "%s"' % br.tag)
            if br.tail is not None:
                description_lines.append(br.tail.strip())

        entry['description_lines'] = description_lines

        # Check if we have choices list
        for line in description_lines:
            if line.startswith('Possible values'):
                choices = []
                values_str = re.sub('Possible values = ','', line)
                choices = [ val.strip() for val in values_str.split(',') ]
                entry['choices'] = choices
        properties.append(entry)
    return properties




def main():
    base_url = 'http://docs.citrix.com/en-us/netscaler/11-1/nitro-api/nitro-rest/api-reference/configuration/'
    pages = [
        #'basic/servicegroup',
        #'basic/service',
        #'basic/server',
        #'basic/servicegroup_servicegroupmember_binding',
        #'load-balancing/lbvserver',
        #'load-balancing/lbvserver_service_binding',
        #'load-balancing/lbvserver_servicegroup_binding',
        #'load-balancing/lbmonitor',
        #'content-switching/csvserver',
        #'content-switching/cspolicy',
        'content-switching/csaction',
    ]
    for page in pages:
        properties = scrap_page(base_url + page + '.html')
        page_file = re.sub('/','_',page)
        page_file += '.json'
        print('writing to file %s' % page_file)
        with open(page_file, 'w') as fh:
            json.dump(properties, fh, indent=4)




if __name__ == '__main__':
    main()
