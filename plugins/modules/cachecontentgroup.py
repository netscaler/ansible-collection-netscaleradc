#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: cachecontentgroup
short_description: Configuration for Integrated Cache content group resource.
description: Configuration for Integrated Cache content group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - flushed
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(flushed), the resource will be flushed on the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  absexpiry:
    type: list
    description:
      - Local time, up to 4 times a day, at which all objects in the content group
        must expire.
      - ''
      - 'CLI Users:'
      - 'For example, to specify that the objects in the content group should expire
        by 11:00 PM, type the following command: add cache contentgroup <contentgroup
        name> -absexpiry 23:00'
      - 'To specify that the objects in the content group should expire at 10:00 AM,
        3 PM, 6 PM, and 11:00 PM, type: add cache contentgroup <contentgroup name>
        -absexpiry 10:00 15:00 18:00 23:00'
    elements: str
  absexpirygmt:
    type: list
    description:
      - Coordinated Universal Time (GMT), up to 4 times a day, when all objects in
        the content group must expire.
    elements: str
  alwaysevalpolicies:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Force policy evaluation for each response arriving from the origin server.
        Cannot be set to C(YES) if the Prefetch parameter is also set to C(YES).
  cachecontrol:
    type: str
    description:
      - Insert a Cache-Control header into the response.
  expireatlastbyte:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Force expiration of the content immediately after the response is downloaded
        (upon receipt of the last byte of the response body). Applicable only to positive
        responses.
  flashcache:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Perform flash cache. Mutually exclusive with Poll Every Time (PET) on the
        same content group.
  heurexpiryparam:
    type: float
    description:
      - Heuristic expiry time, in percent of the duration, since the object was last
        modified.
  hitparams:
    type: list
    description:
      - Parameters to use for parameterized hit evaluation of an object. Up to 128
        parameters can be specified. Mutually exclusive with the Hit Selector parameter.
    elements: str
  hitselector:
    type: str
    description:
      - Selector for evaluating whether an object gets stored in a particular content
        group. A selector is an abstraction for a collection of PIXL expressions.
  host:
    type: str
    description:
      - Flush only objects that belong to the specified host. Do not use except with
        parameterized invalidation. Also, the Invalidation Restricted to Host parameter
        for the group must be set to YES.
  ignoreparamvaluecase:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore case when comparing parameter values during parameterized hit evaluation.
        (Parameter value case is ignored by default during parameterized invalidation.)
  ignorereloadreq:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore any request to reload a cached object from the origin server.
      - To guard against Denial of Service attacks, set this parameter to C(YES).
        For RFC-compliant behavior, set it to C(NO).
  ignorereqcachinghdrs:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore Cache-Control and Pragma headers in the incoming request.
  insertage:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert an Age header into the response. An Age header contains information
        about the age of the object, in seconds, as calculated by the integrated cache.
  insertetag:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert an ETag header in the response. With ETag header insertion, the integrated
        cache does not serve full responses on repeat requests.
  insertvia:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert a Via header into the response.
  invalparams:
    type: list
    description:
      - Parameters for parameterized invalidation of an object. You can specify up
        to 8 parameters. Mutually exclusive with invalSelector.
    elements: str
  invalrestrictedtohost:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Take the host header into account during parameterized invalidation.
  invalselector:
    type: str
    description:
      - Selector for invalidating objects in the content group. A selector is an abstraction
        for a collection of PIXL expressions.
  lazydnsresolve:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Perform DNS resolution for responses only if the destination IP address in
        the request does not match the destination IP address of the cached response.
  matchcookies:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Evaluate for parameters in the cookie header also.
  maxressize:
    type: float
    description:
      - Maximum size of a response that can be cached in this content group.
  memlimit:
    type: float
    description:
      - Maximum amount of memory that the cache can use. The effective limit is based
        on the available memory of the Citrix ADC.
  minhits:
    type: int
    description:
      - Number of hits that qualifies a response for storage in this content group.
  minressize:
    type: float
    description:
      - Minimum size of a response that can be cached in this content group.
      - ' Default minimum response size is 0.'
  name:
    type: str
    description:
      - Name for the content group.  Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the content group is created.
  persistha:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Setting persistHA to C(YES) causes IC to save objects in contentgroup to Secondary
        node in HA deployment.
  pinned:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Do not flush objects from this content group under memory pressure.
  polleverytime:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Always poll for the objects in this content group. That is, retrieve the objects
        from the origin server whenever they are requested.
  prefetch:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Attempt to refresh objects that are about to go stale.
  prefetchmaxpending:
    type: float
    description:
      - Maximum number of outstanding prefetches that can be queued for the content
        group.
  prefetchperiod:
    type: float
    description:
      - Time period, in seconds before an object's calculated expiry time, during
        which to attempt prefetch.
  prefetchperiodmillisec:
    type: float
    description:
      - Time period, in milliseconds before an object's calculated expiry time, during
        which to attempt prefetch.
  query:
    type: str
    description:
      - Query string specifying individual objects to flush from this group by using
        parameterized invalidation. If this parameter is not set, all objects are
        flushed from the group.
  quickabortsize:
    type: float
    description:
      - If the size of an object that is being downloaded is less than or equal to
        the quick abort value, and a client aborts during the download, the cache
        stops downloading the response. If the object is larger than the quick abort
        size, the cache continues to download the response.
  relexpiry:
    type: float
    description:
      - Relative expiry time, in seconds, after which to expire an object cached in
        this content group.
  relexpirymillisec:
    type: float
    description:
      - Relative expiry time, in milliseconds, after which to expire an object cached
        in this content group.
  removecookies:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Remove cookies from responses.
  selectorvalue:
    type: str
    description:
      - Value of the selector to be used for flushing objects from the content group.
        Requires that an invalidation selector be configured for the content group.
  tosecondary:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - content group whose objects are to be sent to secondary.
  type:
    type: str
    choices:
      - HTTP
      - MYSQL
      - MSSQL
    description:
      - The type of the content group.
  weaknegrelexpiry:
    type: float
    description:
      - 'Relative expiry time, in seconds, for expiring negative responses. This value
        is used only if the expiry time cannot be determined from any other source.
        It is applicable only to the following status codes: 307, 403, 404, and 410.'
  weakposrelexpiry:
    type: float
    description:
      - Relative expiry time, in seconds, for expiring positive responses with response
        codes between 200 and 399. Cannot be used in combination with other Expiry
        attributes. Similar to -relExpiry but has lower precedence.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample cachecontentgroup playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure cachecontentgroup
      delegate_to: localhost
      netscaler.adc.cachecontentgroup:
        nsip: '{{ nsip }}'
        nitro_user: '{{ nitro_user }}'
        nitro_pass: '{{ nitro_pass }}'
        validate_certs: '{{ validate_certs }}'
        state: present
        name: NSFEO
        maxressize: 1994752
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
failed:
  description: Indicates if the module failed or not
  returned: always
  type: bool
  sample: false
loglines:
  description: list of logged messages by the module
  returned: always
  type: list
  sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
