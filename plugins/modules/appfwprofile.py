#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

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
    description:
      - 'Add the specified flags to cookies. Available settings function as follows:'
      - '* None - Do not add flags to cookies.'
      - '* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from
        accessing cookies.'
      - '* Secure - Add Secure flag to cookies.'
      - '* All - Add both HTTPOnly and Secure flags to cookies.'
    type: str
    default: none
    choices:
      - none
      - httpOnly
      - secure
      - all
  archivename:
    description:
      - Source for tar archive.
    type: str
  augment:
    description:
      - Augment Relaxation Rules during import
    type: bool
  blockkeywordaction:
    description:
      - 'Block Keyword action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -blockKeywordAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -blockKeywordAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - log
      - stats
  bufferoverflowaction:
    description:
      - 'One or more Buffer Overflow actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -bufferOverflowAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
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
    description:
      - Perform HTML entity encoding for any special characters in responses sent
        by your protected web sites.
    type: str
    default: true
    choices:
      - true
      - false
  ceflogging:
    description:
      - Enable CEF format logs for the profile.
    type: str
    choices:
      - true
      - false
  checkrequestheaders:
    description:
      - Check request headers as well as web forms for injected SQL and cross-site
        scripts.
    type: str
    choices:
      - true
      - false
  clientipexpression:
    description:
      - Expression to get the client IP.
    type: str
  cmdinjectionaction:
    description:
      - 'Command injection action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -cmdInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -cmdInjectionAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - log
      - stats
  cmdinjectiongrammar:
    description:
      - Check for CMD injection using CMD grammar
    type: str
    choices:
      - true
      - false
  cmdinjectiontype:
    description:
      - 'Available CMD injection types. '
      - '-CMDSplChar              : Checks for CMD Special Chars'
      - '-CMDKeyword              : Checks for CMD Keywords'
      - '-CMDSplCharANDKeyword    : Checks for both and blocks if both are found'
      - '-CMDSplCharORKeyword     : Checks for both and blocks if anyone is found,'
      - '-None                    : Disables checking using both CMD Special Char
        and Keyword'
    type: str
    default: CMDSplCharANDKeyword
    choices:
      - CMDSplChar
      - CMDKeyword
      - CMDSplCharORKeyword
      - CMDSplCharANDKeyword
      - None
  comment:
    description:
      - Any comments about the purpose of profile, or other useful information about
        the profile.
    type: str
  contenttypeaction:
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
        appfw profile -contentTypeaction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  cookieconsistencyaction:
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
        appfw profile -cookieConsistencyAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - learn
      - log
      - stats
  cookieencryption:
    description:
      - 'Type of cookie encryption. Available settings function as follows:'
      - '* None - Do not encrypt cookies.'
      - '* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.'
      - '* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.'
      - '* Encrypt All - Encrypt all cookies.'
    type: str
    default: none
    choices:
      - none
      - decryptOnly
      - encryptSessionOnly
      - encryptAll
  cookiehijackingaction:
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
        appfw profile -cookieHijackingAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - log
      - stats
  cookieproxying:
    description:
      - 'Cookie proxy setting. Available settings function as follows:'
      - '* None - Do not proxy cookies.'
      - '* Session Only - Proxy session cookies by using the Citrix ADC session ID,
        but do not proxy permanent cookies.'
    type: str
    default: none
    choices:
      - none
      - sessionOnly
  cookiesamesiteattribute:
    description:
      - Cookie Samesite attribute added to support adding cookie SameSite attribute
        for all set-cookies including appfw session cookies. Default value will be
        "SameSite=Lax".
    type: str
    default: LAX
    choices:
      - None
      - LAX
      - STRICT
  cookietransforms:
    description:
      - 'Perform the specified type of cookie transformation. '
      - 'Available settings function as follows: '
      - '* Encryption - Encrypt cookies.'
      - '* Proxying - Mask contents of server cookies by sending proxy cookie to users.'
      - '* Cookie flags - Flag cookies as HTTP only to prevent scripts on user''s
        browser from accessing and possibly modifying them.'
      - 'CAUTION: Make sure that this parameter is set to ON if you are configuring
        any cookie transformations. If it is set to OFF, no cookie transformations
        are performed regardless of any other settings.'
    type: str
    choices:
      - true
      - false
  creditcard:
    description:
      - Credit card types that the application firewall should protect.
    type: list
    elements: str
    default: none
    choices:
      - none
      - visa
      - mastercard
      - discover
      - amex
      - jcb
      - dinersclub
  creditcardaction:
    description:
      - 'One or more Credit Card actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -creditCardAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -creditCardAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - learn
      - log
      - stats
  creditcardmaxallowed:
    description:
      - This parameter value is used by the block action. It represents the maximum
        number of credit card numbers that can appear on a web page served by your
        protected web sites. Pages that contain more credit card numbers are blocked.
    type: int
  creditcardxout:
    description:
      - Mask any credit card number detected in a response by replacing each digit,
        except the digits in the final group, with the letter "X."
    type: str
    choices:
      - true
      - false
  crosssitescriptingaction:
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
        appfw profile -crossSiteScriptingAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  crosssitescriptingcheckcompleteurls:
    description:
      - Check complete URLs for cross-site scripts, instead of just the query portions
        of URLs.
    type: str
    choices:
      - true
      - false
  crosssitescriptingtransformunsafehtml:
    description:
      - 'Transform cross-site scripts. This setting configures the application firewall
        to disable dangerous HTML instead of blocking the request. '
      - 'CAUTION: Make sure that this parameter is set to ON if you are configuring
        any cross-site scripting transformations. If it is set to OFF, no cross-site
        scripting transformations are performed regardless of any other settings.'
    type: str
    choices:
      - true
      - false
  csrftagaction:
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
        appfw profile -CSRFTagAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - learn
      - log
      - stats
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
    choices:
      - basic
      - advanced
      - core
  denyurlaction:
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
        appfw profile -denyURLaction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  dosecurecreditcardlogging:
    description:
      - Setting this option logs credit card numbers in the response when the match
        is found.
    type: str
    default: true
    choices:
      - true
      - false
  dynamiclearning:
    description:
      - 'One or more security checks. Available options are as follows:'
      - '* SQLInjection - Enable dynamic learning for SQLInjection security check.'
      - '* CrossSiteScripting - Enable dynamic learning for CrossSiteScripting security
        check.'
      - '* fieldFormat - Enable dynamic learning for  fieldFormat security check.'
      - '* None - Disable security checks for all security checks.'
      - ''
      - 'CLI users: To enable dynamic learning on one or more security checks, type
        "set appfw profile -dynamicLearning" followed by the security checks to be
        enabled. To turn off dynamic learning on all security checks, type "set appfw
        profile -dynamicLearning none".'
    type: list
    elements: str
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
  enableformtagging:
    description:
      - Enable tagging of web form fields for use by the Form Field Consistency and
        CSRF Form Tagging checks.
    type: str
    default: true
    choices:
      - true
      - false
  errorurl:
    description:
      - URL that application firewall uses as the Error URL.
    type: str
  excludefileuploadfromchecks:
    description:
      - Exclude uploaded files from Form checks.
    type: str
    choices:
      - true
      - false
  exemptclosureurlsfromsecuritychecks:
    description:
      - Exempt URLs that pass the Start URL closure check from SQL injection, cross-site
        script, field format and field consistency security checks at locations other
        than headers.
    type: str
    default: true
    choices:
      - true
      - false
  fakeaccountdetection:
    description:
      - 'Fake account detection flag : ON/OFF. If set to ON fake account detection
        in enabled on ADC, if set to OFF fake account detection is disabled.'
    type: str
    choices:
      - true
      - false
  fieldconsistencyaction:
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
        appfw profile -fieldConsistencyAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - learn
      - log
      - stats
  fieldformataction:
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
        appfw profile -fieldFormatAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  fileuploadmaxnum:
    description:
      - Maximum allowed number of file uploads per form-submission request. The maximum
        setting (65535) allows an unlimited number of uploads.
    type: int
    default: 65535
  fileuploadtypesaction:
    description:
      - 'One or more file upload types actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -fileUploadTypeAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -fileUploadTypeAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  geolocationlogging:
    description:
      - Enable Geo-Location Logging in CEF format logs for the profile.
    type: str
    choices:
      - true
      - false
  grpcaction:
    description:
      - gRPC validation
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
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
        appfw profile -inferContentTypeXMLPayloadAction none". Please note "none"
        action cannot be used with any other action type.'
    type: list
    elements: str
    choices:
      - block
      - log
      - stats
      - none
  insertcookiesamesiteattribute:
    description:
      - Configure whether application firewall should add samesite attribute for set-cookies
    type: str
    choices:
      - true
      - false
  inspectcontenttypes:
    description:
      - 'One or more InspectContentType lists. '
      - '* application/x-www-form-urlencoded'
      - '* multipart/form-data'
      - '* text/x-gwt-rpc'
      - ''
      - 'CLI users: To enable, type "set appfw profile -InspectContentTypes" followed
        by the content types to be inspected.'
    type: list
    elements: str
    choices:
      - none
      - application/x-www-form-urlencoded
      - multipart/form-data
      - text/x-gwt-rpc
      - application/grpc
      - application/grpc-web-text
      - application/grpc-web+json
  inspectquerycontenttypes:
    description:
      - Inspect request query as well as web forms for injected SQL and cross-site
        scripts for following content types.
    type: list
    elements: str
    choices:
      - HTML
      - XML
      - JSON
      - OTHER
  invalidpercenthandling:
    description:
      - 'Configure the method that the application firewall uses to handle percent-encoded
        names and values. Available settings function as follows: '
      - '* apache_mode - Apache format.'
      - '* asp_mode - Microsoft ASP format.'
      - '* secure_mode - Secure format.'
    type: str
    default: secure_mode
    choices:
      - apache_mode
      - asp_mode
      - secure_mode
  jsonblockkeywordaction:
    description:
      - 'JSON Block Keyword action. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONBlockKeywordAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONBlockKeywordAction none".'
    type: list
    elements: str
    default: none
    choices:
      - none
      - block
      - log
      - stats
  jsoncmdinjectionaction:
    description:
      - 'One or more JSON CMD Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONCMDInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONCMDInjectionAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  jsoncmdinjectiongrammar:
    description:
      - Check for CMD injection using CMD grammar in JSON
    type: str
    choices:
      - true
      - false
  jsoncmdinjectiontype:
    description:
      - Available CMD injection types.
      - '-CMDSplChar              : Checks for CMD Special Chars'
      - '-CMDKeyword              : Checks for CMD Keywords'
      - '-CMDSplCharANDKeyword    : Checks for both and blocks if both are found'
      - '-CMDSplCharORKeyword     : Checks for both and blocks if anyone is found,'
      - '-None                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: CMDSplCharANDKeyword
    choices:
      - CMDSplChar
      - CMDKeyword
      - CMDSplCharORKeyword
      - CMDSplCharANDKeyword
      - None
  jsondosaction:
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
        appfw profile -JSONDoSAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
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
    description:
      - 'One or more JSON SQL Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -JSONSQLInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -JSONSQLInjectionAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  jsonsqlinjectiongrammar:
    description:
      - Check for SQL injection using SQL grammar in JSON
    type: str
    choices:
      - true
      - false
  jsonsqlinjectiontype:
    description:
      - Available SQL injection types.
      - '-SQLSplChar              : Checks for SQL Special Chars'
      - '-SQLKeyword              : Checks for SQL Keywords'
      - '-SQLSplCharANDKeyword    : Checks for both and blocks if both are found'
      - '-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found,'
      - '-None                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: SQLSplCharANDKeyword
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
  jsonxssaction:
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
        appfw profile -JSONXssAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  logeverypolicyhit:
    description:
      - Log every profile match, regardless of security checks results.
    type: str
    choices:
      - true
      - false
  matchurlstring:
    description:
      - Match this action url in archived Relaxation Rules to replace.
    type: str
  multipleheaderaction:
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
    choices:
      - block
      - keepLast
      - log
      - none
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
    description:
      - Optimize handle of HTTP partial requests i.e. those with range headers.
      - 'Available settings are as follows: '
      - '* ON  - Partial requests by the client result in partial requests to the
        backend server in most cases.'
      - '* OFF - Partial requests by the client are changed to full requests to the
        backend server'
    type: str
    default: true
    choices:
      - true
      - false
  overwrite:
    description:
      - Purge existing Relaxation Rules and replace during import
    type: bool
  percentdecoderecursively:
    description:
      - Configure whether the application firewall should use percentage recursive
        decoding
    type: str
    default: true
    choices:
      - true
      - false
  postbodylimit:
    description:
      - Maximum allowed HTTP post body size, in bytes. Maximum supported value is
        10GB. Citrix recommends enabling streaming option for large values of post
        body limit (>20MB).
    type: int
    default: 20000000
  postbodylimitaction:
    description:
      - 'One or more Post Body Limit actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check. Must always
        be set.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -PostBodyLimitAction
        block" followed by the other actions to be enabled.'
    type: list
    elements: str
    choices:
      - block
      - log
      - stats
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
    description:
      - 'Enable validation of Referer headers. '
      - 'Referer validation ensures that a web form that a user sends to your web
        site originally came from your web site, not an outside attacker. '
      - Although this parameter is part of the Start URL check, referer validation
        protects against cross-site request forgery (CSRF) attacks, not Start URL
        attacks.
    type: str
    choices:
      - false
      - if_present
      - AlwaysExceptStartURLs
      - AlwaysExceptFirstRequest
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
    description:
      - Allow ';' as a form field separator in URL queries and POST form bodies.
    type: str
    choices:
      - true
      - false
  sessionlessfieldconsistency:
    description:
      - Perform sessionless Field Consistency Checks.
    type: str
    choices:
      - false
      - true
      - postOnly
  sessionlessurlclosure:
    description:
      - Enable session less URL Closure Checks.
      - 'This check is applicable to Profile Type: HTML.'
    type: str
    choices:
      - true
      - false
  signatures:
    description:
      - Object name for signatures.
      - 'This check is applicable to Profile Type: HTML, XML.'
    type: str
  sqlinjectionaction:
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
        appfw profile -SQLInjectionAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  sqlinjectionchecksqlwildchars:
    description:
      - Check for form fields that contain SQL wild chars .
    type: str
    choices:
      - true
      - false
  sqlinjectiongrammar:
    description:
      - Check for SQL injection using SQL grammar
    type: str
    choices:
      - true
      - false
  sqlinjectiononlycheckfieldswithsqlchars:
    description:
      - Check only form fields that contain SQL special strings (characters) for injected
        SQL code.
      - Most SQL servers require a special string to activate an SQL request, so SQL
        code without a special string is harmless to most SQL servers.
    type: str
    default: true
    choices:
      - true
      - false
  sqlinjectionparsecomments:
    description:
      - 'Parse HTML comments and exempt them from the HTML SQL Injection check. You
        must specify the type of comments that the application firewall is to detect
        and exempt from this security check. Available settings function as follows:'
      - '* Check all - Check all content.'
      - '* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. '
      - '* Nested - Exempt content that is part of a nested (Microsoft-style) comment.'
      - '* ANSI Nested - Exempt content that is part of any type of comment.'
    type: str
    choices:
      - checkall
      - ansi
      - nested
      - ansinested
  sqlinjectionruletype:
    description:
      - 'Specifies SQL Injection rule type: ALLOW/DENY. If ALLOW rule type is configured
        then allow list rules are used, if DENY rule type is configured then deny
        rules are used.'
    type: str
    default: ALLOW
    choices:
      - ALLOW
      - DENY
  sqlinjectiontransformspecialchars:
    description:
      - Transform injected SQL code. This setting configures the application firewall
        to disable SQL special strings instead of blocking the request. Since most
        SQL servers require a special string to activate an SQL keyword, in most cases
        a request that contains injected SQL code is safe if special strings are disabled.
      - 'CAUTION: Make sure that this parameter is set to ON if you are configuring
        any SQL injection transformations. If it is set to OFF, no SQL injection transformations
        are performed regardless of any other settings.'
    type: str
    choices:
      - true
      - false
  sqlinjectiontype:
    description:
      - 'Available SQL injection types. '
      - '-SQLSplChar              : Checks for SQL Special Chars'
      - "-SQLKeyword\t\t : Checks for SQL Keywords"
      - '-SQLSplCharANDKeyword    : Checks for both and blocks if both are found'
      - '-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found'
      - '-None                    : Disables checking using both SQL Special Char
        and Keyword'
    type: str
    default: SQLSplCharANDKeyword
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
  starturlaction:
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
        appfw profile -startURLaction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  starturlclosure:
    description:
      - Toggle  the state of Start URL Closure.
    type: str
    choices:
      - true
      - false
  streaming:
    description:
      - 'Setting this option converts content-length form submission requests (requests
        with content-type "application/x-www-form-urlencoded" or "multipart/form-data")
        to chunked requests when atleast one of the following protections : Signatures,
        SQL injection protection, XSS protection, form field consistency protection,
        starturl closure, CSRF tagging, JSON SQL, JSON XSS, JSON DOS is enabled. Please
        make sure that the backend server accepts chunked requests before enabling
        this option. Citrix recommends enabling this option for large request sizes(>20MB).'
    type: str
    choices:
      - true
      - false
  stripcomments:
    description:
      - Strip HTML comments.
      - 'This check is applicable to Profile Type: HTML.'
    type: str
    choices:
      - true
      - false
  striphtmlcomments:
    description:
      - Strip HTML comments before forwarding a web page sent by a protected web site
        in response to a user request.
    type: str
    default: none
    choices:
      - none
      - all
      - exclude_script_tag
  stripxmlcomments:
    description:
      - Strip XML comments before forwarding a web page sent by a protected web site
        in response to a user request.
    type: str
    default: none
    choices:
      - none
      - all
  trace:
    description:
      - Toggle  the state of trace
    type: str
    choices:
      - true
      - false
  type:
    description:
      - 'Application firewall profile type, which controls which security checks and
        settings are applied to content that is filtered with the profile. Available
        settings function as follows:'
      - '* HTML - HTML-based web sites.'
      - '* XML -  XML-based web sites and services.'
      - '* JSON - JSON-based web sites and services.'
      - '* HTML XML (Web 2.0) - Sites that contain both HTML and XML content, such
        as ATOM feeds, blogs, and RSS feeds.'
      - '* HTML JSON  - Sites that contain both HTML and JSON content.'
      - '* XML JSON   - Sites that contain both XML and JSON content.'
      - '* HTML XML JSON   - Sites that contain HTML, XML and JSON content.'
    type: list
    elements: str
    default: HTML
    choices:
      - HTML
      - XML
      - JSON
  urldecoderequestcookies:
    description:
      - URL Decode request cookies before subjecting them to SQL and cross-site scripting
        checks.
    type: str
    choices:
      - true
      - false
  usehtmlerrorobject:
    description:
      - Send an imported HTML Error object to a user when a request is blocked, instead
        of redirecting the user to the designated Error URL.
    type: str
    choices:
      - true
      - false
  verboseloglevel:
    description:
      - Detailed Logging Verbose Log Level.
    type: str
    default: pattern
    choices:
      - pattern
      - patternPayload
      - patternPayloadHeader
  xmlattachmentaction:
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
        appfw profile -XMLAttachmentAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  xmldosaction:
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
        appfw profile -XMLDoSAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
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
    description:
      - 'One or more XML Format actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLFormatAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  xmlsoapfaultaction:
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
        appfw profile -XMLSOAPFaultAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - remove
      - stats
  xmlsqlinjectionaction:
    description:
      - 'One or more XML SQL Injection actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check.'
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLSQLInjectionAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  xmlsqlinjectionchecksqlwildchars:
    description:
      - Check for form fields that contain SQL wild chars .
    type: str
    choices:
      - true
      - false
  xmlsqlinjectiononlycheckfieldswithsqlchars:
    description:
      - Check only form fields that contain SQL special characters, which most SQL
        servers require before accepting an SQL command, for injected SQL.
    type: str
    default: true
    choices:
      - true
      - false
  xmlsqlinjectionparsecomments:
    description:
      - 'Parse comments in XML Data and exempt those sections of the request that
        are from the XML SQL Injection check. You must configure the type of comments
        that the application firewall is to detect and exempt from this security check.
        Available settings function as follows:'
      - '* Check all - Check all content.'
      - '* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment. '
      - '* Nested - Exempt content that is part of a nested (Microsoft-style) comment.'
      - '* ANSI Nested - Exempt content that is part of any type of comment.'
    type: str
    default: checkall
    choices:
      - checkall
      - ansi
      - nested
      - ansinested
  xmlsqlinjectiontype:
    description:
      - Available SQL injection types.
      - '-SQLSplChar              : Checks for SQL Special Chars'
      - '-SQLKeyword              : Checks for SQL Keywords'
      - '-SQLSplCharANDKeyword    : Checks for both and blocks if both are found'
      - '-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found'
    type: str
    default: SQLSplCharANDKeyword
    choices:
      - SQLSplChar
      - SQLKeyword
      - SQLSplCharORKeyword
      - SQLSplCharANDKeyword
      - None
  xmlvalidationaction:
    description:
      - 'One or more XML Validation actions. Available settings function as follows:'
      - '* Block - Block connections that violate this security check.'
      - '* Log - Log violations of this security check.'
      - '* Stats - Generate statistics for this security check.'
      - '* None - Disable all actions for this security check. '
      - ''
      - 'CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction"
        followed by the actions to be enabled. To turn off all actions, type "set
        appfw profile -XMLValidationAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - log
      - stats
  xmlwsiaction:
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
        appfw profile -XMLWSIAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
  xmlxssaction:
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
        appfw profile -XMLXSSAction none".'
    type: list
    elements: str
    choices:
      - none
      - block
      - learn
      - log
      - stats
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
