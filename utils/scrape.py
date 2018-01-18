#!/usr/bin/env python


import requests
import re
import json
import argparse
import os
from lxml import html


def scrape_page(page):
    properties = []
    print('Scraping page %s' % page)
    r = requests.get(page)
    if r.status_code != 200:
        raise Exception('status %s' % r.status_code)
    htmltree = html.fromstring(r.content)
    with open('out.html', 'w') as fh:
        fh.write(html.tostring(htmltree))
    tables = htmltree.xpath('''//div[@class='rst-content']//table''')

    if len(tables) == 0:
        raise Exception('Cannot find documentation table')

    if len(tables) > 1:
        raise Exception('Found too many documentation tables')

    rows = htmltree.xpath('''//div[@class='rst-content']//table/tbody//tr''')
    if len(rows) == 0:
        raise Exception('Could not find documentation table for %s' % page)

    for row in rows:
        entry = {}
        items = row.xpath('''./td''')
        # Skip empty rows
        if items == []:
            #print ("Empty row")
            continue
        entry['name'] = items[0].text_content().strip()
        type_text = items[1].text_content().strip()
        type_text = re.sub('^<', '', type_text)
        type_text = re.sub('>$', '', type_text)

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
        entry['description_lines'] = items[3].text.strip().split('<br>')

        # Check if we have choices list
        for line in entry['description_lines']:
            if line.startswith('Possible values'):
                choices = []
                values_str = re.sub('Possible values = ', '', line)
                choices = [val.strip() for val in values_str.split(',')]
                entry['choices'] = choices
        properties.append(entry)
    return properties


def update_for_immutables(properties, base_command_url, item):
    m = re.match(r'^.*/(.*)$', item)
    if m is None:
        raise Exception('Cannot match item: ' % item)
    # command_with_dashes = m.group(1)
    command_with_spaces = m.group(1).replace('-', ' ')

    page = base_command_url + item

    print('Scraping %s' % page)
    r = requests.get(page)
    htmltree = html.fromstring(r.content)
    #print(htmltree)
    # id = 'set-%s' % command_with_dashes
    h2s = htmltree.xpath('''//h2/following-sibling::p''')
    for h2 in h2s:
        if h2.text is not None:
            doc_text = h2.text.strip().lower()
            if doc_text.startswith('set %s' % command_with_spaces):
                break
    else:
        raise Exception('Cannot find "set %s"' % command_with_spaces)
    #print(doc_text)
    mutable_options = [item[1:] for item in re.findall(r'-\w+', doc_text)]
    #print('Mutables %s' % mutable_options)
    updated_properties = []
    for property in properties:
        # print('Muting property %s' % property['name'])
        property['mutable'] = property['name'] in mutable_options
        # print('new property %s' % property)
        updated_properties.append(property)
    return updated_properties
    # print('options: %s' % [ item[1:] for item in re.findall(r'-\w+', doc_text)])


def main():
    #base_nitro_url = 'https://docs.citrix.com/en-us/netscaler/11-1/nitro-api/nitro-rest/api-reference/configuration/'
    #base_command_url = 'https://docs.citrix.com/en-us/netscaler/11-1/reference/netscaler-command-reference/'

    parser = argparse.ArgumentParser(description='Scrape html page for nitro object attributes')
    parser.add_argument(
        '--base-nitro-url',
        default='https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/12.0/configuration/',
        help='The base url for the nitro object'
    )
    parser.add_argument(
        '--base-command-url',
        default='https://developer-docs.citrix.com/projects/netscaler-command-reference/en/12.0/',
        help='The base url for the nitro command'
    )
    parser.add_argument(
        '--nitro-url',
        required=True,
        help='The full url to the nitro object documentation page'
    )
    parser.add_argument(
        '--command-url',
        help='The full url to the nitro command documentation page'
    )

    args = parser.parse_args()

    # Scrape nitro object
    if args.base_nitro_url not in args.nitro_url:
        raise Exception('Cannot find base nitro url in %s' % args.nitro_url)

    truncate_start = args.nitro_url.find(args.base_nitro_url) + len(args.base_nitro_url)
    nitro_page = args.nitro_url[truncate_start:]
    page_file = re.sub('/', '_', nitro_page)
    page_file = page_file[:page_file.rindex('_')]
    page_file += '.json'

    properties = scrape_page(args.base_nitro_url + nitro_page)

    # Apply command url processing
    if args.command_url is not None:
        if args.base_command_url not in args.command_url:
            raise Exception('Cannot find base command url in %s' % args.command_url)
        truncate_start = args.nitro_url.find(args.base_command_url) + len(args.base_command_url)
        command_page = args.command_url[truncate_start:]
        properties = update_for_immutables(properties, args.base_command_url, command_page)

    # Write json file
    print('writing to file %s' % page_file)
    with open(page_file, 'w') as fh:
        json.dump(properties, fh, indent=4)


if __name__ == '__main__':
    main()
