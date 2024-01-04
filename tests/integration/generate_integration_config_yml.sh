#!/usr/bin/env bash

# This script generates the integration_config.yml file used by the integration tests.
# This is used during github-actions.
# During github-actions, the NetScaler CPX is running as a docker container.
# The integration tests are run against the NetScaler CPX.
# NetScaler CPX API credentials are generated and stored in the integration_config.yml file.
# `ansible-test integration` uses the integration_config.yml file to run the integration tests.

NS_NITRO_PORT=$(docker port netscaler 9080 | cut -d ':' -f2)
NETSCALER_NSIP=localhost:$NS_NITRO_PORT
NETSCALER_NITRO_PASS=$(docker exec netscaler cat /var/random_id)
NETSCALER_NITRO_USER=nsroot
NETSCALER_NITRO_PROTOCOL=http
NETSCALER_VALIDATE_CERTS=false

HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

integration_config_yml_path="$HERE/integration_config.yml"

cat << EOF > "$integration_config_yml_path"
---
nsip: $NETSCALER_NSIP
nitro_user: $NETSCALER_NITRO_USER
nitro_pass: $NETSCALER_NITRO_PASS
nitro_protocol: $NETSCALER_NITRO_PROTOCOL
validate_certs: $NETSCALER_VALIDATE_CERTS
save_config: false
EOF
