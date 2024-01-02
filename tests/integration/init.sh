HERE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export NETSCALER_NSIP=$(cat "$HERE/integration_config.yml" | grep nsip | awk '{print $2}')
export NETSCALER_NITRO_USER=$(cat "$HERE/integration_config.yml" | grep nitro_user | awk '{print $2}')
export NETSCALER_NITRO_PASS=$(cat "$HERE/integration_config.yml" | grep nitro_pass | awk '{print $2}')
export NETSCALER_NITRO_PROTOCOL=$(cat "$HERE/integration_config.yml"| grep nitro_protocol | awk '{print $2}')
export NETSCALER_VALIDATE_CERTS=$(cat "$HERE/integration_config.yml" | grep validate_certs | awk '{print $2}')
export NETSCALER_SAVE_CONFIG=$(cat "$HERE/integration_config.yml" | grep save_config | awk '{print $2}')
