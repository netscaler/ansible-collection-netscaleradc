#!/usr/bin/env python3

from __future__ import print_function

import sys
import re
import argparse
import logging


if sys.version_info[0] == 2:
    from HTMLParser import HTMLParser
    # from htmlentitydefs import name2codepoint
elif sys.version_info[0] == 3:
    from html.parser import HTMLParser
    # from html.entities import name2codepoint

import json


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.entity = None
        self.state = 'IDLE'
        self.data = {
            'rwattrs': [],
            'roattrs': [],
            'addattrs': [],
            'updateattrs': [],
        }
        self.new_current_attr()

        self.re_json_arg = re.compile(r'"([^"]+)": *<[^>]+>')

    def new_current_attr(self):
        self.current_attr = {
            'name': None,
            'type': None,
            'description': [],
        }

    def json_data(self):
        rw_dict = {v['name']: v for v in self.data['rwattrs']}
        ro_dict = {v['name']: v for v in self.data['roattrs']}
        json_data = []
        for attribute in self.data['addattrs']:
            data_entry = rw_dict[attribute]
            entry = {}
            entry['name'] = attribute
            entry['description_lines'] = data_entry['description']
            if data_entry['type'] == '<String>':
                entry['type'] = 'str'
            elif data_entry['type'] == '<Integer>':
                entry['type'] = 'int'
            elif data_entry['type'] == '<Double>':
                entry['type'] = 'float'
            elif data_entry['type'] == '<Double[]>':
                entry['type'] = 'list'
            elif data_entry['type'] == '<String[]>':
                entry['type'] = 'list'
            elif data_entry['type'] == '<Boolean>':
                entry['type'] = 'bool'
            else:
                raise Exception('Cannot determine type %s' % data_entry['type'])

            entry['mutable'] = attribute in self.data['updateattrs']
            entry['readonly'] = False

            json_data.append(entry)

        for attribute, value in ro_dict.items():
            entry = {
                'name': attribute,
                'description_lines': value['description'],
                'readonly': True,
                'mutable': False,
            }

            json_data.append(entry)

        return json_data

    def transition_state(self, next_state):
        logging.debug('%s -> %s' % (self.state, next_state))
        self.state = next_state

    def handle_starttag(self, tag, attrs):
        attr_dict = {}
        for attr in attrs:
            attr_dict[attr[0]] = attr[1]

        if self.state == 'IDLE':
            if tag == 'title':
                self.transition_state('TITLE')

        if self.state in ('IDLE', 'RWATTR', 'ROATTR', 'OPERATION_ADD', 'OPERATION_UPDATE'):
            if tag == 'p' and 'class' in attr_dict and attr_dict['class'] == 'heading':
                self.transition_state('SCAN_HEADING')

        if self.state == 'RWATTR' and tag == 'p' and 'class' in attr_dict and attr_dict['class'] == 'property_name':
            self.transition_state('RWATTR_NAME')

        if self.state == 'RWATTR' and tag == 'p' and 'class' in attr_dict and attr_dict['class'] == 'property_description':
            self.transition_state('RWATTR_DESCRIPTION')

        if self.state == 'RWATTR_NAME' and tag == 'span' and 'class' in attr_dict and attr_dict['class'] == 'property_type':
            self.transition_state('RWATTR_TYPE')

        if self.state == 'ROATTR' and tag == 'p' and 'class' in attr_dict and attr_dict['class'] == 'property_name':
            self.transition_state('ROATTR_NAME')

        if self.state == 'ROATTR' and tag == 'p' and 'class' in attr_dict and attr_dict['class'] == 'property_description':
            self.transition_state('ROATTR_DESCRIPTION')

        if self.state == 'ROATTR_NAME' and tag == 'span' and 'class' in attr_dict and attr_dict['class'] == 'property_type':
            self.transition_state('ROATTR_TYPE')

        if self.state == 'SCAN_HEADING' and tag == 'a' and attr_dict.get('name') == 'add':
            self.transition_state('OPERATION_ADD')

        if self.state == 'OPERATION_ADD' and tag == 'p' and attr_dict.get('class') == 'payload':
            self.transition_state('PAYLOAD_ADD')

        if self.state == 'SCAN_HEADING' and tag == 'a' and attr_dict.get('name') == 'update':
            self.transition_state('OPERATION_UPDATE')

        if self.state == 'OPERATION_UPDATE' and tag == 'p' and attr_dict.get('class') == 'payload':
            self.transition_state('PAYLOAD_UPDATE')

    def handle_data(self, data):

        data = data.strip()
        if self.state == 'TITLE':
            self.entity = data

        if self.state == 'SCAN_HEADING':
            logging.debug('heading %s' % data)
            if data == 'Read/write properties':
                self.transition_state('RWATTR')
            elif data == 'Read only properties':
                self.transition_state('ROATTR')

        if self.state in ('RWATTR_NAME', 'ROATTR_NAME'):
            if data != '':
                self.current_attr['name'] = data

        if self.state in ('RWATTR_TYPE', 'ROATTR_TYPE'):
            self.current_attr['type'] = data

        if self.state in ('RWATTR_DESCRIPTION', 'ROATTR_DESCRIPTION'):
            self.current_attr['description'].append(data)

        if self.state == 'PAYLOAD_ADD':
            m = self.re_json_arg.match(data)
            if m:
                logging.debug('add: %s' % m.group(1))
                self.data['addattrs'].append(m.group(1))

        if self.state == 'PAYLOAD_UPDATE':
            m = self.re_json_arg.match(data)
            if m:
                logging.debug('add: %s' % m.group(1))
                self.data['updateattrs'].append(m.group(1))

    def handle_endtag(self, tag):
        if self.state == 'TITLE':
            if tag == 'title':
                self.transition_state('IDLE')

        if self.state == 'RWATTR_NAME' and tag == 'p':
            self.transition_state('RWATTR')

        if self.state == 'RWATTR_TYPE' and tag == 'span':
            self.transition_state('RWATTR_NAME')

        if self.state == 'RWATTR_DESCRIPTION' and tag == 'p':
            self.transition_state('RWATTR')
            self.data['rwattrs'].append(self.current_attr)
            self.new_current_attr()

        if self.state == 'ROATTR_NAME' and tag == 'p':
            self.transition_state('ROATTR')

        if self.state == 'ROATTR_TYPE' and tag == 'span':
            self.transition_state('ROATTR_NAME')

        if self.state == 'ROATTR_DESCRIPTION' and tag == 'p':
            self.transition_state('ROATTR')
            self.data['roattrs'].append(self.current_attr)
            self.new_current_attr()

        if self.state == 'PAYLOAD_ADD' and tag == 'p':
            self.transition_state('OPERATION_ADD')

        if self.state == 'PAYLOAD_UPDATE' and tag == 'p':
            self.transition_state('OPERATION_UPDATE')

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass
        # c = chr(name2codepoint[name])

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
            print("Num ent  :", c)

    def handle_decl(self, data):
        pass


def main():

    parser = argparse.ArgumentParser(description='Parse a NITRO API html file and produce a json file with its attributes.')
    parser.add_argument('html', help='NITRO API input html file')
    parser.add_argument('--json-data', help='Output json file', required=True)
    parser.add_argument('--log-level', default='warning')
    args = parser.parse_args()

    log_level = {
        'debug': logging.DEBUG,
        'warning': logging.WARNING,
        'info': logging.INFO,
    }
    logging.basicConfig(level=log_level[args.log_level])

    logging.info('Processing %s' % args.html)

    html_parser = MyHTMLParser()
    with open(args.html, 'rt', encoding='latin-1') as fh:
        html_parser.feed(fh.read())

    json_data = html_parser.json_data()

    if json_data == []:
        logging.warning('Empty json data')

    with open(args.json_data, 'w') as fh:
        json.dump(json_data, fh, indent=4)


if __name__ == '__main__':
    main()
