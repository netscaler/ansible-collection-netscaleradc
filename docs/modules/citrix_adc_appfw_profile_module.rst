:orphan:

.. _citrix_adc_appfw_profile_module:

citrix_adc_appfw_profile - Manage Citrix ADC Web Application Firewall profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADC Web Application Firewall profiles.
- The module uses the NITRO API to make configuration changes to WAF policy labels on the target Citrix ADC.
- The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest
- Note that due to NITRO API limitations the module may incorrectly report a changed status when no configuration change has taken place.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - addcookieflags

        *(str)*
      - Choices:

          - none
          - httpOnly
          - secure
          - all
      - Add the specified flags to cookies. Available settings function as follows:

        * None - Do not add flags to cookies.

        * HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from accessing cookies.

        * Secure - Add Secure flag to cookies.

        * All - Add both HTTPOnly and Secure flags to cookies.
    * - archivename

        *(str)*
      -
      - Source for tar archive.

        Minimum length =  1

        Maximum length =  31
    * - bufferoverflowaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more Buffer Overflow actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -bufferOverflowAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -bufferOverflowAction none".
    * - bufferoverflowmaxcookielength

        *(str)*
      -
      - Maximum length, in characters, for cookies sent to your protected web sites. Requests with longer are blocked.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - bufferoverflowmaxheaderlength

        *(str)*
      -
      - Maximum length, in characters, for HTTP headers in requests sent to your protected web sites. with longer headers are blocked.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - bufferoverflowmaxurllength

        *(str)*
      -
      - Maximum length, in characters, for URLs on your protected web sites. Requests with longer URLs are

        Minimum value = ``0``

        Maximum value = ``65535``
    * - canonicalizehtmlresponse

        *(bool)*
      -
      - Perform HTML entity encoding for any special characters in responses sent by your protected web
    * - checkrequestheaders

        *(bool)*
      -
      - Check request headers as well as web forms for injected SQL and cross-site scripts.
    * - comment

        *(str)*
      -
      - Any comments about the purpose of profile, or other useful information about the profile.
    * - contenttype_bindings

        *(dict)*
      -
      - contenttype bindings
    * - contenttypeaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Content-type actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -contentTypeaction" followed by the to be enabled. To turn off all actions, type "set appfw profile -contentTypeaction none".
    * - cookieconsistency_bindings

        *(dict)*
      -
      - cookieconsistency bindings
    * - cookieconsistencyaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Cookie Consistency actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -cookieConsistencyAction" followed the actions to be enabled. To turn off all actions, type "set appfw profile -cookieConsistencyAction
    * - cookieencryption

        *(str)*
      - Choices:

          - none
          - decryptOnly
          - encryptSessionOnly
          - encryptAll
      - Type of cookie encryption. Available settings function as follows:

        * None - Do not encrypt cookies.

        * Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.

        * Encrypt Session Only - Encrypt session cookies, but not permanent cookies.

        * Encrypt All - Encrypt all cookies.
    * - cookieproxying

        *(str)*
      - Choices:

          - none
          - sessionOnly
      - Cookie proxy setting. Available settings function as follows:

        * None - Do not proxy cookies.

        * Session Only - Proxy session cookies by using the Citrix ADC session ID, but do not proxy permanent
    * - cookietransforms

        *(bool)*
      -
      - Perform the specified type of cookie transformation.

        Available settings function as follows:

        * Encryption - Encrypt cookies.

        * Proxying - Mask contents of server cookies by sending proxy cookie to users.

        * Cookie flags - Flag cookies as HTTP only to prevent scripts on user's browser from accessing and modifying them.

        CAUTION: Make sure that this parameter is set to ON if you are configuring any cookie If it is set to OFF, no cookie transformations are performed regardless of any other settings.
    * - creditcard

        *(list)*
      - Choices:

          - none
          - visa
          - mastercard
          - discover
          - amex
          - jcb
          - dinersclub
      - Credit card types that the application firewall should protect.
    * - creditcardaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Credit Card actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -creditCardAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -creditCardAction none".
    * - creditcardmaxallowed

        *(str)*
      -
      - This parameter value is used by the block action. It represents the maximum number of credit card that can appear on a web page served by your protected web sites. Pages that contain more credit card are blocked.

        Minimum value = ``0``

        Maximum value = ``255``
    * - creditcardnumber_bindings

        *(dict)*
      -
      - creditcardnumber bindings
    * - creditcardxout

        *(bool)*
      -
      - Mask any credit card number detected in a response by replacing each digit, except the digits in the group, with the letter "X.".
    * - crosssitescripting_bindings

        *(dict)*
      -
      - crosssitescripting bindings
    * - crosssitescriptingaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Cross-Site Scripting (XSS) actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -crossSiteScriptingAction" followed the actions to be enabled. To turn off all actions, type "set appfw profile -crossSiteScriptingAction
    * - crosssitescriptingcheckcompleteurls

        *(bool)*
      -
      - Check complete URLs for cross-site scripts, instead of just the query portions of URLs.
    * - crosssitescriptingtransformunsafehtml

        *(bool)*
      -
      - Transform cross-site scripts. This setting configures the application firewall to disable dangerous instead of blocking the request.

        CAUTION: Make sure that this parameter is set to ON if you are configuring any cross-site scripting If it is set to OFF, no cross-site scripting transformations are performed regardless of any other
    * - csrftag_bindings

        *(dict)*
      -
      - csrftag bindings
    * - csrftagaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available settings function as

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -CSRFTagAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -CSRFTagAction none".
    * - customsettings

        *(str)*
      -
      - Object name for custom settings.

        This check is applicable to Profile Type: HTML, XML. .

        Minimum length =  1
    * - defaultcharset

        *(str)*
      -
      - Default character set for protected web pages. Web pages sent by your protected web sites in response user requests are assigned this character set if the page does not already specify a character set. character sets supported by the application firewall are:

        * iso-8859-1 (English US)

        * big5 (Chinese Traditional)

        * gb2312 (Chinese Simplified)

        * sjis (Japanese Shift-JIS)

        * euc-jp (Japanese EUC-JP)

        * iso-8859-9 (Turkish)

        * utf-8 (Unicode)

        * euc-kr (Korean).

        Minimum length =  1

        Maximum length =  31
    * - defaultfieldformatmaxlength

        *(str)*
      -
      - Maximum length, in characters, for data entered into a field that is assigned the default field type.

        Minimum value = ``1``

        Maximum value = ``2147483647``
    * - defaultfieldformatminlength

        *(str)*
      -
      - Minimum length, in characters, for data entered into a field that is assigned the default field type.

        To disable the minimum and maximum length settings and allow data of any length to be entered into field, set this parameter to zero (0).

        Minimum value = ``0``

        Maximum value = ``2147483647``
    * - defaultfieldformattype

        *(str)*
      -
      - Designate a default field type to be applied to web form fields that do not have a field type assigned to them.

        Minimum length =  1
    * - defaults

        *(str)*
      - Choices:

          - basic
          - advanced
      - Default configuration to apply to the profile. Basic defaults are intended for standard content that little further configuration, such as static web site content. Advanced defaults are intended for content that requires significant specialized configuration, such as heavily scripted or dynamic

        CLI users: When adding an application firewall profile, you can set either the defaults or the type, not both. To set both options, create the profile by using the add appfw profile command, and then the set appfw profile command to configure the other option.
    * - denyurl_bindings

        *(dict)*
      -
      - denyurl bindings
    * - denyurlaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more Deny URL actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        NOTE: The Deny URL check takes precedence over the Start URL check. If you enable blocking for the URL check, the application firewall blocks any URL that is explicitly blocked by a Deny URL, even if same URL would otherwise be allowed by the Start URL check.

        CLI users: To enable one or more actions, type "set appfw profile -denyURLaction" followed by the to be enabled. To turn off all actions, type "set appfw profile -denyURLaction none".
    * - dosecurecreditcardlogging

        *(bool)*
      -
      - Setting this option logs credit card numbers in the response when the match is found.
    * - dynamiclearning

        *(list)*
      - Choices:

          - none
          - SQLInjection
          - CrossSiteScripting
          - fieldFormat
      - One or more security checks. Available options are as follows:

        * SQLInjection - Enable dynamic learning for SQLInjection security check.

        * CrossSiteScripting - Enable dynamic learning for CrossSiteScripting security check.

        * fieldFormat - Enable dynamic learning for  fieldFormat security check.

        * None - Disable security checks for all security checks.

        CLI users: To enable dynamic learning on one or more security checks, type "set appfw profile followed by the security checks to be enabled. To turn off dynamic learning on all security checks, "set appfw profile -dynamicLearning none".
    * - enableformtagging

        *(bool)*
      -
      - Enable tagging of web form fields for use by the Form Field Consistency and CSRF Form Tagging checks.
    * - errorurl

        *(str)*
      -
      - URL that application firewall uses as the Error URL.

        Minimum length =  1
    * - excludefileuploadfromchecks

        *(bool)*
      -
      - Exclude uploaded files from Form checks.
    * - excluderescontenttype_bindings

        *(dict)*
      -
      - excluderescontenttype bindings
    * - exemptclosureurlsfromsecuritychecks

        *(bool)*
      -
      - Exempt URLs that pass the Start URL closure check from SQL injection, cross-site script, field format field consistency security checks at locations other than headers.
    * - fieldconsistency_bindings

        *(dict)*
      -
      - fieldconsistency bindings
    * - fieldconsistencyaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Form Field Consistency actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -fieldConsistencyaction" followed the actions to be enabled. To turn off all actions, type "set appfw profile -fieldConsistencyAction
    * - fieldformat_bindings

        *(dict)*
      -
      - fieldformat bindings
    * - fieldformataction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Field Format actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of suggested web form fields and field format

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -fieldFormatAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -fieldFormatAction none".
    * - fileuploadmaxnum

        *(str)*
      -
      - Maximum allowed number of file uploads per form-submission request. The maximum setting (65535) an unlimited number of uploads.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - fileuploadtypesaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more file upload types actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -fileUploadTypeAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -fileUploadTypeAction none".
    * - htmlerrorobject

        *(str)*
      -
      - Name to assign to the HTML Error Object.

        Must begin with a letter, number, or the underscore character (_), and must contain only letters, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore Cannot be changed after the HTML error object is added.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my HTML error object" or 'my HTML error object').

        Minimum length =  1
    * - inspectcontenttypes

        *(list)*
      - Choices:

          - none
          - application/x-www-form-urlencoded
          - multipart/form-data
          - text/x-gwt-rpc
      - One or more InspectContentType lists.

        * application/x-www-form-urlencoded

        * multipart/form-data

        * text/x-gwt-rpc

        CLI users: To enable, type "set appfw profile -InspectContentTypes" followed by the content types to inspected.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - invalidpercenthandling

        *(str)*
      - Choices:

          - apache_mode
          - asp_mode
          - secure_mode
      - Configure the method that the application firewall uses to handle percent-encoded names and values. settings function as follows:

        * apache_mode - Apache format.

        * asp_mode - Microsoft ASP format.

        * secure_mode - Secure format.
    * - jsondosaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more JSON Denial-of-Service (JsonDoS) actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -JSONDoSAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -JSONDoSAction none".
    * - jsonerrorobject

        *(str)*
      -
      - Name to the imported JSON Error Object to be set on application firewall profile.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my JSON error object" or 'my JSON error object').

        Minimum length =  1
    * - jsonsqlinjectionaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more JSON SQL Injection actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -JSONSQLInjectionAction" followed the actions to be enabled. To turn off all actions, type "set appfw profile -JSONSQLInjectionAction
    * - jsonsqlinjectiontype

        *(str)*
      - Choices:

          - SQLSplChar
          - SQLKeyword
          - SQLSplCharORKeyword
          - SQLSplCharANDKeyword
      - Available SQL injection types.

        -SQLSplChar              : Checks for SQL Special Chars

        -SQLKeyword              : Checks for SQL Keywords

        -SQLSplCharANDKeyword    : Checks for both and blocks if both are found

        -SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.
    * - jsonxssaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more JSON Cross-Site Scripting actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -JSONXssAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -JSONXssAction none".
    * - logeverypolicyhit

        *(bool)*
      -
      - Log every profile match, regardless of security checks results.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - multipleheaderaction

        *(list)*
      - Choices:

          - block
          - keepLast
          - log
          - none
      - One or more multiple header actions. Available settings function as follows:

        * Block - Block connections that have multiple headers.

        * Log - Log connections that have multiple headers.

        * KeepLast - Keep only last header when multiple headers are present.

        CLI users: To enable one or more actions, type "set appfw profile -multipleHeaderAction" followed by actions to be enabled.
    * - name

        *(str)*
      -
      - Name for the profile. Must begin with a letter, number, or the underscore character (_), and must only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), (:), and underscore (_) characters. Cannot be changed after the profile is added.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my profile" or 'my profile').

        Minimum length =  1
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout

        *(float)*
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - optimizepartialreqs

        *(bool)*
      -
      - Optimize handle of HTTP partial requests i.e. those with range headers.

        Available settings are as follows:

        * ON - Partial requests by the client result in partial requests to the backend server in most cases.

        * OFF - Partial requests by the client are changed to full requests to the backend server.
    * - percentdecoderecursively

        *(bool)*
      -
      - Configure whether the application firewall should use percentage recursive decoding.
    * - postbodylimit

        *(str)*
      -
      - Maximum allowed HTTP post body size, in bytes.
    * - postbodylimitsignature

        *(str)*
      -
      - Maximum allowed HTTP post body size for signature inspection for location HTTP_POST_BODY in the in bytes.
    * - refererheadercheck

        *(str)*
      - Choices:

          - OFF
          - if_present
          - AlwaysExceptStartURLs
          - AlwaysExceptFirstRequest
      - Enable validation of Referer headers.

        Referer validation ensures that a web form that a user sends to your web site originally came from web site, not an outside attacker.

        Although this parameter is part of the Start URL check, referer validation protects against request forgery (CSRF) attacks, not Start URL attacks.
    * - requestcontenttype

        *(str)*
      -
      - Default Content-Type header for requests.

        A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_)

        Minimum length =  1

        Maximum length =  255
    * - responsecontenttype

        *(str)*
      -
      - Default Content-Type header for responses.

        A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_)

        Minimum length =  1

        Maximum length =  255
    * - rfcprofile

        *(str)*
      -
      - Object name of the rfc profile.

        Minimum length =  1
    * - safeobject_bindings

        *(dict)*
      -
      - safeobject bindings
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - semicolonfieldseparator

        *(bool)*
      -
      - Allow ';' as a form field separator in URL queries and POST form bodies. .
    * - sessionlessfieldconsistency

        *(str)*
      - Choices:

          - OFF
          - ON
          - postOnly
      - Perform sessionless Field Consistency Checks.
    * - sessionlessurlclosure

        *(bool)*
      -
      - Enable session less URL Closure Checks.

        This check is applicable to Profile Type: HTML. .
    * - signatures

        *(str)*
      -
      - Object name for signatures.

        This check is applicable to Profile Type: HTML, XML. .

        Minimum length =  1
    * - sqlinjection_bindings

        *(dict)*
      -
      - sqlinjection bindings
    * - sqlinjectionaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more HTML SQL Injection actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -SQLInjectionAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -SQLInjectionAction none".
    * - sqlinjectionchecksqlwildchars

        *(bool)*
      -
      - Check for form fields that contain SQL wild chars .
    * - sqlinjectiononlycheckfieldswithsqlchars

        *(bool)*
      -
      - Check only form fields that contain SQL special strings (characters) for injected SQL code.

        Most SQL servers require a special string to activate an SQL request, so SQL code without a special is harmless to most SQL servers.
    * - sqlinjectionparsecomments

        *(str)*
      - Choices:

          - checkall
          - ansi
          - nested
          - ansinested
      - Parse HTML comments and exempt them from the HTML SQL Injection check. You must specify the type of that the application firewall is to detect and exempt from this security check. Available settings as follows:

        * Check all - Check all content.

        * ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment.

        * Nested - Exempt content that is part of a nested (Microsoft-style) comment.

        * ANSI Nested - Exempt content that is part of any type of comment.
    * - sqlinjectiontransformspecialchars

        *(bool)*
      -
      - Transform injected SQL code. This setting configures the application firewall to disable SQL special instead of blocking the request. Since most SQL servers require a special string to activate an SQL in most cases a request that contains injected SQL code is safe if special strings are disabled.

        CAUTION: Make sure that this parameter is set to ON if you are configuring any SQL injection If it is set to OFF, no SQL injection transformations are performed regardless of any other settings.
    * - sqlinjectiontype

        *(str)*
      - Choices:

          - SQLSplChar
          - SQLKeyword
          - SQLSplCharORKeyword
          - SQLSplCharANDKeyword
      - Available SQL injection types.

        -SQLSplChar              : Checks for SQL Special Chars

        -SQLKeyword		 : Checks for SQL Keywords

        -SQLSplCharANDKeyword    : Checks for both and blocks if both are found

        -SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.
    * - starturl_bindings

        *(dict)*
      -
      - starturl bindings
    * - starturlaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Start URL actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -startURLaction" followed by the to be enabled. To turn off all actions, type "set appfw profile -startURLaction none".
    * - starturlclosure

        *(bool)*
      -
      - Toggle  the state of Start URL Closure.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - streaming

        *(bool)*
      -
      - Setting this option converts content-length form submission requests (requests with content-type or "multipart/form-data") to chunked requests when atleast one of the following protections : SQL protection, XSS protection, form field consistency protection, starturl closure, CSRF tagging is Please make sure that the backend server accepts chunked requests before enabling this option.
    * - stripcomments

        *(bool)*
      -
      - Strip HTML comments.

        This check is applicable to Profile Type: HTML. .
    * - striphtmlcomments

        *(str)*
      - Choices:

          - none
          - all
          - exclude_script_tag
      - Strip HTML comments before forwarding a web page sent by a protected web site in response to a user
    * - stripxmlcomments

        *(str)*
      - Choices:

          - none
          - all
      - Strip XML comments before forwarding a web page sent by a protected web site in response to a user
    * - trace

        *(bool)*
      -
      - Toggle  the state of trace.
    * - trustedlearningclients_bindings

        *(dict)*
      -
      - trustedlearningclients bindings
    * - type

        *(list)*
      - Choices:

          - HTML
          - XML
          - JSON
      - Application firewall profile type, which controls which security checks and settings are applied to that is filtered with the profile. Available settings function as follows:

        * HTML - HTML-based web sites.

        * XML -  XML-based web sites and services.

        * JSON - JSON-based web sites and services.

        * HTML XML (Web 2.0) - Sites that contain both HTML and XML content, such as ATOM feeds, blogs, and feeds.

        * HTML JSON  - Sites that contain both HTML and JSON content.

        * XML JSON   - Sites that contain both XML and JSON content.

        * HTML XML JSON   - Sites that contain HTML, XML and JSON content.
    * - urldecoderequestcookies

        *(bool)*
      -
      - URL Decode request cookies before subjecting them to SQL and cross-site scripting checks.
    * - usehtmlerrorobject

        *(bool)*
      -
      - Send an imported HTML Error object to a user when a request is blocked, instead of redirecting the to the designated Error URL.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - verboseloglevel

        *(str)*
      - Choices:

          - pattern
          - patternPayload
          - patternPayloadHeader
      - Detailed Logging Verbose Log Level.
    * - xmlattachmentaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more XML Attachment actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLAttachmentAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -XMLAttachmentAction none".
    * - xmlattachmenturl_bindings

        *(dict)*
      -
      - xmlattachmenturl bindings
    * - xmldosaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more XML Denial-of-Service (XDoS) actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLDoSAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -XMLDoSAction none".
    * - xmldosurl_bindings

        *(dict)*
      -
      - xmldosurl bindings
    * - xmlerrorobject

        *(str)*
      -
      - Name to assign to the XML Error Object, which the application firewall displays when a user request blocked.

        Must begin with a letter, number, or the underscore character (_), and must contain only letters, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore Cannot be changed after the XML error object is added.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my XML error object" or 'my XML error object').

        Minimum length =  1
    * - xmlformataction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more XML Format actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLFormatAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -XMLFormatAction none".
    * - xmlsoapfaultaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - remove
          - stats
      - One or more XML SOAP Fault Filtering actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        * Remove - Remove all violations for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLSOAPFaultAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -XMLSOAPFaultAction none".
    * - xmlsqlinjection_bindings

        *(dict)*
      -
      - xmlsqlinjection bindings
    * - xmlsqlinjectionaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more XML SQL Injection actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLSQLInjectionAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -XMLSQLInjectionAction none".
    * - xmlsqlinjectionchecksqlwildchars

        *(bool)*
      -
      - Check for form fields that contain SQL wild chars .
    * - xmlsqlinjectiononlycheckfieldswithsqlchars

        *(bool)*
      -
      - Check only form fields that contain SQL special characters, which most SQL servers require before an SQL command, for injected SQL.
    * - xmlsqlinjectionparsecomments

        *(str)*
      - Choices:

          - checkall
          - ansi
          - nested
          - ansinested
      - Parse comments in XML Data and exempt those sections of the request that are from the XML SQL check. You must configure the type of comments that the application firewall is to detect and exempt this security check. Available settings function as follows:

        * Check all - Check all content.

        * ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment.

        * Nested - Exempt content that is part of a nested (Microsoft-style) comment.

        * ANSI Nested - Exempt content that is part of any type of comment.
    * - xmlsqlinjectiontype

        *(str)*
      - Choices:

          - SQLSplChar
          - SQLKeyword
          - SQLSplCharORKeyword
          - SQLSplCharANDKeyword
      - Available SQL injection types.

        -SQLSplChar              : Checks for SQL Special Chars

        -SQLKeyword              : Checks for SQL Keywords

        -SQLSplCharANDKeyword    : Checks for both and blocks if both are found

        -SQLSplCharORKeyword     : Checks for both and blocks if anyone is found.
    * - xmlvalidationaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - One or more XML Validation actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLValidationAction" followed by actions to be enabled. To turn off all actions, type "set appfw profile -XMLValidationAction none".
    * - xmlvalidationurl_bindings

        *(dict)*
      -
      - xmlvalidationurl bindings
    * - xmlwsiaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more Web Services Interoperability (WSI) actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Learn - Use the learning engine to generate a list of exceptions to this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLWSIAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -XMLWSIAction none".
    * - xmlwsiurl_bindings

        *(dict)*
      -
      - xmlwsiurl bindings
    * - xmlxss_bindings

        *(dict)*
      -
      - xmlxss bindings
    * - xmlxssaction

        *(list)*
      - Choices:

          - none
          - block
          - learn
          - log
          - stats
      - One or more XML Cross-Site Scripting actions. Available settings function as follows:

        * Block - Block connections that violate this security check.

        * Log - Log violations of this security check.

        * Stats - Generate statistics for this security check.

        * None - Disable all actions for this security check.

        CLI users: To enable one or more actions, type "set appfw profile -XMLXSSAction" followed by the to be enabled. To turn off all actions, type "set appfw profile -XMLXSSAction none".



Examples
--------

.. code-block:: yaml+jinja
    
    - name: setup profile with basic presets
      delegate_to: localhost
      citrix_adc_appfw_profile:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: present
        name: profile_basic_1
        defaults: basic
    
    - name: setup profile with denyurl bindings
      delegate_to: localhost
      citrix_adc_appfw_profile:
        nitro_user: ''
        nitro_pass: ''
        nsip: ''
        state: present
        name: profile_basic_2
        denyurl_bindings:
          mode: exact
          attributes:
            - state: enabled
              denyurl: denyme.*
              comment: 'denyurl comment'
    
    - name: remove profile
      delegate_to: localhost
      citrix_adc_appfw_profile:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.1
        state: absent
        name: profile_basic_integration_test
        defaults: basic


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
