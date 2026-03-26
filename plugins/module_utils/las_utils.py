# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import os
import re
import subprocess  # nosec B404
import tempfile
import uuid

from ansible.module_utils.urls import open_url

try:
    import paramiko

    HAS_PARAMIKO = True
except ImportError:
    HAS_PARAMIKO = False

# ---------------------------------------------------------------------------
# NS PEM entitlement name mapping (MPX and VPX)
# ---------------------------------------------------------------------------

PEM_ENT_NAME_MAPPING = {
    "CNS_8905_SERVER": "MPX 8905",
    "CNS_8910_SERVER": "MPX 8910",
    "CNS_8920_SERVER": "MPX 8920",
    "CNS_8930_SERVER": "MPX 8930",
    "CNS_9110_SERVER": "MPX 9110",
    "CNS_9120_SERVER": "MPX 9120",
    "CNS_9130_SERVER": "MPX 9130",
    "CNS_5901_SERVER": "MPX 5901",
    "CNS_5905_SERVER": "MPX 5905",
    "CNS_5910_SERVER": "MPX 5910",
    "CNS_14020_SERVER": "FIPS MPX 14020",
    "CNS_14030_SERVER": "FIPS MPX 14030",
    "CNS_14060_SERVER": "FIPS MPX 14060",
    "CNS_14080_SERVER": "FIPS MPX 14080",
    "CNS_14500_SERVER": "FIPS MPX 14500",
    "CNS_16030_SERVER": "MPX 16030",
    "CNS_16040_SERVER": "MPX 16040",
    "CNS_16060_SERVER": "MPX 16060",
    "CNS_16120_SERVER": "MPX 16120",
    "CNS_16200_SERVER": "MPX 16200",
    "CNS_15120_SERVER": "MPX 15120 / 15120-50G",
    "CNS_26200_SERVER": "MPX 26200 / 26200-50S / 26200-100G Premium",
    "CNS_9205_SERVER": "MPX 9205",
    "CNS_9210_SERVER": "MPX 9210",
    "CNS_9220_SERVER": "MPX 9220",
    "CNS_9240_SERVER": "MPX 9240",
    "CNS_9260_SERVER": "MPX 9260",
    "CNS_9280_SERVER": "MPX 9280",
    "CNS_9295_SERVER": "MPX 9295",
    "CNS_9299_SERVER": "MPX 9299",
    "CNS_17020_SERVER": "MPX 17020",
    "CNS_17050_SERVER": "MPX 17050",
    "CNS_17100_SERVER": "MPX 17100",
    "CNS_17150_SERVER": "MPX 17150",
    "CNS_17200_SERVER": "MPX 17200",
    "CNS_17250_SERVER": "MPX 17250",
    "CNS_17300_SERVER": "MPX 17300",
    "CNS_17400_SERVER": "MPX 17400",
    "CNS_17500_SERVER": "MPX 17500",
    "CNS_V25000_SERVER": "VPX 25000",
    "CNS_V10000_SERVER": "VPX 10000",
    "CNS_V5000_SERVER": "VPX 5000",
    "CNS_V3000_SERVER": "VPX 3000",
    "CNS_V1000_SERVER": "VPX 1000",
    "CNS_V200_SERVER": "VPX 200",
    "CNS_V25_SERVER": "VPX 25",
    "CNS_V10_SERVER": "VPX 10",
}

# Minimum build versions at which the "new API" (use_hostname) is available
NEW_API_MAPPING_NS = {
    "13.1": {"major_high": "62", "61": "26", "62": "6"},
    "14.1": {"major_high": "68", "68": "3", "60": "55", "66": "32"},
    "release_high": "14.1",
}

NEW_API_MAPPING_FIPS = {
    "13.1": {"major_high": "37", "37": "256"},
    "14.1": {"major_high": "68", "68": "3", "60": "55", "66": "32"},
    "release_high": "14.1",
}

FIPS_VALID_PEMS = frozenset(
    (
        "CNS_8910_SERVER",
        "CNS_8920_SERVER",
        "CNS_9130_SERVER",
        "CNS_15120_SERVER",
        "CNS_V5000_SERVER",
        "CNS_V3000_SERVER",
        "CNS_V1000_SERVER",
        "CNS_V200_SERVER",
        "CNS_V25_SERVER",
    )
)

FIPS_MPX_PREMIUM_ONLY_PEMS = frozenset(
    ("CNS_8910_SERVER", "CNS_8920_SERVER", "CNS_9130_SERVER", "CNS_15120_SERVER")
)

MPX14K_PEMS = frozenset(
    (
        "CNS_14020_SERVER",
        "CNS_14030_SERVER",
        "CNS_14060_SERVER",
        "CNS_14080_SERVER",
        "CNS_14500_SERVER",
    )
)


# ---------------------------------------------------------------------------
# NITRO API helper
# ---------------------------------------------------------------------------


class NitroHelper:
    """Thin wrapper around open_url for NITRO API calls to the device."""

    def __init__(self, ip, protocol, user, password, validate_certs, loglines=None):
        self._ip = ip
        self._protocol = protocol
        self._validate_certs = validate_certs
        self._headers = {
            "Content-Type": "application/json",
            "X-NITRO-USER": user,
            "X-NITRO-PASS": password,
        }
        self._loglines = loglines if loglines is not None else []
        self.last_response_body = ""

    def _url(self, resource):
        return "{0}://{1}/nitro/v1/config/{2}".format(
            self._protocol, self._ip, resource
        )

    def get(self, resource):
        url = self._url(resource)
        self._loglines.append("DEBUG: NITRO GET {0}".format(url))
        try:
            resp = open_url(
                url,
                headers=self._headers,
                validate_certs=self._validate_certs,
                method="GET",
            )
            body = resp.read()
            self._loglines.append(
                "DEBUG: NITRO GET response: {0}".format(
                    body.decode("utf-8", errors="replace").strip()
                )
            )
            return json.loads(body) if body.strip() else {}
        except Exception as e:
            self._loglines.append("DEBUG: NITRO GET exception: {0}".format(str(e)))
            return {}

    def post(self, resource, payload, action=None):
        url = self._url(resource)
        if action:
            url += "?action={0}".format(action)
        self._loglines.append(
            "DEBUG: NITRO POST {0} request: {1}".format(url, json.dumps(payload))
        )
        try:
            resp = open_url(
                url,
                headers=self._headers,
                validate_certs=self._validate_certs,
                method="POST",
                data=json.dumps(payload).encode("utf-8"),
            )
            body = resp.read()
            self.last_response_body = body.decode("utf-8", errors="replace").strip()
            self._loglines.append(
                "DEBUG: NITRO POST response: {0!r}".format(self.last_response_body)
            )
            return json.loads(body) if body.strip() else {}
        except Exception as e:
            self._loglines.append("DEBUG: NITRO POST exception: {0}".format(str(e)))
            return {}


# ---------------------------------------------------------------------------
# LAS cloud API client
# ---------------------------------------------------------------------------


def build_multipart(fields, files):
    """Build a multipart/form-data body. Returns (body_bytes, content_type_header)."""
    boundary = uuid.uuid4().hex
    crlf = b"\r\n"
    body = b""
    for name, value in fields.items():
        body += b"--" + boundary.encode() + crlf
        body += (
            b'Content-Disposition: form-data; name="'
            + name.encode()
            + b'"'
            + crlf
            + crlf
        )
        body += value.encode() + crlf
    for name, (filename, file_content) in files.items():
        body += b"--" + boundary.encode() + crlf
        body += (
            b'Content-Disposition: form-data; name="'
            + name.encode()
            + b'"; filename="'
            + filename.encode()
            + b'"'
            + crlf
        )
        body += b"Content-Type: application/octet-stream" + crlf + crlf
        body += file_content + crlf
    body += b"--" + boundary.encode() + b"--" + crlf
    return body, "multipart/form-data; boundary={0}".format(boundary)


class LASClient:
    """Client for the LAS (License Activation Service) cloud API."""

    # Namespaced by effective user ID to avoid insecure shared /tmp file access.
    _BEARER_CACHE = os.path.join(
        tempfile.gettempdir(), "r56_bearer_{0}".format(os.geteuid())
    )

    def __init__(self, lsguid, secret_file, loglines=None):
        self.endpoint = "netscalerfixedbw"
        self.lsguid = lsguid
        with open(secret_file, "r") as f:
            x = json.load(f)
        self._ccid = x["ccid"]
        self._client_id = x["client"]
        self._client_secret = x["password"]
        self._base_url = x["las_endpoint"]
        self._cc_token_url = x["cc_endpoint"]
        self._loglines = loglines if loglines is not None else []

    def _post_json(self, url, headers, payload, log_payload=True):
        logged_payload = (
            payload
            if log_payload
            else {
                k: ("***" if k in ("clientSecret", "password") else v)
                for k, v in payload.items()
            }
        )
        self._loglines.append(
            "DEBUG: LAS POST {0} request: {1}".format(url, json.dumps(logged_payload))
        )
        try:
            resp = open_url(
                url,
                headers=headers,
                method="POST",
                data=json.dumps(payload).encode("utf-8"),
                timeout=60,
            )
            body = resp.read()
            self._loglines.append(
                "DEBUG: LAS POST response: {0}".format(
                    body.decode("utf-8", errors="replace").strip()
                )
            )
            return json.loads(body)
        except Exception as e:
            error_body = ""
            if hasattr(e, "read"):
                try:
                    error_body = e.read().decode("utf-8", errors="replace").strip()
                except Exception:
                    error_body = ""
            msg = "DEBUG: LAS POST exception: {0}".format(str(e))
            if error_body:
                msg += " response_body={0}".format(error_body)
            self._loglines.append(msg)
            raise

    def generate_bearer_token(self):
        headers = {"Content-Type": "application/json"}
        result = self._post_json(
            self._cc_token_url,
            headers,
            {"clientId": self._client_id, "clientSecret": self._client_secret},
            log_payload=False,
        )
        token = result.get("token", "")
        with open(self._BEARER_CACHE, "w") as f:
            f.write(token)
        return token or None

    def validate_bearer_cache(self):
        if not os.path.isfile(self._BEARER_CACHE):
            return None
        with open(self._BEARER_CACHE) as f:
            bearer = f.read().strip()
        if not bearer:
            return None
        url = "{0}/support/{1}/{2}/listls".format(
            self._base_url, self._ccid, self.endpoint
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        try:
            self._post_json(url, headers, {"ver": "1.0"})
            return bearer
        except Exception as e:
            self._loglines.append(
                "DEBUG: LAS bearer cache validation failed: {0}".format(str(e))
            )
            return None

    def get_fingerprint_for_lsguid(self, bearer, loglines):
        url = "{0}/support/{1}/{2}/listls".format(
            self._base_url, self._ccid, self.endpoint
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        try:
            ls_list = self._post_json(url, headers, {"ver": "1.0"})
            for ls in ls_list.get("lstlasactivatedls", []):
                if ls["lsguid"] == self.lsguid:
                    return ls.get("lsfingerprint", "") or ""
            return ""
        except Exception as e:
            loglines.append("ERROR: get_fingerprint_for_lsguid: {0}".format(str(e)))
            return "EXCEPTION ERROR"

    def get_customer_entitlements(self, bearer, platform, loglines):
        url = "{0}/{1}/netscalerfixedbw/customerentitlements".format(
            self._base_url, self._ccid
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        try:
            return self._post_json(url, headers, {"ver": "1.0", "platform": platform})
        except Exception as e:
            loglines.append(
                "ERROR: get_customer_entitlements platform={0}: {1}".format(
                    platform, str(e)
                )
            )
            return None

    def import_offline_activation_request(
        self, request_file, fingerprint, bearer, loglines
    ):
        url = "{0}/support/{1}/{2}/importofflineactivationrequest".format(
            self._base_url, self._ccid, self.endpoint
        )
        base_data = json.dumps({"ver": "1.0", "lsfingerprint": fingerprint})
        with open(request_file, "rb") as f:
            file_content = f.read()
        body, content_type = build_multipart(
            fields={"data": base_data},
            files={"file": (os.path.basename(request_file), file_content)},
        )
        headers = {
            "Authorization": "CWSAuth bearer={0}".format(bearer),
            "Content-Type": content_type,
        }
        loglines.append(
            "DEBUG: LAS POST {0} request: multipart/form-data file={1}".format(
                url, os.path.basename(request_file)
            )
        )
        try:
            resp = open_url(url, headers=headers, method="POST", data=body, timeout=120)
            raw = resp.read()
            loglines.append(
                "DEBUG: LAS POST response: {0}".format(
                    raw.decode("utf-8", errors="replace").strip()
                )
            )
            result = json.loads(raw)
            return result.get("importrequesttoken", "")
        except Exception as e:
            loglines.append(
                "ERROR: import_offline_activation_request: {0}".format(str(e))
            )
            return "EXCEPTION ERROR"

    def import_restricted_offline_activation_request(
        self, lsid, pubkey, bearer, loglines
    ):
        url = "{0}/support/{1}/{2}/importrestrictedofflineactivationrequest".format(
            self._base_url, self._ccid, self.endpoint
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        payload = {"ver": "1.0", "lsid": lsid, "pubkey": pubkey}
        try:
            result = self._post_json(url, headers, payload)
            return result.get("importrequesttoken", "")
        except Exception as e:
            loglines.append(
                "ERROR: import_restricted_offline_activation_request: {0}".format(
                    str(e)
                )
            )
            return "EXCEPTION ERROR"

    def generate_offline_activation(self, import_token, bearer, ent_name, loglines):
        url = "{0}/{1}/{2}/generateofflineactivation".format(
            self._base_url, self._ccid, self.endpoint
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        data = {
            "ver": "1.0",
            "importrequesttoken": import_token,
            "entitlementname": ent_name,
        }
        try:
            return self._post_json(url, headers, data)
        except Exception as e:
            loglines.append("ERROR: generate_offline_activation: {0}".format(str(e)))
            return "EXCEPTION ERROR"

    def get_blob_from_las(
        self, newactivationid, lsfingerprint, output_file, bearer, loglines
    ):
        url = "{0}/support/{1}/{2}/exportofflineactivationresponse".format(
            self._base_url, self._ccid, self.endpoint
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "CWSAuth bearer={0}".format(bearer),
        }
        payload = {
            "ver": "1.0",
            "lsfingerprint": lsfingerprint,
            "newactivationid": newactivationid,
        }
        loglines.append(
            "DEBUG: LAS POST {0} request: {1}".format(url, json.dumps(payload))
        )
        try:
            resp = open_url(
                url,
                headers=headers,
                method="POST",
                data=json.dumps(payload).encode("utf-8"),
                timeout=120,
            )
            blob = resp.read()
            loglines.append(
                "DEBUG: LAS POST response: <binary blob {0} bytes>".format(len(blob))
            )
            with open(output_file, "wb") as f:
                f.write(blob)
            return "SUCCESS"
        except Exception as e:
            loglines.append("ERROR: get_blob_from_las: {0}".format(str(e)))
            return "EXCEPTION ERROR"


# ---------------------------------------------------------------------------
# SFTP helpers
# ---------------------------------------------------------------------------


def sftp_get(ip, username, password, remote_path, local_path, loglines):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # nosec B507
    sftp = None
    try:
        ssh.connect(ip, username=username, password=password)
        sftp = ssh.open_sftp()
        sftp.get(remote_path, local_path)
        loglines.append(
            "INFO: SFTP downloaded {0} -> {1}".format(remote_path, local_path)
        )
    except Exception as e:
        raise RuntimeError(
            "SFTP get failed ({0} -> {1}): {2}".format(remote_path, local_path, str(e))
        )
    finally:
        if sftp:
            sftp.close()
        ssh.close()


def sftp_put(ip, username, password, local_path, remote_path, loglines):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # nosec B507
    sftp = None
    try:
        ssh.connect(ip, port=22, username=username, password=password)
        sftp = ssh.open_sftp()
        sftp.put(local_path, remote_path)
        loglines.append(
            "INFO: SFTP uploaded {0} -> {1}".format(local_path, remote_path)
        )
    except Exception as e:
        raise RuntimeError(
            "SFTP put failed ({0} -> {1}): {2}".format(local_path, remote_path, str(e))
        )
    finally:
        if sftp:
            sftp.close()
        ssh.close()


# ---------------------------------------------------------------------------
# Version detection
# ---------------------------------------------------------------------------


def is_build_ge(a_major, a_minor, b_major, b_minor):
    return (a_major > b_major) or (a_major == b_major and a_minor >= b_minor)


def check_ns_version(nitro, is_fips, loglines):
    """Query NS version via NITRO and check LAS compatibility. Returns dict with version/build/las_ok/reason."""
    o = nitro.get("nsversion")
    ns = o.get("nsversion", {})
    if not isinstance(ns, dict):
        return {
            "version": None,
            "build": None,
            "las_ok": False,
            "reason": "Missing nsversion in NITRO response",
        }
    ver_str = ns.get("version", "")
    if not ver_str:
        return {
            "version": None,
            "build": None,
            "las_ok": False,
            "reason": "Empty version field in nsversion",
        }
    loglines.append("INFO: NS version string: {0}".format(ver_str))

    version_match = re.search(r"NS(\d+\.\d+)", ver_str)
    if not version_match:
        return {
            "version": None,
            "build": None,
            "las_ok": False,
            "reason": "Unable to parse version from: {0}".format(ver_str),
        }
    version = version_match.group(1)

    build_match = re.search(r"Build\s+(\d+)\.(\d+)", ver_str)
    if not build_match:
        return {
            "version": version,
            "build": None,
            "las_ok": False,
            "reason": "Unable to parse build from: {0}".format(ver_str),
        }
    major_build = int(build_match.group(1))
    minor_build = int(build_match.group(2))

    las_ok = False
    reason = ""
    if version == "14.1":
        las_ok = is_build_ge(major_build, minor_build, 51, 80)
        reason = "Minimum required build is 14.1-51.80"
    elif version == "13.1":
        if is_fips:
            las_ok = is_build_ge(major_build, minor_build, 37, 247)
            reason = (
                "Minimum required build is 13.1-37.247 (FIPS)"
                if not las_ok
                else "Meets minimum build 13.1-37.247 (FIPS)"
            )
        else:
            las_ok = is_build_ge(major_build, minor_build, 60, 29)
            reason = (
                "Minimum required build is 13.1-60.29"
                if not las_ok
                else "Meets minimum build 13.1-60.29"
            )
    else:
        reason = "Unsupported version {0} for LAS offline licensing".format(version)

    return {
        "version": version,
        "build": "{0}.{1}".format(major_build, minor_build),
        "las_ok": las_ok,
        "reason": reason,
    }


def check_if_new_api(mapping, release, major, minor):
    rel_high = mapping.get("release_high")
    if not rel_high:
        return False
    if release > rel_high:
        return True
    build_map = mapping.get(release)
    if not build_map:
        return False
    maj_high = build_map.get("major_high")
    if not maj_high:
        return False
    if int(major) > int(maj_high):
        return True
    if major in build_map:
        min_minor = build_map[major]
        pad = len(minor) - len(min_minor)
        min_minor = min_minor + "0" * pad
        return int(minor) >= int(min_minor)
    return False


# ---------------------------------------------------------------------------
# Activation request package retrieval
# ---------------------------------------------------------------------------


def get_offline_request_package(
    nitro, ip, username, password, local_dir, new_api, loglines
):
    """Trigger NITRO to generate the NS offline activation request tgz, then SFTP it to local_dir."""
    resource = (
        "nslicenseactivationdata?args=usehostname:true"
        if new_api
        else "nslicenseactivationdata"
    )
    o = nitro.get(resource)
    src_file = (o.get("nslicenseactivationdata") or {}).get("filename", "")

    if not src_file:
        loglines.append(
            "ERROR: Could not get package filename from NITRO response: {0}".format(o)
        )
        return ""

    local_path = os.path.join(local_dir, src_file)
    sftp_get(
        ip, username, password, "/nsconfig/license/" + src_file, local_path, loglines
    )
    return src_file


# ---------------------------------------------------------------------------
# Extract lsguid from the NS activation request tgz
# ---------------------------------------------------------------------------


def extract_request_fields(file_path, loglines):
    """Extract lsguid, lsid, and pubkey from the NS offline activation request tgz in one pass."""
    dest_dir = os.path.dirname(file_path)
    # Validate that file_path is within dest_dir to guard against path traversal.
    real_file_path = os.path.realpath(file_path)
    real_dest_dir = os.path.realpath(dest_dir)
    if not real_file_path.startswith(real_dest_dir + os.sep):
        raise RuntimeError(
            "Invalid file path outside temp directory: {0}".format(file_path)
        )
    json_file = "ns_offline_activation_request.json"
    # shell=False ensures no shell metacharacter interpretation; all args are controlled internally.
    cmd = [
        "tar",
        "-xvf",
        file_path,
        "--no-same-owner",
        "--no-same-permissions",
        "--no-overwrite-dir",
        "-C",
        dest_dir,
    ]
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False
    )  # nosec B603
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError("tar extraction failed: {0}".format(stderr))

    json_path = os.path.join(dest_dir, json_file)
    if not os.path.exists(json_path):
        raise RuntimeError("{0} not found after tar extraction".format(json_path))
    if os.path.getsize(json_path) == 0:
        raise RuntimeError("{0} is empty after tar extraction".format(json_path))

    with open(json_path, "r") as f:
        content = f.read().strip()
    if not content:
        raise RuntimeError("{0} contains no data".format(json_path))
    data = json.loads(content)

    try:
        os.remove(json_path)
    except Exception as e:
        loglines.append(
            "DEBUG: Could not remove temp file {0}: {1}".format(json_path, str(e))
        )
    try:
        os.remove(os.path.join(dest_dir, "lasData.tgz"))
    except Exception as e:
        loglines.append(
            "DEBUG: Could not remove temp file lasData.tgz: {0}".format(str(e))
        )

    lsguid = data["lsguid"]
    inner = data.get("data", {})
    lsid = inner["lsid"]
    pubkey = inner["pubkey"]
    loglines.append("INFO: Extracted lsguid: {0}".format(lsguid))
    loglines.append("INFO: Extracted lsid: {0}".format(lsid))
    return lsguid, lsid, pubkey


# ---------------------------------------------------------------------------
# License blob application
# ---------------------------------------------------------------------------


def apply_license_blob_ns(nitro, ip, username, password, fname, loglines):
    sftp_put(ip, username, password, fname, "/nsconfig/license/" + fname, loglines)
    payload = {
        "params": {"action": "apply", "warning": "YES"},
        "nslaslicense": {
            "filename": fname,
            "filelocation": "/nsconfig/license",
            "fixedbandwidth": True,
        },
    }
    r = nitro.post("nslaslicense", payload, action="apply")
    if r.get("errorcode") == 1043:
        loglines.append("WARNING: Invalid license blob (NITRO errorcode 1043)")
    loglines.append("INFO: Sending warm reboot")
    nitro.post("reboot", {"params": {"warning": "YES"}, "reboot": {"warm": True}})


# ---------------------------------------------------------------------------
# Entitlement name resolution
# ---------------------------------------------------------------------------


def get_ent_name(request_pem, request_ed, is_fips, loglines):
    base_ent = PEM_ENT_NAME_MAPPING.get(request_pem)
    if not base_ent:
        loglines.append(
            "ERROR: PEM {0} not found in entitlement mapping".format(request_pem)
        )
        return None

    if is_fips:
        if request_pem not in FIPS_VALID_PEMS:
            loglines.append("ERROR: FIPS not supported for PEM {0}".format(request_pem))
            return None
        if request_pem in FIPS_MPX_PREMIUM_ONLY_PEMS and request_ed != "Premium":
            loglines.append("ERROR: FIPS MPX devices only support the Premium edition")
            return None
        base_ent = (
            "FIPS MPX 15120-50G"
            if request_pem == "CNS_15120_SERVER"
            else "FIPS " + base_ent
        )

    if request_ed not in ("Advanced", "Standard", "Premium"):
        loglines.append(
            "ERROR: Invalid edition {0} for PEM {1}".format(request_ed, request_pem)
        )
        return None

    return base_ent + " " + request_ed


# ---------------------------------------------------------------------------
# Full offline token generation workflow
# ---------------------------------------------------------------------------


def generate_offline_package(
    lsguid,
    request_file,
    output_file,
    ent_name,
    secret_file,
    loglines,
    restricted_mode=False,
    lsid=None,
    pubkey=None,
):
    client = LASClient(lsguid, secret_file, loglines=loglines)

    bearer = client.validate_bearer_cache()
    if not bearer:
        bearer = client.generate_bearer_token()
        loglines.append("INFO: New bearer token generated")
    else:
        loglines.append("INFO: Using cached bearer token")

    if not bearer:
        loglines.append("ERROR: Failed to obtain bearer token from LAS")
        return None

    if restricted_mode:
        import_token = client.import_restricted_offline_activation_request(
            lsid, pubkey, bearer, loglines
        )
    else:
        fingerprint = client.get_fingerprint_for_lsguid(bearer, loglines)
        if "ERROR" in str(fingerprint):
            loglines.append(
                "ERROR: Failed to get device fingerprint for lsguid {0}".format(lsguid)
            )
            return None
        loglines.append("INFO: Device fingerprint in LAS: {0!r}".format(fingerprint))
        import_token = client.import_offline_activation_request(
            request_file, fingerprint, bearer, loglines
        )

    if not import_token or "ERROR" in import_token:
        loglines.append("ERROR: Failed to import offline activation request")
        return None
    loglines.append("INFO: Import token: {0}".format(import_token))

    gen_resp = client.generate_offline_activation(
        import_token, bearer, ent_name, loglines
    )
    if not isinstance(gen_resp, dict):
        loglines.append("ERROR: Failed to generate offline activation from LAS")
        return None
    loglines.append(
        "INFO: New activation ID: {0}".format(gen_resp.get("newactivationid"))
    )

    if (
        client.get_blob_from_las(
            gen_resp["newactivationid"],
            gen_resp["lsfingerprint"],
            output_file,
            bearer,
            loglines,
        )
        != "SUCCESS"
    ):
        loglines.append("ERROR: Failed to retrieve license blob from LAS")
        return None

    loglines.append("INFO: Created license blob file: {0}".format(output_file))
    return output_file
