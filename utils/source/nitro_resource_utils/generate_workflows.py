import os
import json
import argparse
import pyaml
from collections import OrderedDict as od

HERE = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


def create_basic_section_workflows(args, workflows):
    workflows['server'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'server'),
        ('primary_id_attribute', 'name'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'server')),
    ])

    workflows['service'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'service'),
        ('primary_id_attribute', 'name'),
        ('resource_missing_errorcode', '344'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'service')),
    ])

    workflows['servicegroup'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'servicegroup'),
        ('primary_id_attribute', 'servicegroupname'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'servicegroup')),
    ])

    workflows['service_lbmonitor_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'service_lbmonitor_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'service_lbmonitor_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'service_lbmonitor_binding')[0]),
    ])

    workflows['servicegroup_lbmonitor_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'servicegroup_lbmonitor_binding'),
        ('bound_resource_missing_errorcode', '351'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'servicegroup_lbmonitor_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'servicegroup_lbmonitor_binding')[0]),
    ])

def create_lb_section_workflows(args, workflows):

    workflows['lbgroup'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'lbgroup'),
        ('primary_id_attribute', 'name'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'lbgroup')),
    ])

    workflows['lbgroup_lbvserver_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbgroup_lbvserver_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbgroup_lbvserver_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbgroup_lbvserver_binding')[0]),
    ])

    workflows['lbvserver'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'lbvserver'),
        ('primary_id_attribute', 'name'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'lbvserver')),
    ])

    workflows['lbvserver_analyticsprofile_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_analyticsprofile_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_analyticsprofile_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_analyticsprofile_binding')[0]),
    ])

    workflows['lbvserver_appflowpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_appflowpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_appflowpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_appflowpolicy_binding')[0]),
    ])

    workflows['lbvserver_appfwpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_appfwpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_appfwpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_appfwpolicy_binding')[0]),
    ])

    workflows['lbvserver_appqoepolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_appqoepolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_appqoepolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_appqoepolicy_binding')[0]),
    ])

    workflows['lbvserver_auditnslogpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_auditnslogpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_auditnslogpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_auditnslogpolicy_binding')[0]),
    ])

    workflows['lbvserver_auditsyslogpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_auditsyslogpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_auditsyslogpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_auditsyslogpolicy_binding')[0]),
    ])

    workflows['lbvserver_authorizationpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_authorizationpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_authorizationpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_authorizationpolicy_binding')[0]),
    ])

    workflows['lbvserver_cachepolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_cachepolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_cachepolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_cachepolicy_binding')[0]),
    ])

    workflows['lbvserver_capolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_capolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_capolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_capolicy_binding')[0]),
    ])

    workflows['lbvserver_cmppolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_cmppolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_cmppolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_cmppolicy_binding')[0]),
    ])

    workflows['lbvserver_csvserver_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_csvserver_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_csvserver_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_csvserver_binding')[0]),
    ])

    workflows['lbvserver_dnspolicy64_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_dnspolicy64_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_dnspolicy64_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_dnspolicy64_binding')[0]),
    ])

    workflows['lbvserver_feopolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_feopolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_feopolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_feopolicy_binding')[0]),
    ])

    workflows['lbvserver_filterpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_filterpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_filterpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_filterpolicy_binding')[0]),
    ])

    workflows['lbvserver_pqpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_pqpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_pqpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_pqpolicy_binding')[0]),
    ])

    workflows['lbvserver_responderpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_responderpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_responderpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_responderpolicy_binding')[0]),
    ])

    workflows['lbvserver_rewritepolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_rewritepolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_rewritepolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_rewritepolicy_binding')[0]),
    ])

    workflows['lbvserver_scpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_scpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_scpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_scpolicy_binding')[0]),
    ])

    workflows['lbvserver_servicegroupmember_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_servicegroupmember_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_servicegroupmember_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_servicegroupmember_binding')[0]),
    ])

    workflows['lbvserver_servicegroup_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_servicegroup_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_servicegroup_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_servicegroup_binding')[0]),
    ])

    workflows['lbvserver_service_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_service_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_service_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_service_binding')[0]),
    ])

    workflows['lbvserver_spilloverpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_spilloverpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_spilloverpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_spilloverpolicy_binding')[0]),
    ])

    workflows['lbvserver_transformpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_transformpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_transformpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_transformpolicy_binding')[0]),
    ])

    workflows['lbvserver_contentinspectionpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_contentinspectionpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_contentinspectionpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_contentinspectionpolicy_binding')[0]),
    ])

    workflows['lbvserver_videooptimizationdetectionpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_videooptimizationdetectionpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_videooptimizationdetectionpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_videooptimizationdetectionpolicy_binding')[0]),
    ])

    workflows['lbvserver_videooptimizationpacingpolicy_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbvserver_videooptimizationpacingpolicy_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbvserver_videooptimizationpacingpolicy_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbvserver_videooptimizationpacingpolicy_binding')[0]),
    ])


    workflows['lbmetrictable'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'lbmetrictable'),
        ('primary_id_attribute', 'metrictable'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'lbmetrictable')),
    ])

    workflows['lbmetrictable_metric_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbmetrictable_metric_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbmetrictable_metric_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbmetrictable_metric_binding')[0]),
    ])

    workflows['lbmonitor'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'lbmonitor'),
        ('primary_id_attribute', 'monitorname'),
        ('resource_missing_errorcode', '258'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'lbmonitor')),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbmonitor')[0]),
    ])

    workflows['lbmonitor_metric_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbmonitor_metric_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbmonitor_metric_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbmonitor_metric_binding')[0]),
    ])

    workflows['lbmonitor_sslcertkey_binding'] = od([
        ('lifecycle', 'binding'),
        ('endpoint', 'lbmonitor_sslcertkey_binding'),
        ('bound_resource_missing_errorcode', '258'),
        ('primary_id_attribute', _get_bindig_id_attributes(args, 'lbmonitor_sslcertkey_binding')[1]),
        ('delete_id_attributes', _get_bindig_id_attributes(args, 'lbmonitor_sslcertkey_binding')[0]),
    ])

    workflows['lbprofile'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'lbprofile'),
        ('primary_id_attribute', 'lbprofilename'),
        ('resource_missing_errorcode', '3574'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'lbprofile')),
    ])

    workflows['lbroute'] = od([
        ('lifecycle', 'non_updateable_object'),
        ('endpoint', 'lbroute'),
        ('primary_id_attribute', 'network'),
        ('resource_missing_errorcode', '258'),
        ('delete_id_attributes', _filter_delete_id_attributes(args, 'lbroute', ['network'])),
    ])

    workflows['lbroute6'] = od([
        ('lifecycle', 'non_updateable_object'),
        ('endpoint', 'lbroute6'),
        ('primary_id_attribute', 'network'),
        ('resource_missing_errorcode', '258'),
        ('delete_id_attributes', _filter_delete_id_attributes(args, 'lbroute6', ['network'])),
    ])


def create_spillover_section_workflows(args, workflows):
    workflows['spilloverpolicy'] = od([
        ('lifecycle', 'object'),
        ('endpoint', 'spilloverpolicy'),
        ('primary_id_attribute', 'name'),
        ('resource_missing_errorcode', '2054'),
        ('allow_recreate', 'true'),
        ('non_updateable_attributes', _get_non_updateable_attributes(args, 'spilloverpolicy')),
    ])

def get_workflows(args):
    workflows = od()

    create_basic_section_workflows(args, workflows)
    create_lb_section_workflows(args, workflows)

    create_spillover_section_workflows(args, workflows)

    return { 'workflow': workflows }

def _filter_delete_id_attributes(args, nitro_object, exclude_attributes):
    # This for objects where we cannot find the primary id by the is_get_id attribute
    # So we define it explicitly
    delete_ids = _get_bindig_id_attributes(args, nitro_object, primary_required=False)[0]
    for excluded in exclude_attributes:
        if excluded not in delete_ids:
            raise Exception('Missing excluded attribute "%s"' % excluded)
        delete_ids.remove(excluded)
    return delete_ids

def _get_non_updateable_attributes(args, nitro_object):

    for item in os.listdir(args.nitro_api_defines):
        item_path = os.path.join(args.nitro_api_defines, item)
        if item == '%s.json' % nitro_object:
            with open(item_path, 'r') as fh:
                json_data = json.load(fh)
            non_updateables = []
            for option in json_data:
                if not option['is_updateable']:
                    non_updateables.append(option['option_name'])
            return non_updateables
    else:
        raise Exception('Cannot find json source for %s' % nitro_object)

def _get_bindig_id_attributes(args, nitro_object, primary_required=True):

    for item in os.listdir(args.nitro_api_defines):
        item_path = os.path.join(args.nitro_api_defines, item)
        if item == '%s.json' % nitro_object:
            with open(item_path, 'r') as fh:
                json_data = json.load(fh)
            delete_ids = []
            primary_ids = []
            for option in json_data:
                if option['is_get_id']:
                    primary_ids.append(option['option_name'])
                if option['is_delete_id'] and not option['is_get_id']:
                    delete_ids.append(option['option_name'])
            if len(primary_ids) != 1:
                if primary_required:
                    raise Exception('Found inappropriate primary ids %s' % primary_ids)
                else:
                    return delete_ids, None

            # Fallthrough
            return delete_ids, primary_ids[0]

    else:
        raise Exception('Cannot find json source for %s' % nitro_object)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nitro-api-defines', required=True)
    parser.add_argument('--output', required=True)
    
    args = parser.parse_args()
    workflows = get_workflows(args)
    with open(args.output, 'w') as fh:
        pyaml.dump(workflows, fh, vspacing=[1,1])

if __name__ == '__main__':
    main()
