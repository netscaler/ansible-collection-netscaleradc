# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import codecs
import json
import traceback

from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.urls import fetch_url

from .constants import (
    HTTP_SUCCESS_CODES,
    NESTED_POST_DATA_RESOURCES,
)
from .decorators import trace
from .logger import log


class NitroAPIClient(object):
    def __init__(self, module, resource_name):
        self._module = module
        self.check_mode = module.check_mode  # Dry run mode
        self.api_path = self._module.params.get("api_path")
        self.resource_name = resource_name

        # Prepare the http headers according to module arguments
        self._headers = {}
        self._headers["Content-Type"] = "application/json"
        self._headers["User-Agent"] = "ansible-ctxadc"

        # Check for conflicting authentication methods
        have_token = self._module.params.get("nitro_auth_token") is not None
        have_userpass = None not in (
            self._module.params.get("nitro_user"),
            self._module.params.get("nitro_pass"),
        )

        # Prioritize token over user/pass
        if have_token:
            self._headers["Cookie"] = (
                "NITRO_AUTH_TOKEN=%s" % self._module.params["nitro_auth_token"]
            )
        elif have_userpass:
            self._headers["X-NITRO-USER"] = self._module.params["nitro_user"]
            self._headers["X-NITRO-PASS"] = self._module.params["nitro_pass"]
        elif self.resource_name in {"login", "change_password"}:
            # Do not set any authentication headers for the `login` resource
            pass
        else:
            self._module.fail_json(
                msg="Either `nitro_auth_token` or `nitro_user/nitro_pass` must be given for authentication for the resource %s"
                % self.resource_name
            )

        # Do header manipulation when using NetScaler Console (ADM) as proxy
        # Refer: https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software/current-release/adm-as-api-proxy-server.html
        netscaler_console_as_proxy = self._module.params.get(
            "netscaler_console_as_proxy_server"
        )
        if netscaler_console_as_proxy:
            if self._module.params.get("managed_netscaler_instance_name"):
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_NAME"
                ] = self._module.params.get("managed_netscaler_instance_name")
            if self._module.params.get("managed_netscaler_instance_ip"):
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_IP"
                ] = self._module.params.get("managed_netscaler_instance_ip")
            if self._module.params.get("managed_netscaler_instance_id"):
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_ID"
                ] = self._module.params.get("managed_netscaler_instance_id")
            if self._module.params.get("managed_netscaler_instance_username"):
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_USERNAME"
                ] = self._module.params.get("managed_netscaler_instance_username")
            if self._module.params.get("managed_netscaler_instance_password"):
                self._headers[
                    "_MPS_API_PROXY_MANAGED_INSTANCE_PASSWORD"
                ] = self._module.params.get("managed_netscaler_instance_password")

    @trace
    def url_builder(
        self,
        resource,
        id=None,
        args=None,
        attrs=None,
        filter=None,
        action=None,
        count=False,
    ):
        args = args if args is not None else {}
        attrs = attrs if attrs is not None else []
        filter = filter if filter is not None else {}

        # Construct basic URL
        if resource in NESTED_POST_DATA_RESOURCES:
            url = "%s://%s/%s/%s/%s" % (
                self._module.params["nitro_protocol"],
                self._module.params["nsip"],
                self.api_path,
                "routerDynamicRouting",
                resource,
            )
        else:
            url = "%s://%s/%s/%s" % (
                self._module.params["nitro_protocol"],
                self._module.params["nsip"],
                self.api_path,
                resource,
            )

        # Append resource id
        if id:
            # if id is float type and it is equal to int(id) then convert it to int
            # Reason: nd6ravariables module has a primary key (vlan) of type float
            # however, the Nitro API expects the id to be of type int
            # http://NSIP/nitro/v1/config/nd6ravariables/1.0 -- This does not work
            # http://NSIP/nitro/v1/config/nd6ravariables/1 -- This works
            if isinstance(id, float) and id == int(id):
                id = int(id)
            # Double encode the id
            # https://owasp.org/www-community/Double_Encoding
            url = "%s/%s" % (url, quote(quote(str(id), safe=""), safe=""))

        # Query String Builder
        # Construct args
        args_val = ",".join(
            ["%s:%s" % (k, quote(codecs.encode(str(args[k])), safe="")) for k in args]
        )
        args_val = ("args=%s" % args_val) if args_val != "" else ""

        # Construct attrs
        attrs_val = ",".join(attrs)
        attrs_val = ("attrs=%s" % attrs_val) if attrs_val != "" else ""

        # Construct filters
        # if filter = {'key1':'value1', 'key2':'value2'}
        # filter_val=key1:value1,key2:value2
        # filter_val = ",".join(["%s:%s" % (k, filter[k]) for k in filter])
        filter_val = ",".join(
            [
                "%s:%s" % (k, quote(codecs.encode(str(filter[k])), safe=""))
                for k in filter
            ]
        )
        filter_val = ("filter=%s" % filter_val) if filter_val != "" else ""

        # Construct action
        action_val = "action=%s" % action if action is not None else ""

        # Construct count
        count_val = "count=yes" if count else ""

        # Filter out empty string parameters
        val_list = [args_val, attrs_val, filter_val, action_val, count_val]
        query_params = "&".join([v for v in val_list if v != ""])

        return "%s?%s" % (url, query_params) if query_params != "" else url

    @trace
    def send(self, method, url, data=None):
        # log the self object contents
        log("DEBUG: self=%s" % self.__dict__)
        if self.check_mode and method != "GET":
            log("DEBUG: check_mode is enabled, skipping %s:%s request" % (method, url))
            return 0, {}

        r, info = fetch_url(
            self._module, url=url, headers=self._headers, method=method, data=data
        )
        log("DEBUG: fetch_url()-resonse-info= %s: %s" % (method, info))
        status_code = info["status"]
        # if status_code == -1:
        #     log("ERROR: Could not connect to the target Netscaler instance: %s" % url)
        #     return status_code, {}
        body = r.read() if r else None
        # info['body'] will not be present for status_codes < 400
        if status_code >= 400:
            try:
                return status_code, json.loads(to_text(info["body"]))
            # Catch json.decoder.JSONDecodeError and print the full stack trace
            except json.decoder.JSONDecodeError as e:
                log("ERROR: json.decoder.JSONDecodeError: %s" % e)
                log("DEBUG: info['body'] = %s" % info["body"])
                log("DEBUG: Traceback = %s" % traceback.format_exc())
                return status_code, {}
        else:
            if not body:
                if "body" in info:
                    try:
                        return status_code, json.loads(to_text(info["body"]))
                    except json.decoder.JSONDecodeError as e:
                        log("ERROR: json.decoder.JSONDecodeError: %s" % e)
                        log("DEBUG: info['body'] = %s" % info["body"])
                        log("DEBUG: Traceback = %s" % traceback.format_exc())
                        return status_code, {}
                else:
                    return status_code, {}
            else:
                try:
                    return status_code, json.loads(to_text(body))
                except json.decoder.JSONDecodeError as e:
                    log("ERROR: json.decoder.JSONDecodeError: %s" % e)
                    log("DEBUG: info['body'] = %s" % info["body"])
                    log("DEBUG: Traceback = %s" % traceback.format_exc())
                    return status_code, {}

    @trace
    def get(self, resource, id=None, args=None, attrs=None, filter=None):
        url = self.url_builder(resource, id=id, args=args, attrs=attrs, filter=filter)
        status_code, response_body = self.send("GET", url)
        if status_code not in HTTP_SUCCESS_CODES:
            return status_code, response_body
        if "service" in response_body.keys():
            for service in response_body["service"]:
                if "ip" not in service.keys() and "ipaddress" in service.keys():
                    service["ip"] = service["ipaddress"]
        return status_code, response_body

    @trace
    def post(self, post_data, resource, action=None):
        url = self.url_builder(resource, action=action)
        data = self._module.jsonify(post_data)
        if resource == "login":
            # Remove 'X-NITRO-USER', 'X-NITRO-PASS' and 'Cookie' headers if present
            self._headers.pop("X-NITRO-USER", None)
            self._headers.pop("X-NITRO-PASS", None)
            self._headers.pop("Cookie", None)
        if resource in {"login", "logout"}:
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_NAME", None)
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_IP", None)
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_ID", None)
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_USERNAME", None)
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_PASSWORD", None)
            self._headers.pop("_MPS_API_PROXY_MANAGED_INSTANCE_SESSID", None)
        return self.send("POST", url, data)

    @trace
    def put(self, put_data, resource=None, id=None):
        url = self.url_builder(resource, id=id)
        data = self._module.jsonify(put_data)
        return self.send("PUT", url, data)

    @trace
    def delete(self, resource, id=None, args=None):
        url = self.url_builder(resource, id=id, args=args)
        return self.send("DELETE", url)
