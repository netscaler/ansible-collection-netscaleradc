from collections import OrderedDict
import copy

from BaseIntegrationModule import BaseIntegrationModule

ENTITY_NAME = 'citrix_adc_lb_monitor'

# PREREQUISITES/Testbed
def get_testbed_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    testbed_data = []
    #TODO: test bed data here
    return testbed_data


def get_input_data(test_type='citrix_adc_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    # For Submodule 'lb_monitor_citrix_aac'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_citrix_aac')
    setup_data = OrderedDict(
        [
            ('state', 'present'),
            ('monitorname', 'lb-monitor-citrix-aac'),
            ('type', 'CITRIX-AAC-LAS'),
            ('lasversion', 7.1),
            ('logonpointname', 'user'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-aac'),
            ('type', 'CITRIX-AAC-LAS'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_citrix_ag'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_citrix_ag')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-ag'),
            ('state', 'present'),
            ('type', 'CITRIX-AG'),
            ('username', 'user1'),
            ('password', 'password1'),
            ('secondarypassword', 'password2'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-ag'),
            ('type', 'CITRIX-AG'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_citrix_web_interface'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_citrix_web_interface')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-web-interface'),
            ('state', 'present'),
            ('type', 'CITRIX-WEB-INTERFACE'),
            ('sitepath','hello/'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-web-interface'),
            ('state', 'absent'),
            ('type', 'CITRIX-WEB-INTERFACE'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_citrix_xd_ddc'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_citrix_xd_ddc')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-xd-ddc'),
            ('state', 'present'),
            ('type', 'CITRIX-XD-DDC'),
            ('validatecred','no'),
            ('domain','somedomain.com'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-xd-ddc'),
            ('type', 'CITRIX-XD-DDC'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_citrix_xml_service'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_citrix_xml_service')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-xml-service'),
            ('state', 'present'),
            ('type', 'CITRIX-XML-SERVICE'),
            ('application','app'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-citrix-xml-service'),
            ('state', 'absent'),
            ('type', 'CITRIX-XML-SERVICE'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_diameter'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_diameter')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-diameter'),
            ('state', 'present'),
            ('type', 'DIAMETER'),
            ('originhost','origin.host'),
            ('originrealm','some.realm'),
            ('hostipaddress','192.169.1.1'),
            ('vendorid',20),
            ('productname','someproduct'),
            ('firmwarerevision',10),
            ('authapplicationid',["'100'", "'200'"]),
            ('inbandsecurityid','NO_INBAND_SECURITY'),
            ('supportedvendorids',["'10'","'20'"]),
            ('vendorspecificvendorid',10),
            ('vendorspecificauthapplicationids',["'11'","'22'"]),
            ('vendorspecificacctapplicationids',["'12'","'23'"]),
            ('acctapplicationid',["'1'","'2'"]),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-diameter'),
            ('state', 'absent'),
            ('type', 'DIAMETER'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_dns'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_dns')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-dns-tcp'),
            ('state', 'present'),
            ('type', 'DNS-TCP'),
            ('query','example.com'),
            ('querytype','Address'),
            ('ipaddress',["192.168.1.1","192.168.1.2"]),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-dns-tcp'),
            ('state', 'absent'),
            ('type', 'DNS-TCP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_ftp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_ftp')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-ftp'),
            ('state', 'present'),
            ('type', 'FTP-EXTENDED'),
            ('filename', 'somefile.txt'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-ftp'),
            ('state', 'absent'),
            ('type', 'FTP-EXTENDED'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_http'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_http')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-http'),
            ('state', 'present'),
            ('type', 'HTTP'),
            ('trofscode',500),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-http'),
            ('state', 'absent'),
            ('type', 'HTTP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    # For Submodule 'lb_monitor_http_ecv'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_http_ecv')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-http-ecv'),
            ('state', 'present'),
            ('type', 'HTTP-ECV'),
            ('trofsstring', 'somestring'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-http-ecv'),
            ('state', 'absent'),
            ('type', 'HTTP-ECV'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_http_inline'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_http_inline')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-1'),
            ('state', 'present'),
            ('type', 'HTTP-INLINE'),
            ('action', 'DOWN'),
            ('respcode', ["'200'","'203'"]),
            ('httprequest', 'HEAD /file.html'),
            ('customheaders', 'HEADER_CUSTOM: NONE\r\n'),
        ]
    )
    
    update_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-1'),
            ('state', 'present'),
            ('type', 'HTTP-INLINE'),
            ('action', 'DOWN'),
            ('respcode', ["200-201"]),
            ('httprequest', 'HEAD /new_file.html'),
            ('customheaders', 'HEADER_CUSTOM: NONE\r\n'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-1'),
            ('state', 'absent'),
            ('type', 'HTTP-INLINE'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('update', update_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_ldap'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_ldap')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-ldap'),
            ('state', 'present'),
            ('type', 'LDAP'),
            ('basedn', 'example.com'),
            ('binddn', 'example.com'),
            ('filter', 'somefilter'),
            ('attribute', 'cn'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-ldap'),
            ('state', 'absent'),
            ('type', 'LDAP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_load'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_load')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-load'),
            ('state', 'present'),
            ('type', 'LOAD'),
            ('snmpversion', 'V1'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-load'),
            ('state', 'absent'),
            ('type', 'LOAD'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_nntp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_nntp')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-nntp'),
            ('state', 'present'),
            ('type', 'NNTP'),
            ('group', 'somegroup.nntp'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-nntp'),
            ('state', 'absent'),
            ('type', 'NNTP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_radius'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_radius')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-radius'),
            ('state', 'present'),
            ('type', 'RADIUS'),
            ('username', 'someuser'),
            ('password', 'somepass'),
            ('radkey', 'somekey'),
            ('radnasid', 'someid'),
            ('radnasip', '192.168.1.2'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-radius'),
            ('state', 'absent'),
            ('type', 'RADIUS'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_radius_accounting'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_radius_accounting')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-radius-accounting'),
            ('state', 'present'),
            ('type', 'RADIUS_ACCOUNTING'),
            ('username', 'someuser'),
            ('password', 'somepass'),
            ('radkey', 'somekey'),
            ('radaccounttype', 10),
            ('radframedip', '192.168.1.1'),
            ('radapn', 'someapn'),
            ('radmsisdn', 'someisdn'),
            ('radaccountsession', 'sessionid'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-radius-accounting'),
            ('state', 'absent'),
            ('type', 'RADIUS_ACCOUNTING'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_rtsp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_rtsp')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-rtsp'),
            ('state', 'present'),
            ('type', 'RTSP'),
            ('rtsprequest', 'OPTIONS'),
            ('deviation', 100),
            ('units1', 'MSEC'),
            ('interval', 5),
            ('units3', 'SEC'),
            ('resptimeout', 10),
            ('units4', 'MSEC'),
            ('resptimeoutthresh', 10),
            ('retries', 5),
            ('failureretries', 3),
            ('alertretries', 2),
            ('successretries', 4),
            ('downtime', 60),
            ('units2', 'MSEC'),
            ('destip', '10.10.10.10'),
            ('destport', 1111),
            ('reverse', 'yes'),
            ('transparent', 'yes'),
            ('iptunnel', 'no'),
            ('tos', 'yes'),
            ('tosid', 20),
            ('secure', 'no'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-rtsp'),
            ('type', 'RTSP'),
            ('state', 'absent'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_sip'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_sip')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-2'),
            ('state', 'present'),
            ('type', 'SIP-UDP'),
            ('customheaders', 'HEADER_CUSTOM: NONE\r\n'),
            ('maxforwards', 5),
            ('sipmethod', 'REGISTER'),
            ('sipuri', 'sip:sip:test'),
            ('sipreguri', 'sip:sip:register'),
            ('lrtm', 'disabled'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-2'),
            ('state', 'absent'),
            ('type', 'SIP-UDP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_snmp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_snmp')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-snmp'),
            ('state', 'present'),
            ('type', 'SNMP'),
            ('Snmpoid', 'some.id'),
            ('snmpcommunity', 'some.community'),
            ('snmpthreshold', 'threshold'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-snmp'),
            ('state', 'absent'),
            ('type', 'SNMP'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_storefront'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_storefront')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-storefront'),
            ('state', 'present'),
            ('type', 'STOREFRONT'),
            ('storename', 'store'),
            ('storefrontacctservice', 'yes'),
            ('storefrontcheckbackendservices', 'yes'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-storefront'),
            ('state', 'absent'),
            ('type', 'STOREFRONT'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_tcp'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_tcp')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-tcp-ecv'),
            ('state', 'present'),
            ('type', 'TCP-ECV'),
            ('send', 'sendstring'),
            ('recv', 'recvstring'),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-tcp-ecv'),
            ('state', 'absent'),
            ('type', 'TCP-ECV'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    # For Submodule 'lb_monitor_user'
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'lb_monitor_user')
    setup_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-user'),
            ('state', 'present'),
            ('type', 'USER'),
            ('scriptname', 'myscript.sh'),
            ('dispatcherip', '10.10.10.10'),
            ('dispatcherport', 22),
        ]
    )
    
    remove_data = OrderedDict(
        [
            ('monitorname', 'lb-monitor-user'),
            ('state', 'absent'),
            ('type', 'USER'),
        ]
    )
    
    submodObj.add_operation('setup', setup_data)
    submodObj.add_operation('remove', remove_data)
    
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    return input_data
