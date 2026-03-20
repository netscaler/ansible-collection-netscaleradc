#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: nslaslicense_offline
short_description: Generate and apply an offline LAS license token to a NetScaler ADC (NS) device.
description:
  - Performs an offline License Activation Service (LAS) token generation and application
    workflow for NetScaler ADC (NS) devices that do not have direct internet access.
  - Retrieves the offline activation request package from the device via the NITRO API and
    SFTP, contacts the LAS cloud service to generate a license token, and applies the
    resulting license blob back to the device.
  - Requires the C(paramiko) Python library on the Ansible control node for SFTP transfers.
version_added: "2.14.0"
author:
  - Lakshman M J (@lakshmj)
options:
  nsip:
    description:
      - The IP address of the NetScaler ADC appliance.
      - Can also be set via the C(NETSCALER_NSIP) environment variable.
    type: str
    required: true
  nitro_user:
    description:
      - The username for the NetScaler ADC appliance. Must be C(nsroot).
      - Can also be set via the C(NETSCALER_NITRO_USER) environment variable.
    type: str
    required: true
    no_log: true
  nitro_pass:
    description:
      - The password for the NetScaler ADC appliance.
      - Can also be set via the C(NETSCALER_NITRO_PASS) environment variable.
    type: str
    required: true
    no_log: true
  nitro_protocol:
    description:
      - Protocol used to communicate with the NITRO API.
    type: str
    choices:
      - http
      - https
    default: https
  validate_certs:
    description:
      - If C(false), SSL certificates will not be validated.
    type: bool
    default: true
  request_pem:
    description:
      - The PEM entitlement identifier for the device (e.g. C(CNS_8905_SERVER)).
    type: str
    required: true
  request_ed:
    description:
      - The license edition.
    type: str
    required: true
    choices:
      - Advanced
      - Premium
      - Standard
  is_fips:
    description:
      - Set to C(true) for FIPS-enabled appliances.
    type: bool
    default: false
  las_secrets_json:
    description:
      - Path to the JSON file on the control node containing LAS cloud service credentials.
      - The file must contain the keys C(ccid), C(client), C(password), C(las_endpoint), and C(cc_endpoint).
    type: str
    required: true
"""

EXAMPLES = r"""
---
- name: Generate and apply offline LAS license for NS (MPX) device
  delegate_to: localhost
  netscaler.adc.nslaslicense_offline:
    nsip: 10.102.201.230
    nitro_user: nsroot
    nitro_pass: "{{ nitro_pass }}"
    nitro_protocol: https
    validate_certs: false
    request_pem: CNS_8905_SERVER
    request_ed: Premium
    is_fips: false
    las_secrets_json: /etc/netscaler/zmcd_secrets.json

- name: Generate and apply offline LAS license for NS (VPX FIPS)
  delegate_to: localhost
  netscaler.adc.nslaslicense_offline:
    nsip: 10.102.201.231
    nitro_user: nsroot
    nitro_pass: "{{ nitro_pass }}"
    request_pem: CNS_V5000_SERVER
    request_ed: Premium
    is_fips: true
    las_secrets_json: /etc/netscaler/zmcd_secrets.json

- name: Retrieve activation request package only (for debugging)
  delegate_to: localhost
  netscaler.adc.nslaslicense_offline:
    nsip: 10.102.201.230
    nitro_user: nsroot
    nitro_pass: "{{ nitro_pass }}"
    request_pem: CNS_8905_SERVER
    request_ed: Standard
    las_secrets_json: /etc/netscaler/zmcd_secrets.json

"""

RETURN = r"""
---
changed:
  description: Indicates if a license was applied to the device.
  returned: always
  type: bool
  sample: true
failed:
  description: Indicates if the module failed.
  returned: always
  type: bool
  sample: false
loglines:
  description: List of logged messages from the module execution.
  returned: always
  type: list
  sample:
    - "INFO: LAS version check passed: 14.1-51.80"
    - "INFO: Got request package: ns_activation_request.tgz"
    - "INFO: License blob applied successfully"
output_file:
  description: Path to the generated offline license blob file on the control node.
  returned: on success
  type: str
  sample: offline_token_10.102.201.230_activation.blob.tgz
"""

import os
import shutil
import tempfile

from ansible.module_utils.basic import AnsibleModule, env_fallback

from ..module_utils.las_utils import (
    HAS_PARAMIKO,
    MPX14K_PEMS,
    NEW_API_MAPPING_FIPS,
    NEW_API_MAPPING_NS,
    NitroHelper,
    apply_license_blob_ns,
    check_if_new_api,
    check_ns_version,
    extract_lsguid,
    generate_offline_package,
    get_ent_name,
    get_offline_request_package,
)


# ---------------------------------------------------------------------------
# Module entry point
# ---------------------------------------------------------------------------


def main():
    argument_spec = dict(
        nsip=dict(required=True, type="str", fallback=(env_fallback, ["NETSCALER_NSIP"])),
        nitro_user=dict(required=True, type="str", no_log=True, fallback=(env_fallback, ["NETSCALER_NITRO_USER"])),
        nitro_pass=dict(required=True, type="str", no_log=True, fallback=(env_fallback, ["NETSCALER_NITRO_PASS"])),
        nitro_protocol=dict(type="str", choices=["http", "https"], default="https"),
        validate_certs=dict(type="bool", default=True, fallback=(env_fallback, ["NETSCALER_VALIDATE_CERTS"])),
        request_pem=dict(required=True, type="str"),
        request_ed=dict(required=True, type="str", choices=["Advanced", "Premium", "Standard"]),
        is_fips=dict(type="bool", default=False),
        las_secrets_json=dict(required=True, type="str"),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    if not HAS_PARAMIKO:
        module.fail_json(msg="The 'paramiko' Python library is required. Install it with: pip install paramiko")

    loglines = []
    result = dict(changed=False, failed=False, loglines=loglines)

    ip = module.params["nsip"]
    username = module.params["nitro_user"]
    password = module.params["nitro_pass"]
    request_pem = module.params["request_pem"]
    request_ed = module.params["request_ed"]
    is_fips = module.params["is_fips"]
    las_secrets_json = module.params["las_secrets_json"]
    if username != "nsroot":
        module.fail_json(msg="Only the 'nsroot' account is supported. Got: '{0}'".format(username), **result)

    if is_fips and request_pem in MPX14K_PEMS:
        module.fail_json(msg="MPX 14K devices (CNS_14xxx) do not require the is_fips argument", **result)

    if not os.path.isfile(las_secrets_json):
        module.fail_json(msg="las_secrets_json not found: {0}".format(las_secrets_json), **result)

    ent_name = get_ent_name(request_pem, request_ed, is_fips, loglines)
    if not ent_name:
        module.fail_json(
            msg="Could not resolve entitlement name for pem={0}, ed={1}, fips={2}".format(request_pem, request_ed, is_fips),
            **result,
        )

    nitro = NitroHelper(ip, module.params["nitro_protocol"], username, password, module.params["validate_certs"], loglines)

    # Version check and new_api flag
    ver_info = check_ns_version(nitro, is_fips, loglines)
    if not ver_info["las_ok"]:
        module.fail_json(
            msg="LAS version check failed: {0} (version={1}, build={2})".format(
                ver_info["reason"], ver_info["version"], ver_info["build"]
            ),
            **result,
        )
    loglines.append("INFO: LAS version check passed: {0}".format(ver_info["reason"]))

    release = ver_info["version"]
    build = ver_info["build"]
    mapping = NEW_API_MAPPING_FIPS if is_fips else NEW_API_MAPPING_NS
    new_api = check_if_new_api(mapping, release, build.split(".")[0], build.split(".")[-1])
    loglines.append("INFO: release={0} build={1} new_api={2}".format(release, build, new_api))

    # Get activation request package from device
    temp_dir = os.path.join(tempfile.mkdtemp(prefix="nslas_"), "")
    try:
        ns_file_name = get_offline_request_package(nitro, ip, username, password, temp_dir, new_api, loglines)
        if not ns_file_name:
            module.fail_json(msg="Failed to retrieve activation request package from device", **result)

        request_file = os.path.join(temp_dir, ns_file_name)
        loglines.append("INFO: Got request package: {0}".format(request_file))

        # Extract lsguid (retry once on parse failure)
        try:
            lsguid = extract_lsguid(request_file, loglines)
        except Exception as e:
            loglines.append("WARNING: First parse attempt failed ({0}), re-downloading package".format(str(e)))
            ns_file_name = get_offline_request_package(nitro, ip, username, password, temp_dir, new_api, loglines)
            if not ns_file_name:
                module.fail_json(msg="Re-download of activation request package failed", **result)
            request_file = os.path.join(temp_dir, ns_file_name)
            lsguid = extract_lsguid(request_file, loglines)

        # Generate offline token from LAS cloud
        output_file = "offline_token_{0}_activation.blob.tgz".format(ip)
        if generate_offline_package(lsguid, request_file, output_file, ent_name, las_secrets_json, loglines) is None:
            module.fail_json(msg="Failed to generate offline license token from LAS", **result)

        # Apply license blob to device
        apply_license_blob_ns(nitro, ip, username, password, output_file, loglines)

        result["changed"] = True
        result["output_file"] = output_file
        loglines.append("INFO: Successfully generated and applied offline license blob to {0}".format(ip))

    except Exception as e:
        loglines.append("ERROR: {0}".format(str(e)))
        module.fail_json(msg=str(e), **result)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
