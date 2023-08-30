#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: appfwprofile
short_description: Configuration for application firewall profile resource.
description: Configuration for application firewall profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  addcookieflags:
    choices:
      - none
      - httpOnly
      - secure
      - all
    description:
      - 'Add the specified flags to cookies. Available settings function as follows:'
      - '* None - Do not add flags to cookies.'
      - '* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from
        accessing cookies.'
      - '* Secure - Add Secure flag to cookies.'
      - '* All - Add both HTTPOnly and Secure flags to cookies.'
    type: str
    default: none
  archivename:
    description:
      - Source for tar archive.
    type: str
  augment:
    description:
      - Augment Relaxation Rules during import
    type: bool
  blockkeywordaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'Block Keyword action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -blockKeywordAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -blockKeywordAction C(none)".'
    type: list
    elements: str
    default: none
  bufferoverflowaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more Buffer Overflow actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -bufferOverflowAction C(none)".'
    type: list
    elements: str
  bufferoverflowmaxcookielength:
    description:
      - Maximum length, in characters, for cookies sent to your protected web sites.
        Requests with longer cookies are blocked.
    type: int
    default: 4096
  bufferoverflowmaxheaderlength:
    description:
      - Maximum length, in characters, for HTTP headers in requests sent to your protected
        web sites. Requests with longer headers are blocked.
    type: int
    default: 4096
  bufferoverflowmaxquerylength:
    description:
      - Maximum length, in bytes, for query string sent to your protected web sites.
        Requests with longer query strings are blocked.
    type: int
    default: 65535
  bufferoverflowmaxtotalheaderlength:
    description:
      - Maximum length, in bytes, for the total HTTP header length in requests sent
        to your protected web sites. The minimum value of this and maxHeaderLen in
        httpProfile will be used. Requests with longer length are blocked.
    type: int
    default: 65535
  bufferoverflowmaxurllength:
    description:
      - Maximum length, in characters, for URLs on your protected web sites. Requests
        with longer URLs are blocked.
    type: int
    default: 1024
  canonicalizehtmlresponse:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Perform HTML entity encoding for any special characters in responses sent
        by your protected web sites.
    type: str
    default: 'ON'
  ceflogging:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable CEF format logs for the profile.
    type: str
  checkrequestheaders:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check request headers as well as web forms for injected SQL and cross-site
        scripts.
    type: str
    default: 'OFF'
  clientipexpression:
    description:
      - Expression to get the client IP.
    type: str
  cmdinjectionaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'Command injection action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -cmdInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -cmdInjectionAction C(none)".'
    type: list
    elements: str
    default: none
  cmdinjectiongrammar:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for CMD injection using CMD grammar
    type: str
    default: 'OFF'
  cmdinjectiontype:
    choices:
      - CMDSplChar
      - CMDKeyword
      - CMDSplCharORKeyword
      - CMDSplCharANDKeyword
      - None
    description:
      - 'Available CMD injection types. '
      - '-C(CMDSplChar)              : Checks for CMD Special Chars'
      - '-C(CMDKeyword)              : Checks for CMD Keywords'
      - '-C(CMDSplCharANDKeyword)    : Checks for both and blocks if both are found'
      - '-C(CMDSplCharORKeyword)     : Checks for both and blocks if anyone is found,'
      - '-C(None)                    : Disables checking using both CMD Special Char
        and Keyword'
    type: str
    default: CMDSplCharANDKeyword
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  contenttypeaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Content-type actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -contentTypeaction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -contentTypeaction C(none)".'
    type: list
    elements: str
  cookieconsistencyaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Cookie Consistency actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -cookieConsistencyAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -cookieConsistencyAction C(none)".'
    type: list
    elements: str
    default: none
  cookieencryption:
    choices:
      - none
      - decryptOnly
      - encryptSessionOnly
      - encryptAll
    description:
      - 'Type of cookie encryption. Available settings function as follows:'
      - '* None - Do not encrypt cookies.'
      - '* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.'
      - '* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.'
      - '* Encrypt All - Encrypt all cookies.'
    type: str
    default: none
  cookiehijackingaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more actions to prevent cookie hijacking. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - 'NOTE: Cookie Hijacking feature is not supported for TLSv1.3'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -cookieHijackingAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -cookieHijackingAction C(none)".'
    type: list
    elements: str
    default: none
  cookieproxying:
    choices:
      - none
      - sessionOnly
    description:
      - 'Cookie proxy setting. Available settings function as follows:'
      - '* None - Do not proxy cookies.'
      - '* Session Only - Proxy session cookies by using the Citrix ADC session ID,
        but do not proxy permanent cookies.'
    type: str
    default: none
  cookiesamesiteattribute:
    choices:
      - None
      - LAX
      - STRICT
    description:
      - Cookie Samesite attribute added to support adding cookie SameSite attribute
        for all set-cookies including appfw session cookies. Default value will be
        "SameSite=Lax".
    type: str
    default: LAX
  cookietransforms:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'Perform the specified type of cookie transformation. '
      - 'Available settings function as follows: '
      - '* Encryption - Encrypt cookies.'
      - '* Proxying - Mask contents of server cookies by sending proxy cookie to users.'
      - '* Cookie flags - Flag cookies as HTTP only to prevent scripts on user''s
        browser from accessing and possibly modifying them.'
      - 'CAUTION: Make sure that this parameter is set to C(ON) if you are configuring
        any cookie transformations. If it is set to C(OFF), no cookie transformations
        are performed regardless of any other settings.'
    type: str
    default: 'OFF'
  creditcard:
    choices:
      - none
      - visa
      - mastercard
      - discover
      - amex
      - jcb
      - dinersclub
    description:
      - Credit card types that the application firewall should protect.
    type: list
    elements: str
    default: none
  creditcardaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Credit Card actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -creditCardAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -creditCardAction C(none)".'
    type: list
    elements: str
    default: none
  creditcardmaxallowed:
    description:
      - This parameter value is used by the block action. It represents the maximum
        number of credit card numbers that can appear on a web page served by your
        protected web sites. Pages that contain more credit card numbers are blocked.
    type: int
  creditcardxout:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Mask any credit card number detected in a response by replacing each digit,
        except the digits in the final group, with the letter "X."
    type: str
    default: 'OFF'
  crosssitescriptingaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Cross-Site Scripting (XSS) actions. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -crossSiteScriptingAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -crossSiteScriptingAction C(none)".'
    type: list
    elements: str
  crosssitescriptingcheckcompleteurls:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check complete URLs for cross-site scripts, instead of just the query portions
        of URLs.
    type: str
    default: 'OFF'
  crosssitescriptingtransformunsafehtml:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'Transform cross-site scripts. This setting configures the application firewall
        to disable dangerous HTML instead of blocking the request. '
      - 'CAUTION: Make sure that this parameter is set to C(ON) if you are configuring
        any cross-site scripting transformations. If it is set to C(OFF), no cross-site
        scripting transformations are performed regardless of any other settings.'
    type: str
    default: 'OFF'
  csrftagaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available
        settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -CSRFTagAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -CSRFTagAction C(none)".'
    type: list
    elements: str
    default: none
  customsettings:
    description:
      - Object name for custom settings.
      - 'This check is applicable to Profile Type: HTML, XML.'
    type: str
  defaultcharset:
    description:
      - 'Default character set for protected web pages. Web pages sent by your protected
        web sites in response to user requests are assigned this character set if
        the page does not already specify a character set. The character sets supported
        by the application firewall are: '
      - '* iso-8859-1 (English US)'
      - '* big5 (Chinese Traditional)'
      - '* gb2312 (Chinese Simplified)'
      - '* sjis (Japanese Shift-JIS)'
      - '* euc-jp (Japanese EUC-JP)'
      - '* iso-8859-9 (Turkish)'
      - '* utf-8 (Unicode)'
      - '* euc-kr (Korean)'
    type: str
  defaultfieldformatmaxlength:
    description:
      - Maximum length, in characters, for data entered into a field that is assigned
        the default field type.
    type: int
    default: 65535
  defaultfieldformatminlength:
    description:
      - 'Minimum length, in characters, for data entered into a field that is assigned
        the default field type. '
      - To disable the minimum and maximum length settings and allow data of any length
        to be entered into the field, set this parameter to zero (0).
    type: int
  defaultfieldformattype:
    description:
      - Designate a default field type to be applied to web form fields that do not
        have a field type explicitly assigned to them.
    type: str
  defaults:
    choices:
      - basic
      - advanced
      - core
    description:
      - Default configuration to apply to the profile. Basic defaults are intended
        for standard content that requires little further configuration, such as static
        web site content. Advanced defaults are intended for specialized content that
        requires significant specialized configuration, such as heavily scripted or
        dynamic content.
      - ''
      - 'CLI users: When adding an application firewall profile, you can set either
        the defaults or the type, but not both. To set both options, create the profile
        by using the add appfw profile command, and then use the set appfw profile
        command to configure the other option.'
    type: str
  denyurlaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more Deny URL actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'NOTE: The Deny URL check takes precedence over the Start URL check. If you
        enable blocking for the Deny URL check, the application firewall blocks any
        URL that is explicitly blocked by a Deny URL, even if the same URL would otherwise
        be allowed by the Start URL check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -denyURLaction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -denyURLaction C(none)".'
    type: list
    elements: str
  dosecurecreditcardlogging:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Setting this option logs credit card numbers in the response when the match
        is found.
    type: str
    default: 'ON'
  dynamiclearning:
    choices:
      - none
      - SQLInjection
      - CrossSiteScripting
      - fieldFormat
      - startURL
      - cookieConsistency
      - fieldConsistency
      - CSRFtag
      - ContentType
    description:
      - 'One or more security checks. Available options are as follows:'
      - '* C(SQLInjection) - Enable dynamic learning for C(SQLInjection) security
        check.'
      - '* C(CrossSiteScripting) - Enable dynamic learning for C(CrossSiteScripting)
        security check.'
      - '* C(fieldFormat) - Enable dynamic learning for  C(fieldFormat) security check.'
      - '* None - Disable security checks for all security checks.'
      - ''
      - 'CLI users: To enable dynamic learning on one or more security checks, type
        "set appfw profile -dynamicLearning" followed by the security checks to be
        enabled. To turn off dynamic learning on all security checks, type "set appfw
        profile -dynamicLearning C(none)".'
    type: list
    elements: str
  enableformtagging:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable tagging of web form fields for use by the Form Field Consistency and
        CSRF Form Tagging checks.
    type: str
    default: 'ON'
  errorurl:
    description:
      - URL that application firewall uses as the Error URL.
    type: str
  excludefileuploadfromchecks:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Exclude uploaded files from Form checks.
    type: str
    default: 'OFF'
  exemptclosureurlsfromsecuritychecks:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Exempt URLs that pass the Start URL closure check from SQL injection, cross-site
        script, field format and field consistency security checks at locations other
        than headers.
    type: str
    default: 'ON'
  fakeaccountdetection:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'Fake account detection flag : C(ON)/C(OFF). If set to C(ON) fake account
        detection in enabled on ADC, if set to C(OFF) fake account detection is disabled.'
    type: str
    default: 'OFF'
  fieldconsistencyaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Form Field Consistency actions. Available settings function as
        follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -fieldConsistencyaction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -fieldConsistencyAction C(none)".'
    type: list
    elements: str
    default: none
  fieldformataction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Field Format actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of suggested web form
        fields and field format assignments.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -fieldFormatAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -fieldFormatAction C(none)".'
    type: list
    elements: str
  fileuploadmaxnum:
    description:
      - Maximum allowed number of file uploads per form-submission request. The maximum
        setting (65535) allows an unlimited number of uploads.
    type: int
    default: 65535
  fileuploadtypesaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more file upload types actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -fileUploadTypeAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -fileUploadTypeAction C(none)".'
    type: list
    elements: str
  geolocationlogging:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable Geo-Location Logging in CEF format logs for the profile.
    type: str
  grpcaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - gRPC validation
    type: list
    elements: str
  htmlerrorobject:
    description:
      - 'Name to assign to the HTML Error Object. '
      - Must begin with a letter, number, or the underscore character \(_\), and must
        contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\),
        space \( \), at (@), equals \(=\), colon \(:\), and underscore characters.
        Cannot be changed after the HTML error object is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks \(for example, "my HTML error object" or 'my HTML error object'\).
    type: str
  htmlerrorstatuscode:
    description:
      - Response status code associated with HTML error page. Non-empty HTML error
        object must be imported to the application firewall profile for the status
        code.
    type: int
    default: 200
  htmlerrorstatusmessage:
    description:
      - Response status message associated with HTML error page
    type: str
  importprofilename:
    description:
      - Name of the profile which will be created/updated to associate the relaxation
        rules
    type: str
  infercontenttypexmlpayloadaction:
    choices:
      - block
      - log
      - stats
      - none
    description:
      - 'One or more infer content type payload actions. Available settings function
        as follows:'
      - '* Block - Block connections that have mismatch in content-type header and
        payload.'
      - '* Log - Log connections that have mismatch in content-type header and payload.
        The mismatched content-type in HTTP request header will be logged for the
        request.'
      - '* Stats - Generate statistics when there is mismatch in content-type header
        and payload.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -inferContentTypeXMLPayloadAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -inferContentTypeXMLPayloadAction C(none)". Please note "C(none)"
        action cannot be used with any other action type.'
    type: list
    elements: str
  insertcookiesamesiteattribute:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure whether application firewall should add samesite attribute for set-cookies
    type: str
    default: 'OFF'
  inspectcontenttypes:
    choices:
      - none
      - application/x-www-form-urlencoded
      - multipart/form-data
      - text/x-gwt-rpc
      - application/grpc
      - application/grpc-web-text
      - application/grpc-web+json
    description:
      - 'One or more InspectContentType lists. '
      - '* C(application/x-www-form-urlencoded)'
      - '* C(multipart/form-data)'
      - '* C(text/x-gwt-rpc)'
      - ''
      - 'CLI users: To enable, type "set appfw profile -InspectContentTypes" followed
        by the content types to be inspected.'
    type: list
    elements: str
  inspectquerycontenttypes:
    choices:
      - HTML
      - XML
      - JSON
      - OTHER
    description:
      - Inspect request query as well as web forms for injected SQL and cross-site
        scripts for following content types.
    type: list
    elements: str
  invalidpercenthandling:
    choices:
      - apache_mode
      - asp_mode
      - secure_mode
    description:
      - 'Configure the method that the application firewall uses to handle percent-encoded
        names and values. Available settings function as follows: '
      - '* C(apache_mode) - Apache format.'
      - '* C(asp_mode) - Microsoft ASP format.'
      - '* C(secure_mode) - Secure format.'
    type: str
    default: secure_mode
  jsonblockkeywordaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'JSON Block Keyword action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONBlockKeywordAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONBlockKeywordAction C(none)".'
    type: list
    elements: str
    default: none
  jsoncmdinjectionaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more JSON CMD Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONCMDInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONCMDInjectionAction C(none)".'
    type: list
    elements: str
  jsoncmdinjectiongrammar:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for CMD injection using CMD grammar in JSON
    type: str
    default: 'OFF'
  jsoncmdinjectiontype:
    choices:
      - CMDSplChar
      - CMDKeyword
      - CMDSplCharORKeyword
      - CMDSplCharANDKeyword
      - None
    description:
      - Available CMD injection types.
      - '-C(CMDSplChar)              : Checks for CMD Special Chars'
      - '-C(CMDKeyword)              : Checks for CMD Keywords'
      - '-C(CMDSplCharANDKeyword)    : Checks for both and blocks if both are found'
      - '-C(CMDSplCharORKeyword)     : Checks for both and blocks if anyone is found,'
      - '-C(None)                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: CMDSplCharANDKeyword
  jsondosaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more JSON Denial-of-Service (JsonDoS) actions. Available settings
        function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONDoSAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONDoSAction C(none)".'
    type: list
    elements: str
  jsonerrorobject:
    description:
      - Name to the imported JSON Error Object to be set on application firewall profile.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks \(for example, "my JSON error object" or 'my JSON error object'\).
    type: str
  jsonerrorstatuscode:
    description:
      - Response status code associated with JSON error page. Non-empty JSON error
        object must be imported to the application firewall profile for the status
        code.
    type: int
    default: 200
  jsonerrorstatusmessage:
    description:
      - Response status message associated with JSON error page
    type: str
  jsonsqlinjectionaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more JSON SQL Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONSQLInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONSQLInjectionAction C(none)".'
    type: list
    elements: str
  jsonsqlinjectiongrammar:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for SQL injection using SQL grammar in JSON
    type: str
    default: 'OFF'
  jsonsqlinjectiontype:
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
    description:
      - Available SQL injection types.
      - '-C(SQLSplChar)              : Checks for SQL Special Chars'
      - '-C(SQLKeyword)              : Checks for SQL Keywords'
      - '-C(SQLSplCharANDKeyword)    : Checks for both and blocks if both are found'
      - '-C(SQLSplCharORKeyword)     : Checks for both and blocks if anyone is found,'
      - '-C(None)                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: SQLSplCharANDKeyword
  jsonxssaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more JSON Cross-Site Scripting actions. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONXssAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONXssAction C(none)".'
    type: list
    elements: str
  logeverypolicyhit:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Log every profile match, regardless of security checks results.
    type: str
    default: 'OFF'
  matchurlstring:
    description:
      - Match this action url in archived Relaxation Rules to replace.
    type: str
  multipleheaderaction:
    choices:
      - block
      - keepLast
      - log
      - none
    description:
      - 'One or more multiple header actions. Available settings function as follows:'
      - '* Block - Block connections that have multiple headers.'
      - '* Log - Log connections that have multiple headers.'
      - '* KeepLast - Keep only last header when multiple headers are present.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -multipleHeaderAction"
        followed by the actions to be enabled.'
    type: list
    elements: str
  name:
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
    type: str
  optimizepartialreqs:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Optimize handle of HTTP partial requests i.e. those with range headers.
      - 'Available settings are as follows: '
      - '* C(ON)  - Partial requests by the client result in partial requests to the
        backend server in most cases.'
      - '* C(OFF) - Partial requests by the client are changed to full requests to
        the backend server'
    type: str
    default: 'ON'
  overwrite:
    description:
      - Purge existing Relaxation Rules and replace during import
    type: bool
  percentdecoderecursively:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Configure whether the application firewall should use percentage recursive
        decoding
    type: str
    default: 'ON'
  postbodylimit:
    description:
      - Maximum allowed HTTP post body size, in bytes. Maximum supported value is
        10GB. Citrix recommends enabling streaming option for large values of post
        body limit (>20MB).
    type: int
    default: 20000000
  postbodylimitaction:
    choices:
      - block
      - log
      - stats
    description:
      - 'One or more Post Body Limit actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check. Must always
        be set.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -PostBodyLimitAction
        C(block)" followed by the other actions to be enabled.'
    type: list
    elements: str
  postbodylimitsignature:
    description:
      - Maximum allowed HTTP post body size for signature inspection for location
        HTTP_POST_BODY in the signatures, in bytes. Note that the changes in value
        could impact CPU and latency profile.
    type: int
    default: 2048
  protofileobject:
    description:
      - Name of the imported proto file.
    type: str
  refererheadercheck:
    choices:
      - 'OFF'
      - if_present
      - AlwaysExceptStartURLs
      - AlwaysExceptFirstRequest
    description:
      - 'Enable validation of Referer headers. '
      - 'Referer validation ensures that a web form that a user sends to your web
        site originally came from your web site, not an outside attacker. '
      - Although this parameter is part of the Start URL check, referer validation
        protects against cross-site request forgery (CSRF) attacks, not Start URL
        attacks.
    type: str
    default: 'OFF'
  relaxationrules:
    description:
      - Import all appfw relaxation rules
    type: bool
  replaceurlstring:
    description:
      - Replace matched url string with this action url string while restoring Relaxation
        Rules
    type: str
  requestcontenttype:
    description:
      - 'Default Content-Type header for requests. '
      - A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-)
        and underscore (_) characters.
    type: str
  responsecontenttype:
    description:
      - 'Default Content-Type header for responses. '
      - A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-)
        and underscore (_) characters.
    type: str
  rfcprofile:
    description:
      - Object name of the rfc profile.
    type: str
  semicolonfieldseparator:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Allow ';' as a form field separator in URL queries and POST form bodies.
    type: str
    default: 'OFF'
  sessionlessfieldconsistency:
    choices:
      - 'OFF'
      - 'ON'
      - postOnly
    description:
      - Perform sessionless Field Consistency Checks.
    type: str
    default: 'OFF'
  sessionlessurlclosure:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable session less URL Closure Checks.
      - 'This check is applicable to Profile Type: HTML.'
    type: str
    default: 'OFF'
  signatures:
    description:
      - Object name for signatures.
      - 'This check is applicable to Profile Type: HTML, XML.'
    type: str
  sqlinjectionaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more HTML SQL Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -SQLInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -SQLInjectionAction C(none)".'
    type: list
    elements: str
  sqlinjectionchecksqlwildchars:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for form fields that contain SQL wild chars .
    type: str
    default: 'OFF'
  sqlinjectiongrammar:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for SQL injection using SQL grammar
    type: str
    default: 'OFF'
  sqlinjectiononlycheckfieldswithsqlchars:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check only form fields that contain SQL special strings (characters) for injected
        SQL code.
      - Most SQL servers require a special string to activate an SQL request, so SQL
        code without a special string is harmless to most SQL servers.
    type: str
    default: 'ON'
  sqlinjectionparsecomments:
    choices:
      - checkall
      - ansi
      - nested
      - ansinested
    description:
      - 'Parse HTML comments and exempt them from the HTML SQL Injection check. You
        must specify the type of comments that the application firewall is to detect
        and exempt from this security check. Available settings function as follows:'
      - '* Check all - Check all content.'
      - '* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. '
      - '* Nested - Exempt content that is part of a C(nested) (Microsoft-style) comment.'
      - '* ANSI Nested - Exempt content that is part of any type of comment.'
    type: str
  sqlinjectionruletype:
    choices:
      - ALLOW
      - DENY
    description:
      - 'Specifies SQL Injection rule type: C(ALLOW)/C(DENY). If C(ALLOW) rule type
        is configured then allow list rules are used, if C(DENY) rule type is configured
        then deny rules are used.'
    type: str
    default: ALLOW
  sqlinjectiontransformspecialchars:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Transform injected SQL code. This setting configures the application firewall
        to disable SQL special strings instead of blocking the request. Since most
        SQL servers require a special string to activate an SQL keyword, in most cases
        a request that contains injected SQL code is safe if special strings are disabled.
      - 'CAUTION: Make sure that this parameter is set to C(ON) if you are configuring
        any SQL injection transformations. If it is set to C(OFF), no SQL injection
        transformations are performed regardless of any other settings.'
    type: str
    default: 'OFF'
  sqlinjectiontype:
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
    description:
      - 'Available SQL injection types. '
      - '-C(SQLSplChar)              : Checks for SQL Special Chars'
      - "-C(SQLKeyword)\t\t : Checks for SQL Keywords"
      - '-C(SQLSplCharANDKeyword)    : Checks for both and blocks if both are found'
      - '-C(SQLSplCharORKeyword)     : Checks for both and blocks if anyone is found'
      - '-C(None)                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: SQLSplCharANDKeyword
  starturlaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Start URL actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -startURLaction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -startURLaction C(none)".'
    type: list
    elements: str
  starturlclosure:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Toggle  the state of Start URL Closure.
    type: str
    default: 'OFF'
  streaming:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'Setting this option converts content-length form submission requests (requests
        with content-type "application/x-www-form-urlencoded" or "multipart/form-data")
        to chunked requests when atleast one of the following protections : Signatures,
        SQL injection protection, XSS protection, form field consistency protection,
        starturl closure, CSRF tagging, JSON SQL, JSON XSS, JSON DOS is enabled. Please
        make sure that the backend server accepts chunked requests before enabling
        this option. Citrix recommends enabling this option for large request sizes(>20MB).'
    type: str
    default: 'OFF'
  stripcomments:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Strip HTML comments.
      - 'This check is applicable to Profile Type: HTML.'
    type: str
    default: 'OFF'
  striphtmlcomments:
    choices:
      - none
      - all
      - exclude_script_tag
    description:
      - Strip HTML comments before forwarding a web page sent by a protected web site
        in response to a user request.
    type: str
    default: none
  stripxmlcomments:
    choices:
      - none
      - all
    description:
      - Strip XML comments before forwarding a web page sent by a protected web site
        in response to a user request.
    type: str
    default: none
  trace:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Toggle  the state of trace
    type: str
    default: 'OFF'
  type:
    choices:
      - HTML
      - XML
      - JSON
    description:
      - 'Application firewall profile type, which controls which security checks and
        settings are applied to content that is filtered with the profile. Available
        settings function as follows:'
      - '* C(HTML) - C(HTML)-based web sites.'
      - '* C(XML) -  C(XML)-based web sites and services.'
      - '* C(JSON) - C(JSON)-based web sites and services.'
      - '* C(HTML) C(XML) (Web 2.0) - Sites that contain both C(HTML) and C(XML) content,
        such as ATOM feeds, blogs, and RSS feeds.'
      - '* C(HTML) C(JSON)  - Sites that contain both C(HTML) and C(JSON) content.'
      - '* C(XML) C(JSON)   - Sites that contain both C(XML) and C(JSON) content.'
      - '* C(HTML) C(XML) C(JSON)   - Sites that contain C(HTML), C(XML) and C(JSON)
        content.'
    type: list
    elements: str
    default: HTML
  urldecoderequestcookies:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - URL Decode request cookies before subjecting them to SQL and cross-site scripting
        checks.
    type: str
    default: 'OFF'
  usehtmlerrorobject:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Send an imported HTML Error object to a user when a request is blocked, instead
        of redirecting the user to the designated Error URL.
    type: str
    default: 'OFF'
  verboseloglevel:
    choices:
      - pattern
      - patternPayload
      - patternPayloadHeader
    description:
      - Detailed Logging Verbose Log Level.
    type: str
    default: pattern
  xmlattachmentaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more XML Attachment actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLAttachmentAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLAttachmentAction C(none)".'
    type: list
    elements: str
  xmldosaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more XML Denial-of-Service (XDoS) actions. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLDoSAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLDoSAction C(none)".'
    type: list
    elements: str
  xmlerrorobject:
    description:
      - Name to assign to the XML Error Object, which the application firewall displays
        when a user request is blocked.
      - Must begin with a letter, number, or the underscore character \(_\), and must
        contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\),
        space \( \), at (@), equals \(=\), colon \(:\), and underscore characters.
        Cannot be changed after the XML error object is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks \(for example, "my XML error object" or 'my XML error object'\).
    type: str
  xmlerrorstatuscode:
    description:
      - Response status code associated with XML error page. Non-empty XML error object
        must be imported to the application firewall profile for the status code.
    type: int
    default: 200
  xmlerrorstatusmessage:
    description:
      - Response status message associated with XML error page
    type: str
  xmlformataction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more XML Format actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLFormatAction C(none)".'
    type: list
    elements: str
  xmlsoapfaultaction:
    choices:
      - none
      - block
      - log
      - remove
      - stats
    description:
      - 'One or more XML SOAP Fault Filtering actions. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - '* Remove - Remove all violations for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLSOAPFaultAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLSOAPFaultAction C(none)".'
    type: list
    elements: str
  xmlsqlinjectionaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more XML SQL Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLSQLInjectionAction C(none)".'
    type: list
    elements: str
  xmlsqlinjectionchecksqlwildchars:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check for form fields that contain SQL wild chars .
    type: str
    default: 'OFF'
  xmlsqlinjectiononlycheckfieldswithsqlchars:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Check only form fields that contain SQL special characters, which most SQL
        servers require before accepting an SQL command, for injected SQL.
    type: str
    default: 'ON'
  xmlsqlinjectionparsecomments:
    choices:
      - checkall
      - ansi
      - nested
      - ansinested
    description:
      - 'Parse comments in XML Data and exempt those sections of the request that
        are from the XML SQL Injection check. You must configure the type of comments
        that the application firewall is to detect and exempt from this security check.
        Available settings function as follows:'
      - '* Check all - Check all content.'
      - '* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. '
      - '* Nested - Exempt content that is part of a C(nested) (Microsoft-style) comment.'
      - '* ANSI Nested - Exempt content that is part of any type of comment.'
    type: str
    default: checkall
  xmlsqlinjectiontype:
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
    description:
      - Available SQL injection types.
      - '-C(SQLSplChar)              : Checks for SQL Special Chars'
      - '-C(SQLKeyword)              : Checks for SQL Keywords'
      - '-C(SQLSplCharANDKeyword)    : Checks for both and blocks if both are found'
      - '-C(SQLSplCharORKeyword)     : Checks for both and blocks if anyone is found'
    type: str
    default: SQLSplCharANDKeyword
  xmlvalidationaction:
    choices:
      - none
      - block
      - log
      - stats
    description:
      - 'One or more XML Validation actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check. '
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLValidationAction C(none)".'
    type: list
    elements: str
  xmlwsiaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more Web Services Interoperability (WSI) actions. Available settings
        function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Learn - Use the learning engine to generate a list of exceptions to this
        security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLWSIAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLWSIAction C(none)".'
    type: list
    elements: str
  xmlxssaction:
    choices:
      - none
      - block
      - learn
      - log
      - stats
    description:
      - 'One or more XML Cross-Site Scripting actions. Available settings function
        as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLXSSAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLXSSAction C(none)".'
    type: list
    elements: str
  appfwprofile_appfwconfidfield_binding:
    type: dict
    description: Bindings for appfwprofile_appfwconfidfield_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_blockkeyword_binding:
    type: dict
    description: Bindings for appfwprofile_blockkeyword_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_bypasslist_binding:
    type: dict
    description: Bindings for appfwprofile_bypasslist_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_cmdinjection_binding:
    type: dict
    description: Bindings for appfwprofile_cmdinjection_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_contenttype_binding:
    type: dict
    description: Bindings for appfwprofile_contenttype_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_cookieconsistency_binding:
    type: dict
    description: Bindings for appfwprofile_cookieconsistency_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_creditcardnumber_binding:
    type: dict
    description: Bindings for appfwprofile_creditcardnumber_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_crosssitescripting_binding:
    type: dict
    description: Bindings for appfwprofile_crosssitescripting_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_csrftag_binding:
    type: dict
    description: Bindings for appfwprofile_csrftag_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_denylist_binding:
    type: dict
    description: Bindings for appfwprofile_denylist_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_denyurl_binding:
    type: dict
    description: Bindings for appfwprofile_denyurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_excluderescontenttype_binding:
    type: dict
    description: Bindings for appfwprofile_excluderescontenttype_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_fakeaccount_binding:
    type: dict
    description: Bindings for appfwprofile_fakeaccount_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_fieldconsistency_binding:
    type: dict
    description: Bindings for appfwprofile_fieldconsistency_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_fieldformat_binding:
    type: dict
    description: Bindings for appfwprofile_fieldformat_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_fileuploadtype_binding:
    type: dict
    description: Bindings for appfwprofile_fileuploadtype_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_jsonblockkeyword_binding:
    type: dict
    description: Bindings for appfwprofile_jsonblockkeyword_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_jsoncmdurl_binding:
    type: dict
    description: Bindings for appfwprofile_jsoncmdurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_jsondosurl_binding:
    type: dict
    description: Bindings for appfwprofile_jsondosurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_jsonsqlurl_binding:
    type: dict
    description: Bindings for appfwprofile_jsonsqlurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_jsonxssurl_binding:
    type: dict
    description: Bindings for appfwprofile_jsonxssurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_logexpression_binding:
    type: dict
    description: Bindings for appfwprofile_logexpression_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_safeobject_binding:
    type: dict
    description: Bindings for appfwprofile_safeobject_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_sqlinjection_binding:
    type: dict
    description: Bindings for appfwprofile_sqlinjection_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_starturl_binding:
    type: dict
    description: Bindings for appfwprofile_starturl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_trustedlearningclients_binding:
    type: dict
    description: Bindings for appfwprofile_trustedlearningclients_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmlattachmenturl_binding:
    type: dict
    description: Bindings for appfwprofile_xmlattachmenturl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmldosurl_binding:
    type: dict
    description: Bindings for appfwprofile_xmldosurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmlsqlinjection_binding:
    type: dict
    description: Bindings for appfwprofile_xmlsqlinjection_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmlvalidationurl_binding:
    type: dict
    description: Bindings for appfwprofile_xmlvalidationurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmlwsiurl_binding:
    type: dict
    description: Bindings for appfwprofile_xmlwsiurl_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
  appfwprofile_xmlxss_binding:
    type: dict
    description: Bindings for appfwprofile_xmlxss_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
failed:
    description: Indicates if the module failed or not
    returned: always
    type: bool
    sample: false
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
