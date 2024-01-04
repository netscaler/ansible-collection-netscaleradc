#!/usr/bin/env bash

HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

NETSCALER_NSIP=$(grep nsip "$HERE/integration_config.yml" | awk '{print $2}')
NETSCALER_NITRO_USER=$(grep nitro_user "$HERE/integration_config.yml" | awk '{print $2}')
NETSCALER_NITRO_PASS=$(grep nitro_pass "$HERE/integration_config.yml" | awk '{print $2}')
NETSCALER_NITRO_PROTOCOL=$(grep nitro_protocol "$HERE/integration_config.yml" | awk '{print $2}')
NETSCALER_VALIDATE_CERTS=$(grep validate_certs "$HERE/integration_config.yml" | awk '{print $2}')
NETSCALER_SAVE_CONFIG=$(grep save_config "$HERE/integration_config.yml" | awk '{print $2}')

export NETSCALER_NSIP
export NETSCALER_NITRO_USER
export NETSCALER_NITRO_PASS
export NETSCALER_NITRO_PROTOCOL
export NETSCALER_VALIDATE_CERTS
export NETSCALER_SAVE_CONFIG
