#!/usr/bin/env bash

set -e

modules=( \
netscaler_cs_action \
netscaler_cs_policy \
netscaler_cs_vserver \
netscaler_gslb_service \
netscaler_gslb_site \
netscaler_gslb_vserver \
netscaler_lb_monitor \
netscaler_lb_vserver \
netscaler_nitro_request \
netscaler_save_config \
netscaler_server \
netscaler_servicegroup \
netscaler_service \
netscaler_ssl_certkey \
)

HERE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Run unit tests
pversions=("2.7" "3.5")
for module in "${modules[@]}" ; do
    ${HERE_DIR}/run_units.sh $module
done
