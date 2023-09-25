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
module: cachecontentgroup
short_description: Configuration for Integrated Cache content group resource.
description: Configuration for Integrated Cache content group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  absexpiry:
    description:
      - 'Local time, up to 4 times a day, at which all objects in the content group
        must expire. '
      - ''
      - 'CLI Users:'
      - 'For example, to specify that the objects in the content group should expire
        by 11:00 PM, type the following command: add cache contentgroup <contentgroup
        name> -absexpiry 23:00 '
      - 'To specify that the objects in the content group should expire at 10:00 AM,
        3 PM, 6 PM, and 11:00 PM, type: add cache contentgroup <contentgroup name>
        -absexpiry 10:00 15:00 18:00 23:00'
    type: list
    elements: str
  absexpirygmt:
    description:
      - Coordinated Universal Time (GMT), up to 4 times a day, when all objects in
        the content group must expire.
    type: list
    elements: str
  alwaysevalpolicies:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Force policy evaluation for each response arriving from the origin server.
        Cannot be set to C(YES) if the Prefetch parameter is also set to C(YES).
    type: str
    default: 'NO'
  cachecontrol:
    description:
      - Insert a Cache-Control header into the response.
    type: str
  expireatlastbyte:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Force expiration of the content immediately after the response is downloaded
        (upon receipt of the last byte of the response body). Applicable only to positive
        responses.
    type: str
    default: 'NO'
  flashcache:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Perform flash cache. Mutually exclusive with Poll Every Time (PET) on the
        same content group.
    type: str
    default: 'NO'
  heurexpiryparam:
    description:
      - Heuristic expiry time, in percent of the duration, since the object was last
        modified.
    type: float
  hitparams:
    description:
      - Parameters to use for parameterized hit evaluation of an object. Up to 128
        parameters can be specified. Mutually exclusive with the Hit Selector parameter.
    type: list
    elements: str
  hitselector:
    description:
      - Selector for evaluating whether an object gets stored in a particular content
        group. A selector is an abstraction for a collection of PIXL expressions.
    type: str
  host:
    description:
      - Flush only objects that belong to the specified host. Do not use except with
        parameterized invalidation. Also, the Invalidation Restricted to Host parameter
        for the group must be set to YES.
    type: str
  ignoreparamvaluecase:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore case when comparing parameter values during parameterized hit evaluation.
        (Parameter value case is ignored by default during parameterized invalidation.)
    type: str
  ignorereloadreq:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore any request to reload a cached object from the origin server.
      - To guard against Denial of Service attacks, set this parameter to C(YES).
        For RFC-compliant behavior, set it to C(NO).
    type: str
    default: 'YES'
  ignorereqcachinghdrs:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Ignore Cache-Control and Pragma headers in the incoming request.
    type: str
    default: 'YES'
  insertage:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert an Age header into the response. An Age header contains information
        about the age of the object, in seconds, as calculated by the integrated cache.
    type: str
    default: 'YES'
  insertetag:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert an ETag header in the response. With ETag header insertion, the integrated
        cache does not serve full responses on repeat requests.
    type: str
    default: 'YES'
  insertvia:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Insert a Via header into the response.
    type: str
    default: 'YES'
  invalparams:
    description:
      - Parameters for parameterized invalidation of an object. You can specify up
        to 8 parameters. Mutually exclusive with invalSelector.
    type: list
    elements: str
  invalrestrictedtohost:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Take the host header into account during parameterized invalidation.
    type: str
  invalselector:
    description:
      - Selector for invalidating objects in the content group. A selector is an abstraction
        for a collection of PIXL expressions.
    type: str
  lazydnsresolve:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Perform DNS resolution for responses only if the destination IP address in
        the request does not match the destination IP address of the cached response.
    type: str
    default: 'YES'
  matchcookies:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Evaluate for parameters in the cookie header also.
    type: str
  maxressize:
    description:
      - Maximum size of a response that can be cached in this content group.
    type: float
    default: 80
  memlimit:
    description:
      - Maximum amount of memory that the cache can use. The effective limit is based
        on the available memory of the Citrix ADC.
    type: float
    default: 65536
  minhits:
    description:
      - Number of hits that qualifies a response for storage in this content group.
    type: int
  minressize:
    description:
      - Minimum size of a response that can be cached in this content group.
      - ' Default minimum response size is 0.'
    type: float
  name:
    description:
      - Name for the content group.  Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the content group is created.
    type: str
  persistha:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Setting persistHA to C(YES) causes IC to save objects in contentgroup to Secondary
        node in HA deployment.
    type: str
    default: 'NO'
  pinned:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Do not flush objects from this content group under memory pressure.
    type: str
    default: 'NO'
  polleverytime:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Always poll for the objects in this content group. That is, retrieve the objects
        from the origin server whenever they are requested.
    type: str
    default: 'NO'
  prefetch:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Attempt to refresh objects that are about to go stale.
    type: str
    default: 'YES'
  prefetchmaxpending:
    description:
      - Maximum number of outstanding prefetches that can be queued for the content
        group.
    type: float
  prefetchperiod:
    description:
      - Time period, in seconds before an object's calculated expiry time, during
        which to attempt prefetch.
    type: float
  prefetchperiodmillisec:
    description:
      - Time period, in milliseconds before an object's calculated expiry time, during
        which to attempt prefetch.
    type: float
  query:
    description:
      - Query string specifying individual objects to flush from this group by using
        parameterized invalidation. If this parameter is not set, all objects are
        flushed from the group.
    type: str
  quickabortsize:
    description:
      - If the size of an object that is being downloaded is less than or equal to
        the quick abort value, and a client aborts during the download, the cache
        stops downloading the response. If the object is larger than the quick abort
        size, the cache continues to download the response.
    type: float
    default: 4194303
  relexpiry:
    description:
      - Relative expiry time, in seconds, after which to expire an object cached in
        this content group.
    type: float
  relexpirymillisec:
    description:
      - Relative expiry time, in milliseconds, after which to expire an object cached
        in this content group.
    type: float
  removecookies:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Remove cookies from responses.
    type: str
    default: 'YES'
  selectorvalue:
    description:
      - Value of the selector to be used for flushing objects from the content group.
        Requires that an invalidation selector be configured for the content group.
    type: str
  tosecondary:
    choices:
      - 'YES'
      - 'NO'
    description:
      - content group whose objects are to be sent to secondary.
    type: str
    default: 'NO'
  type:
    choices:
      - HTTP
      - MYSQL
      - MSSQL
    description:
      - The type of the content group.
    type: str
    default: HTTP
  weaknegrelexpiry:
    description:
      - 'Relative expiry time, in seconds, for expiring negative responses. This value
        is used only if the expiry time cannot be determined from any other source.
        It is applicable only to the following status codes: 307, 403, 404, and 410.'
    type: float
  weakposrelexpiry:
    description:
      - Relative expiry time, in seconds, for expiring positive responses with response
        codes between 200 and 399. Cannot be used in combination with other Expiry
        attributes. Similar to -relExpiry but has lower precedence.
    type: float
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | cachecontentgroup
      delegate_to: localhost
      netscaler.adc.cachecontentgroup:
        state: present
        name: DEFAULT
    - name: Sample Task | cachecontentgroup | 2
      delegate_to: localhost
      netscaler.adc.cachecontentgroup:
        state: present
        name: BASEFILE
        relexpiry: 86000
        weaknegrelexpiry: 600
        maxressize: 256
        memlimit: 2
    - name: Sample Task | cachecontentgroup | 3
      delegate_to: localhost
      netscaler.adc.cachecontentgroup:
        state: present
        name: DELTAJS
        relexpiry: 86000
        weaknegrelexpiry: 600
        insertage: 'NO'
        maxressize: 256
        memlimit: 1
        pinned: 'YES'
    - name: Sample Task | cachecontentgroup | 4
      delegate_to: localhost
      netscaler.adc.cachecontentgroup:
        state: present
        name: NSFEO
        maxressize: 1994752

"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
