#!/usr/bin/env python


import requests
import re
import json
import os
from lxml import html


def scrap_page(page):
    properties = []
    r = requests.get(page)
    if r.status_code != 200:
        raise Exception('status %s' % r.status_code)
    htmltree = html.fromstring(r.content)
    tables = htmltree.xpath('''//table[@class='cx-table']''')
    if len(tables) > 1:
        raise Exception('Found too many documentation tables')

    rows = htmltree.xpath('''//table[@class='cx-table']/tbody//tr''')
    if len(rows) == 0:
        raise Exception('Could not find documentation table for %s' % page)

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

def update_for_immutables(properties, base_command_url, item):
    m = re.match(r'^.*/(.*)$', item)
    if m is None:
        raise Exception('Cannot match item: ' % item)
    command_with_dashes = m.group(1)
    command_with_spaces = m.group(1).replace('-',' ')

    page = base_command_url + item + '.html'

    r = requests.get(page)
    htmltree = html.fromstring(r.content)
    id = 'set-%s' % command_with_dashes
    h2s = htmltree.xpath('''//h2/following-sibling::p''' )
    for h2 in h2s:
        if h2.text is not None:
            doc_text = h2.text.strip().lower()
            if doc_text.startswith('set %s' % command_with_spaces):
                break
    else:
        raise Exception('Cannot find "set %s"' % command_with_spaces)
    #print(doc_text)
    mutable_options = [ item[1:] for item in re.findall(r'-\w+', doc_text)]
    #print('Mutables %s' % mutable_options)
    updated_properties = []
    for property in properties:
        #print('Muting property %s' % property['name'])
        property['mutable'] = property['name'] in mutable_options
        #print('new property %s' % property)
        updated_properties.append(property)
    return updated_properties
    #print('options: %s' % [ item[1:] for item in re.findall(r'-\w+', doc_text)])
    


def main():
    base_nitro_url = 'http://docs.citrix.com/en-us/netscaler/11-1/nitro-api/nitro-rest/api-reference/configuration/'
    base_command_url = 'http://docs.citrix.com/en-us/netscaler/11-1/reference/netscaler-command-reference/'
    pages = [
        #('basic/servicegroup', 'basic/servicegroup'),
        #('basic/service', 'basic/service'),
        #('basic/server', 'basic/server'),
        #('basic/servicegroup_servicegroupmember_binding', None)
        #('load-balancing/lbvserver', 'lb/lb-vserver'),
        #('load-balancing/lbvserver_service_binding', None)
        #('load-balancing/lbvserver_servicegroup_binding', None)
        #('load-balancing/lbmonitor', 'lb/lb-monitor'),
        #('content-switching/csvserver', 'cs/cs-vserver'),
        #('content-switching/cspolicy', 'cs/cs-policy'),
        #('content-switching/csaction', 'cs/cs-action'),
        #('ssl/sslcertkey', 'ssl/ssl-certkey'),
        #('global-server-load-balancing/gslbsite', 'gslb/gslb-site'),
        #('global-server-load-balancing/gslbservice', 'gslb/gslb-service'),
        #('global-server-load-balancing/gslbvserver', 'gslb/gslb-vserver'),
        ('global-server-load-balancing/gslbvserver_domain_binding', None),

    ]
    for page in pages:
        page_file = re.sub('/','_',page[0])
        page_file += '.json'
        if os.path.exists(page_file):
            print('Skipping %s' % page_file)
            continue
        properties = scrap_page(base_nitro_url + page[0] + '.html')
        if page[1] is not None:
            properties = update_for_immutables(properties, base_command_url, page[1] )
        print('writing to file %s' % page_file)
        with open(page_file, 'w') as fh:
            json.dump(properties, fh, indent=4)




if __name__ == '__main__':
    main()
