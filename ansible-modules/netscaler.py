
# -*- coding: utf-8 -*-

'''

Netscaler utility classes and functions

Eventually to be merged in ansible module utils


'''


class ConfigProxy(object):

    def __init__(self, actual, client, attributes, module, read_only_attrs=[]):
        # Actual config object from nitro sdk
        self.actual = actual

        self.client = client

        # Dictionary with attributes
        self.attributes = attributes

        # ansible module
        self.module = module

        # Read only attributes
        # needed to know what to return in result
        self.read_only_attrs = read_only_attrs

        self._copy_attributes_to_actual()

    def _copy_attributes_to_actual(self):
        for attribute in self.attributes.keys():
            if attribute in self.module.params:
                value = self.module.params[attribute]
                if value is None:
                    continue
                setattr(self.actual, attribute, self.module.params[attribute])

    def add(self):
        self.actual.add(self.client, self.actual)

    def delete(self):
        self.actual.delete(self.client, self.actual)

netscaler_common_arguments = dict(
    nsip=dict(required=True),
    nitro_user=dict(required=True),
    nitro_pass=dict(required=True),
    nitro_protocol=dict(choices=['http', 'https'], default='https'),
    nitro_timeout=dict(default=310, type='float'),
    ssl_cert_validation=dict(required=True, type='bool'),
    state=dict(choices=['enabled', 'disabled', 'present', 'delete'])
)
