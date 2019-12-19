HERE=$(realpath $( dirname ${BASH_SOURCE[0]}))

cd $HERE/source/nitro_resource_utils

echo $PWD
python generate_workflows.py \
--nitro-api-defines "../nitro_api_defines/mana_41_28" \
--output ./workflows.yaml
