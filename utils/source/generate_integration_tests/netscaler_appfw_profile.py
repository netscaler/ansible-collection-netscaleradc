from collections import OrderedDict
import copy
import re

import helpers

from BaseIntegrationModule import BaseIntegrationModule
ENTITY_NAME = 'netscaler_appfw_profile'

def get_testbed_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    testbed_data = []
    #TODO:test bed data here
    return testbed_data


def get_input_data(test_type='netscaler_direct_calls', ns_version='12.1'):
    input_data = OrderedDict()
    ####################################
    # All possible attributes together #
    ####################################
    
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'all_attributes')
    
    attributes = OrderedDict(
        [
            ('state',  'present'),
    
            ('name',  'profile_integration_test'),
            #('defaults',  'basic'),
            ('starturlaction',  ['block', 'log', 'stats']),
            ('contenttypeaction',  ['block', 'learn']),
            ('inspectcontenttypes',  ['application/x-www-form-urlencoded', 'text/x-gwt-rpc']),
            ('starturlclosure',  'off'),
            ('denyurlaction',  ['block', 'log']),
            ('refererheadercheck',  'if_present'),
            ('cookieconsistencyaction',  ['block', 'learn']),
            ('cookietransforms',  'on'),
            ('cookieencryption',  'decryptOnly'),
            ('cookieproxying',  'sessionOnly'),
            ('addcookieflags',  'all'),
            ('fieldconsistencyaction',  ['block', 'learn', 'stats']),
            ('csrftagaction',  ['block', 'learn', 'stats']),
            ('crosssitescriptingaction', ['block', 'learn', 'log']),
            ('crosssitescriptingtransformunsafehtml',  'on'),
            ('crosssitescriptingcheckcompleteurls',  'on'),
            ('sqlinjectionaction',  ['block', 'learn', 'log']),
            ('sqlinjectiontransformspecialchars',  'on'),
    
            # FIXME  see issues.md
            #('sqlinjectiononlycheckfieldswithsqlchars',  'off'),
    
            ('sqlinjectiontype',  'SQLKeyword'),
            ('sqlinjectionchecksqlwildchars',  'on'),
            ('fieldformataction', ['block', 'learn', 'log']),
            ('defaultfieldformattype', 'alpha'),
            ('defaultfieldformatminlength', 1),
            ('defaultfieldformatmaxlength', '255'),
            ('bufferoverflowaction', ['block', 'log', 'stats']),
            ('bufferoverflowmaxurllength', 3500),
            ('bufferoverflowmaxheaderlength', 1000),
            ('bufferoverflowmaxcookielength', '1500'),
            ('creditcardaction', ['block', 'log']),
            ('creditcard', ['visa']),
            ('creditcardmaxallowed', 10),
            ('creditcardxout', 'off'),
            ('dosecurecreditcardlogging', 'off'),
            ('streaming', 'on'),
            ('trace', 'on'),
            ('requestcontenttype', 'x-form/noexist'),
            ('responsecontenttype', 'xxx-form/noexist'),
            ('xmldosaction', ['block', 'learn', 'log']),
            ('xmlformataction', ['block', 'log', 'stats']),
            ('xmlsqlinjectionaction', ['log', 'stats']),
    
            # FIXME  see issues.md
            #('xmlsqlinjectiononlycheckfieldswithsqlchars', 'off'),
    
            ('xmlsqlinjectiontype', 'SQLKeyword'),
            ('xmlsqlinjectionchecksqlwildchars', 'on'),
            ('xmlsqlinjectionparsecomments', 'ansi'),
            ('xmlxssaction', ['block', 'log']),
            ('xmlwsiaction', ['block', 'log']),
            ('xmlattachmentaction', ['block', 'learn', 'log']),
            ('xmlvalidationaction', ['none']),
    
            # FIXME errorcode:2005
            #('xmlerrorobject', 'NS_S_AS_ERROR_OBJECT_DEFAULT'),
    
            # FIXME errorcode:2005
            #('customsettings', 'custom_object'),
    
            # FIXME errorcode:2005
            #('signatures', 'sig_object'),
    
            ('xmlsoapfaultaction', ['block', 'log', 'remove']),
            ('usehtmlerrorobject', 'on'),
            ('errorurl', 'http://error.com'),
    
            # FIXME errorcode:2005
            #('htmlerrorobject', 'my_error_object'),
    
            ('logeverypolicyhit', 'on'),
    
            # FIXME  see issues.md
            #('stripcomments', 'on'),
    
            ('striphtmlcomments', 'none'),
            ('stripxmlcomments', 'all'),
            ('exemptclosureurlsfromsecuritychecks', 'on'),
            ('defaultcharset', 'utf-8'),
            ('postbodylimit', 500000),
            ('fileuploadmaxnum', 10000),
            ('canonicalizehtmlresponse', 'on'),
            ('enableformtagging', 'on'),
            ('sessionlessfieldconsistency', '"OFF"'),
            ('sessionlessurlclosure', 'off'),
            ('semicolonfieldseparator', 'off'),
            ('excludefileuploadfromchecks', 'on'),
            ('sqlinjectionparsecomments', 'nested'),
            ('invalidpercenthandling', 'asp_mode'),
            ('type', ['HTML']),
            ('checkrequestheaders', 'on'),
            ('optimizepartialreqs', 'on'),
            ('urldecoderequestcookies', 'on'),
            ('comment', 'sample appfw profile comment'),
            ('percentdecoderecursively', 'on'),
            ('multipleheaderaction', ['keepLast']),
            #('archivename', 'archive.tar'),
        ]
    )
    
    # Initial values
    submodObj.add_operation('setup', copy.deepcopy(attributes))
    
    verification_dict = copy.deepcopy(attributes)
    
    def process_verification_dict():
        del verification_dict['state']
        for key in verification_dict:
            val = verification_dict[key]
            if isinstance(val, list):
                verification_dict[key] = '%s' % str(verification_dict[key])
                verification_dict[key] = re.sub(r'\'','"', verification_dict[key])
                #print(verification_dict[key])
            elif val == '"OFF"':
                verification_dict[key] = '"OFF"'
            elif val in ('on', 'off'):
                verification_dict[key] = '"%s"' % verification_dict[key].upper()
            else:
                verification_dict[key] = '"%s"' % verification_dict[key]
    
    
    
    process_verification_dict()
    # Verify
    data = helpers.get_verification_playbook_dict(
        nitro_resource='appfwprofile',
        nitro_resource_name=attributes['name'],
        verification_dict=verification_dict,
    )
    submodObj.add_raw_operation('setup_verify', data, run_once=True)
    
    # Change comment
    attributes['comment'] = 'Some other profile comment'
    submodObj.add_operation('update_comment', copy.deepcopy(attributes))
    
    # Change a list type attribute
    attributes['sqlinjectionaction'] = ['learn', 'log', 'stats']
    submodObj.add_operation('update_sqlinjectionaction', copy.deepcopy(attributes))
    
    # Remove profile
    attributes['state'] = 'absent'
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    
    # Add test in roles directory
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    ##########################
    # defaults only testcase #
    ##########################
    
    attributes =  OrderedDict([
        ('state',  'present'),
    
        ('name',  'profile_basic_integration_test'),
        ('defaults',  'basic'),
    ])
    
    submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, 'basic')
    
    # Initial values
    submodObj.add_operation('setup', copy.deepcopy(attributes), run_once=True)
    
    attributes['state'] = 'absent'
    
    submodObj.add_operation('remove', copy.deepcopy(attributes))
    
    # Add test in roles directory
    input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    #######################
    # Bindings one by one #
    #######################
    
    
    def construct_binding_test(bindings_key, bindings_list):
        first_binding = bindings_list[0]
        first_modified = bindings_list[1]
        second_binding = bindings_list[2]
    
        bindings_base_attributes =  OrderedDict([
            ('state',  'present'),
    
            ('name',  'profile_basic_integration_test'),
        ])
    
        submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, bindings_key)
    
        attributes = copy.deepcopy(bindings_base_attributes)
    
        attributes.update({
            bindings_key: OrderedDict([
                ('mode', 'exact'),
                ('attributes', []),
            ])
        })
    
        # Setup one exact
        attributes[bindings_key]['attributes'] = [first_binding]
        submodObj.add_operation('setup', copy.deepcopy(attributes))
    
        # Modify one exact
        attributes[bindings_key]['attributes'] = [first_modified]
        submodObj.add_operation('modify_one_exact', copy.deepcopy(attributes))
    
        # Add one bind
        attributes[bindings_key]['mode'] = 'bind'
        attributes[bindings_key]['attributes'] = [second_binding]
    
        submodObj.add_operation('bind_one', copy.deepcopy(attributes))
    
        # Remove the first with unbind
    
        attributes[bindings_key]['mode'] = 'unbind'
        attributes[bindings_key]['attributes'] = [first_modified]
        submodObj.add_operation('unbind_one', copy.deepcopy(attributes))
    
        # Empty list exact
        attributes[bindings_key]['mode'] = 'exact'
        attributes[bindings_key]['attributes'] = []
    
        submodObj.add_operation('empty_exact', copy.deepcopy(attributes))
    
        # Remove profile
        attributes['state'] = 'absent'
        submodObj.add_operation('remove', copy.deepcopy(attributes))
    
        # Add the integration test to the module
        input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    ########################
    # contenttype_bindings #
    ########################
    
    first_binding = OrderedDict([
            ('state', 'enabled'),
            ('contenttype', 'some_content_type'),
            ('comment', ' content type comment'),
        ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('contenttype', 'some_other_content_type'),
        ('comment', ' content type comment'),
    ])
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='contenttype_bindings',
        bindings_list=bindings_list
    )
    
    
    ##############################
    # cookieconsistency_bindings #
    ##############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('isregex', 'REGEX'),
        ('cookieconsistency', 'cookie_name'),
        ('comment', 'cookieconsistency comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('isregex', 'REGEX'),
        ('cookieconsistency', 'cookie_name_too'),
        ('comment', 'cookieconsistency comment too'),
    ])
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='cookieconsistency_bindings',
        bindings_list=bindings_list
    )
    
    #############################
    # creditcardnumber_bindings #
    #############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('creditcardnumberurl', 'http://credit/com'),
        ('creditcardnumber', '"1234"'),
        ('comment', 'creditcardnumber comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('creditcardnumberurl', 'http://credit/com'),
        ('creditcardnumber', '"4321"'),
        ('comment', 'creditcardnumber comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='creditcardnumber_bindings',
        bindings_list=bindings_list
    )
    
    ##############################
    # crosssitescripting_bindings #
    ##############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('crosssitescripting', 'field_name'),
        ('isregex_xss', 'NOTREGEX'),
        ('state', 'enabled'),
        ('comment', 'crosssitescripting comment'),
        ('formactionurl_xss', 'http://action.com'),
        ('as_value_expr_xss', 'value_expressoin'),
        ('as_scan_location_xss', 'COOKIE'),
        ('as_value_type_xss', 'Attribute'),
        ('isvalueregex_xss', 'REGEX'),
    
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('crosssitescripting', 'field_name_too'),
        ('isregex_xss', 'NOTREGEX'),
        ('state', 'enabled'),
        ('comment', 'crosssitescripting comment'),
        ('formactionurl_xss', 'http://action.com'),
        ('as_value_expr_xss', 'value_expressoin'),
        ('as_scan_location_xss', 'COOKIE'),
        ('as_value_type_xss', 'Attribute'),
        ('isvalueregex_xss', 'REGEX'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='crosssitescripting_bindings',
        bindings_list=bindings_list
    )
    
    ####################
    # csrftag_bindings #
    ####################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('csrftag', 'http://origin.url'),
        ('csrfformactionurl', 'http://action.url'),
        ('comment', 'csrftag comment'),
    
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('csrftag', 'http://origintoo.url'),
        ('csrfformactionurl', 'http://actiontoo.url'),
        ('comment', 'csrftag comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='csrftag_bindings',
        bindings_list=bindings_list
    )
    
    ####################
    # denyurl_bindings #
    ####################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('denyurl', 'denyme.*'),
        ('comment', 'denyurl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('denyurl', 'denymetoo.*'),
        ('comment', 'denyurl comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='denyurl_bindings',
        bindings_list=bindings_list
    )
    
    ##################################
    # excluderescontenttype_bindings #
    ##################################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('excluderescontenttype', 'exclude.*'),
        ('comment', 'excluderescontenttype comment'),
    
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('excluderescontenttype', 'exclude_too.*'),
        ('comment', 'excluderescontenttype comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='excluderescontenttype_bindings',
        bindings_list=bindings_list
    )
    
    #############################
    # fieldconsistency_bindings #
    #############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('fieldconsistency', 'field_name'),
        ('isregex_ffc', 'NOTREGEX'),
        ('formactionurl_ffc', 'http://action.url'),
        ('comment', 'fieldconsistency comment'),
    
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('fieldconsistency', 'field_name_too'),
        ('isregex_ffc', 'REGEX'),
        ('formactionurl_ffc', 'http://action_too.url'),
        ('comment', 'fieldconsistency comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='fieldconsistency_bindings',
        bindings_list=bindings_list
    )
    
    ########################
    # fieldformat_bindings #
    ########################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('fieldformatmaxlength', '"1000"'),
        ('isregex_ff', 'REGEX'),
        ('fieldtype', 'alpha'),
        ('formactionurl_ff', 'http://action.url'),
        ('fieldformatminlength', '"200"'),
        ('comment', 'fieldformat_bindings comment'),
        ('fieldformat', 'form_field_name'),
    
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('fieldformatmaxlength', '"2000"'),
        ('isregex_ff', 'NOTREGEX'),
        ('fieldtype', 'alphanum'),
        ('formactionurl_ff', 'http://action_too.url'),
        ('fieldformatminlength', '"100"'),
        ('comment', 'fieldformat_bindings comment too'),
        ('fieldformat', 'form_field_name_too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='fieldformat_bindings',
        bindings_list=bindings_list
    )
    
    #######################
    # safeobject_bindings #
    #######################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('maxmatchlength', '"1000"'),
        ('as_expression', 'safe_obj_regex'),
        ('safeobject', 'safe_obj_name'),
        ('comment', 'safe_obj_name comment'),
        ('action', ['log']),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('maxmatchlength', '"1000"'),
        ('as_expression', 'safe_obj_regex_too'),
        ('safeobject', 'safe_obj_name_too'),
        ('comment', 'safe_obj_name comment too'),
        ('action', ['block']),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='safeobject_bindings',
        bindings_list=bindings_list
    )
    
    #########################
    # sqlinjection_bindings #
    #########################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_value_expr_sql', 'value_expresssion'),
        ('formactionurl_sql', 'http://action.url'),
        ('isregex_sql', 'REGEX'),
        ('isvalueregex_sql', 'NOTREGEX'),
        ('as_scan_location_sql', 'FORMFIELD'),
        ('sqlinjection', 'field_name'),
        ('as_value_type_sql', 'Keyword'),
        ('comment', 'sqlinjection comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_value_expr_sql', 'value_expresssion_too'),
        ('formactionurl_sql', 'http://action.url.too'),
        ('isregex_sql', 'NOTREGEX'),
        ('isvalueregex_sql', 'REGEX'),
        ('as_scan_location_sql', 'HEADER'),
        ('sqlinjection', 'field_name_too'),
        ('as_value_type_sql', 'Wildchar'),
        ('comment', 'sqlinjection comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='sqlinjection_bindings',
        bindings_list=bindings_list
    )
    
    #####################
    # starturl_bindings #
    #####################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('starturl', 'url_regex'),
        ('comment', 'starturl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('starturl', 'url_regex_too'),
        ('comment', 'starturl comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='starturl_bindings',
        bindings_list=bindings_list
    )
    
    
    
    def construct_binding_test_singular_binding_only(bindings_key, bindings_list):
        '''
            This is special since the only allowed value
            for the key 'xmlattachmenturl' is '.*'.
    
            This results in only one binding ever being possible.
        '''
        first_binding = bindings_list[0]
        first_modified = bindings_list[1]
    
    
        bindings_base_attributes =  OrderedDict([
            ('state',  'present'),
    
            ('name',  'profile_basic_integration_test'),
        ])
    
        submodObj = BaseIntegrationModule(test_type, ENTITY_NAME, bindings_key)
    
        attributes = copy.deepcopy(bindings_base_attributes)
    
        attributes.update({
            bindings_key: OrderedDict([
                ('mode', 'exact'),
                ('attributes', []),
            ])
        })
    
        # Setup one exact
        attributes[bindings_key]['attributes'] = [first_binding]
        submodObj.add_operation('setup', copy.deepcopy(attributes))
    
        # Modify one exact
        attributes[bindings_key]['attributes'] = [first_modified]
        submodObj.add_operation('modify_one_exact', copy.deepcopy(attributes))
    
        # Empty list exact
        attributes[bindings_key]['mode'] = 'exact'
        attributes[bindings_key]['attributes'] = []
    
        submodObj.add_operation('empty_exact', copy.deepcopy(attributes))
    
        # Remove profile
        attributes['state'] = 'absent'
        submodObj.add_operation('remove', copy.deepcopy(attributes))
    
        # Add the integration test to the module
        input_data.update({submodObj.get_sub_mod_name(): copy.deepcopy(submodObj.get_mod_attrib())})
    
    
    #############################
    # xmlattachmenturl_bindings #
    #############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('xmlattachmenturl', '.*'),
        ('xmlmaxattachmentsize', '"100000"'),
        ('xmlmaxattachmentsizecheck', 'on'),
        ('xmlattachmentcontenttypecheck', 'off'),
        ('xmlattachmentcontenttype', 'content_type_regex'),
        ('comment', 'xmlattachmenturl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    construct_binding_test_singular_binding_only(
        bindings_key='xmlattachmenturl_bindings',
        bindings_list=[first_binding, first_modified]
    )
    
    ######################
    # xmldosurl_bindings #
    ######################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('xmlmaxelementdepthcheck', 'on'),
        ('xmlmaxfilesize', '"10000"'),
        ('xmlmaxnamespaceurilength', '"10000"'),
        ('xmldosurl', '.*'),
        ('xmlsoaparraycheck', 'off'),
        ('xmlmaxelementnamelengthcheck', 'off'),
        ('xmlmaxelementscheck', 'off'),
        ('xmlmaxentityexpansions', '"10"'),
        ('xmlmaxattributes', '"100"'),
        ('xmlmaxfilesizecheck', 'on'),
        ('xmlmaxchardatalength', '"100000"'),
        ('xmlmaxnamespacescheck', 'off'),
        ('xmlmaxnamespaces', '"100"'),
        ('xmlmaxattributenamelengthcheck', 'off'),
        ('xmlblockdtd', 'off'),
        ('xmlmaxattributevaluelength', '"1000"'),
        ('xmlmaxelementdepth', '"1000"'),
        ('xmlmaxelementnamelength', '"1000"'),
        ('xmlblockpi', 'off'),
        ('xmlmaxelementchildrencheck', 'off'),
        ('xmlmaxelements', '"100"'),
        ('xmlmaxentityexpansionscheck', 'off'),
        ('xmlmaxnamespaceurilengthcheck', 'off'),
        ('xmlmaxentityexpansiondepthcheck', 'off'),
        ('xmlmaxattributevaluelengthcheck', 'off'),
        ('xmlmaxsoaparraysize', '"100"'),
        ('xmlmaxentityexpansiondepth', '"10"'),
        ('xmlmaxnodescheck', 'off'),
        ('xmlmaxattributenamelength', '"1000"'),
        ('xmlmaxchardatalengthcheck', 'off'),
        ('xmlminfilesizecheck', 'off'),
        ('xmlmaxelementchildren', '"100"'),
        ('xmlminfilesize', '"100"'),
        ('xmlmaxnodes', '"1000"'),
        ('xmlmaxattributescheck', 'off'),
        ('xmlmaxsoaparrayrank', '"16"'),
        ('xmlblockexternalentities', 'off'),
        ('comment', 'some xmldosurl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    
    bindings_list = [
        first_binding,
        first_modified,
    ]
    
    construct_binding_test_singular_binding_only(
        bindings_key='xmldosurl_bindings',
        bindings_list=bindings_list
    )
    
    ############################
    # xmlsqlinjection_bindings #
    ############################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_scan_location_xmlsql', 'ELEMENT'),
        ('xmlsqlinjection', 'ELEMENT'),
        ('isregex_xmlsql', 'REGEX'),
        ('comment', 'xmlsqlinjection comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_scan_location_xmlsql', 'ATTRIBUTE'),
        ('xmlsqlinjection', 'REGEX'),
        ('isregex_xmlsql', 'NOTREGEX'),
        ('comment', 'xmlsqlinjection comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='xmlsqlinjection_bindings',
        bindings_list=bindings_list
    )
    
    #############################
    # xmlvalidationurl_bindings #
    #############################
    
    
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('xmlwsdl', 'wsdl_object'),
        ('xmlendpointcheck', 'ABSOLUTE'),
        ('xmlvalidateresponse', 'on'),
        ('xmlvalidationurl', '.*'),
        ('xmlresponseschema', 'schema_object'),
        ('xmlvalidatesoapenvelope', 'on'),
        ('xmlrequestschema', 'schema_other'),
        ('xmladditionalsoapheaders', 'on'),
        ('comment', 'xmlvalidationurl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    
    second_binding = OrderedDict([
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
    ]
    
    # FIXME need to instantiate objects on NS filesystem
    # for binding to be tested properly
    # Don't know where these files should be
    
    '''
    construct_binding_test_singular_binding_only(
        bindings_key='xmlvalidationurl_bindings',
        bindings_list=bindings_list
    )
    '''
    
    ######################
    # xmlwsiurl_bindings #
    ######################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('xmlwsichecks', 'BP1201, R1140'),
        ('xmlwsiurl', '.*'),
        ('comment', 'xmlwsiurl comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    
    bindings_list = [
        first_binding,
        first_modified,
    ]
    
    construct_binding_test_singular_binding_only(
        bindings_key='xmlwsiurl_bindings',
        bindings_list=bindings_list
    )
    
    ###################
    # xmlxss_bindings #
    ###################
    
    first_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_scan_location_xmlxss', 'ELEMENT'),
        ('isregex_xmlxss', 'REGEX'),
        ('xmlxss', 'REGEX'),
        ('comment', 'xmlxss comment'),
    ])
    
    first_modified = copy.deepcopy(first_binding)
    first_modified['comment'] = 'other comment'
    
    
    second_binding = OrderedDict([
        ('state', 'enabled'),
        ('as_scan_location_xmlxss', 'ATTRIBUTE'),
        ('isregex_xmlxss', 'NOTREGEX'),
        ('xmlxss', 'NOTREGEX'),
        ('comment', 'xmlxss comment too'),
    ])
    
    
    bindings_list = [
        first_binding,
        first_modified,
        second_binding,
    ]
    
    construct_binding_test(
        bindings_key='xmlxss_bindings',
        bindings_list=bindings_list
    )
    
    return input_data
