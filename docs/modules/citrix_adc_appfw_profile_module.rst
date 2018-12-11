:source: citrix_adc_appfw_profile.py

:orphan:

.. _citrix_adc_appfw_profile_module:


citrix_adc_appfw_profile - Manage Citrix ADC Web Application Firewall profiles
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.8.0

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

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <b>addcookieflags</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>httpOnly</li>
                                                                                                                                                                                                <li>secure</li>
                                                                                                                                                                                                <li>all</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Add the specified flags to cookies. Available settings function as follows:</div>
                                                    <div>* None - Do not add flags to cookies.</div>
                                                    <div>* HTTP Only - Add the HTTP Only flag to cookies, which prevents scripts from accessing cookies.</div>
                                                    <div>* Secure - Add Secure flag to cookies.</div>
                                                    <div>* All - Add both HTTPOnly and Secure flags to cookies.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>archivename</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Source for tar archive.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>bufferoverflowaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Buffer Overflow actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -bufferOverflowAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -bufferOverflowAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>bufferoverflowmaxcookielength</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum length, in characters, for cookies sent to your protected web sites. Requests with longer are blocked.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>bufferoverflowmaxheaderlength</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum length, in characters, for HTTP headers in requests sent to your protected web sites. with longer headers are blocked.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>bufferoverflowmaxurllength</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum length, in characters, for URLs on your protected web sites. Requests with longer URLs are</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>canonicalizehtmlresponse</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Perform HTML entity encoding for any special characters in responses sent by your protected web</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>checkrequestheaders</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check request headers as well as web forms for injected SQL and cross-site scripts.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>comment</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Any comments about the purpose of profile, or other useful information about the profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>contenttype_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>contenttype bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>contenttype</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>contenttypeaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Content-type actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -contentTypeaction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -contentTypeaction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cookieconsistency_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>cookieconsistency bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>cookieconsistency</div>
                                                    <div>isregex</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>cookieconsistencyaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Cookie Consistency actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -cookieConsistencyAction&quot; followed the actions to be enabled. To turn off all actions, type &quot;set appfw profile -cookieConsistencyAction</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cookieencryption</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>decryptOnly</li>
                                                                                                                                                                                                <li>encryptSessionOnly</li>
                                                                                                                                                                                                <li>encryptAll</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of cookie encryption. Available settings function as follows:</div>
                                                    <div>* None - Do not encrypt cookies.</div>
                                                    <div>* Decrypt Only - Decrypt encrypted cookies, but do not encrypt cookies.</div>
                                                    <div>* Encrypt Session Only - Encrypt session cookies, but not permanent cookies.</div>
                                                    <div>* Encrypt All - Encrypt all cookies.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cookieproxying</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>sessionOnly</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Cookie proxy setting. Available settings function as follows:</div>
                                                    <div>* None - Do not proxy cookies.</div>
                                                    <div>* Session Only - Proxy session cookies by using the NetScaler session ID, but do not proxy permanent</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cookietransforms</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Perform the specified type of cookie transformation.</div>
                                                    <div>Available settings function as follows:</div>
                                                    <div>* Encryption - Encrypt cookies.</div>
                                                    <div>* Proxying - Mask contents of server cookies by sending proxy cookie to users.</div>
                                                    <div>* Cookie flags - Flag cookies as HTTP only to prevent scripts on user&#x27;s browser from accessing and modifying them.</div>
                                                    <div>CAUTION: Make sure that this parameter is set to ON if you are configuring any cookie If it is set to OFF, no cookie transformations are performed regardless of any other settings.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>creditcard</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>visa</li>
                                                                                                                                                                                                <li>mastercard</li>
                                                                                                                                                                                                <li>discover</li>
                                                                                                                                                                                                <li>amex</li>
                                                                                                                                                                                                <li>jcb</li>
                                                                                                                                                                                                <li>dinersclub</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Credit card types that the application firewall should protect.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>creditcardaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Credit Card actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -creditCardAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -creditCardAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>creditcardmaxallowed</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>This parameter value is used by the block action. It represents the maximum number of credit card that can appear on a web page served by your protected web sites. Pages that contain more credit card are blocked.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>creditcardnumber_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>creditcardnumber bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>creditcardnumber</div>
                                                    <div>creditcardnumberurl</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>creditcardxout</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Mask any credit card number detected in a response by replacing each digit, except the digits in the group, with the letter &quot;X.&quot;</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>crosssitescripting_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>crosssitescripting bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>crosssitescripting</div>
                                                    <div>isregex_xss</div>
                                                    <div>formactionurl_xss</div>
                                                    <div>as_scan_location_xss</div>
                                                    <div>as_value_type_xss</div>
                                                    <div>as_value_expr_xss</div>
                                                    <div>isvalueregex_xss</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>crosssitescriptingaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Cross-Site Scripting (XSS) actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -crossSiteScriptingAction&quot; followed the actions to be enabled. To turn off all actions, type &quot;set appfw profile -crossSiteScriptingAction</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>crosssitescriptingcheckcompleteurls</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check complete URLs for cross-site scripts, instead of just the query portions of URLs.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>crosssitescriptingtransformunsafehtml</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Transform cross-site scripts. This setting configures the application firewall to disable dangerous instead of blocking the request.</div>
                                                    <div>CAUTION: Make sure that this parameter is set to ON if you are configuring any cross-site scripting If it is set to OFF, no cross-site scripting transformations are performed regardless of any other</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>csrftag_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>csrftag bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>csrftag</div>
                                                    <div>csrfformactionurl</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>csrftagaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Cross-Site Request Forgery (CSRF) Tagging actions. Available settings function as</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -CSRFTagAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -CSRFTagAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>customsettings</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Object name for custom settings.</div>
                                                    <div>This check is applicable to Profile Type: HTML, XML.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defaultcharset</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Default character set for protected web pages. Web pages sent by your protected web sites in response user requests are assigned this character set if the page does not already specify a character set. character sets supported by the application firewall are:</div>
                                                    <div>* iso-8859-1 (English US)</div>
                                                    <div>* big5 (Chinese Traditional)</div>
                                                    <div>* gb2312 (Chinese Simplified)</div>
                                                    <div>* sjis (Japanese Shift-JIS)</div>
                                                    <div>* euc-jp (Japanese EUC-JP)</div>
                                                    <div>* iso-8859-9 (Turkish)</div>
                                                    <div>* utf-8 (Unicode)</div>
                                                    <div>* euc-kr (Korean)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defaultfieldformatmaxlength</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum length, in characters, for data entered into a field that is assigned the default field type.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defaultfieldformatminlength</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Minimum length, in characters, for data entered into a field that is assigned the default field type.</div>
                                                    <div>To disable the minimum and maximum length settings and allow data of any length to be entered into field, set this parameter to zero (0).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defaultfieldformattype</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Designate a default field type to be applied to web form fields that do not have a field type assigned to them.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>defaults</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>basic</li>
                                                                                                                                                                                                <li>advanced</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Default configuration to apply to the profile. Basic defaults are intended for standard content that little further configuration, such as static web site content. Advanced defaults are intended for content that requires significant specialized configuration, such as heavily scripted or dynamic</div>
                                                    <div></div>
                                                    <div>CLI users: When adding an application firewall profile, you can set either the defaults or the type, not both. To set both options, create the profile by using the add appfw profile command, and then the set appfw profile command to configure the other option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>denyurl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>denyurl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>denyurl</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>denyurlaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Deny URL actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>NOTE: The Deny URL check takes precedence over the Start URL check. If you enable blocking for the URL check, the application firewall blocks any URL that is explicitly blocked by a Deny URL, even if same URL would otherwise be allowed by the Start URL check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -denyURLaction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -denyURLaction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>dosecurecreditcardlogging</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Setting this option logs credit card numbers in the response when the match is found.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>enableformtagging</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable tagging of web form fields for use by the Form Field Consistency and CSRF Form Tagging checks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>errorurl</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>URL that application firewall uses as the Error URL.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>excludefileuploadfromchecks</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Exclude uploaded files from Form checks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>excluderescontenttype_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>excluderescontenttype bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>excluderescontenttype</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>exemptclosureurlsfromsecuritychecks</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Exempt URLs that pass the Start URL closure check from SQL injection, cross-site script, field format field consistency security checks at locations other than headers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>fieldconsistency_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>fieldconsistency bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>fieldconsistency</div>
                                                    <div>isregex_ffc</div>
                                                    <div>formactionurl_ffc</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>fieldconsistencyaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Form Field Consistency actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -fieldConsistencyaction&quot; followed the actions to be enabled. To turn off all actions, type &quot;set appfw profile -fieldConsistencyAction</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>fieldformat_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>fieldformat bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>fieldformat</div>
                                                    <div>isregex_ff</div>
                                                    <div>formactionurl_ff</div>
                                                    <div>fieldtype</div>
                                                    <div>fieldformatminlength</div>
                                                    <div>fieldformatmaxlength</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>fieldformataction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Field Format actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of suggested web form fields and field format</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -fieldFormatAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -fieldFormatAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>fileuploadmaxnum</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum allowed number of file uploads per form-submission request. The maximum setting (65535) an unlimited number of uploads.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>htmlerrorobject</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name to assign to the HTML Error Object.</div>
                                                    <div>Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and characters. Cannot be changed after the HTML error object is added.</div>
                                                    <div></div>
                                                    <div>The following requirement applies only to the NetScaler CLI:</div>
                                                    <div>If the name includes one or more spaces, enclose the name in double or single quotation marks \(for &quot;my HTML error object&quot; or &#x27;my HTML error object&#x27;\).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>inspectcontenttypes</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>application/x-www-form-urlencoded</li>
                                                                                                                                                                                                <li>multipart/form-data</li>
                                                                                                                                                                                                <li>text/x-gwt-rpc</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more InspectContentType lists.</div>
                                                    <div>* application/x-www-form-urlencoded</div>
                                                    <div>* multipart/form-data</div>
                                                    <div>* text/x-gwt-rpc</div>
                                                    <div></div>
                                                    <div>CLI users: To enable, type &quot;set appfw profile -InspectContentTypes&quot; followed by the content types to inspected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>instance_ip</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.</div>
                                                    <div>It is meaningful only when having set <code>mas_proxy_call</code> to <code>true</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>invalidpercenthandling</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>apache_mode</li>
                                                                                                                                                                                                <li>asp_mode</li>
                                                                                                                                                                                                <li>secure_mode</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Configure the method that the application firewall uses to handle percent-encoded names and values. settings function as follows:</div>
                                                    <div>* apache_mode - Apache format.</div>
                                                    <div>* asp_mode - Microsoft ASP format.</div>
                                                    <div>* secure_mode - Secure format.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>logeverypolicyhit</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Log every profile match, regardless of security checks results.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>mas_proxy_call</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.</div>
                                                    <div>{&#x27;When true you must also define the following options&#x27;: &#x27;<em>nitro_auth_token</em>, <em>instance_ip</em>.&#x27;}</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>multipleheaderaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>keepLast</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>none</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more multiple header actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that have multiple headers.</div>
                                                    <div>* Log - Log connections that have multiple headers.</div>
                                                    <div>* KeepLast - Keep only last header when multiple headers are present.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -multipleHeaderAction&quot; followed by actions to be enabled.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>name</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the profile. Must begin with a letter, number, or the underscore character (_), and must only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), (:), and underscore (_) characters. Cannot be changed after the profile is added.</div>
                                                    <div></div>
                                                    <div>The following requirement applies only to the NetScaler CLI:</div>
                                                    <div>If the name includes one or more spaces, enclose the name in double or single quotation marks (for &quot;my profile&quot; or &#x27;my profile&#x27;).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nitro_auth_token</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The authentication token provided by a login operation.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, a, u, t, h, _, t, o, k, e, n</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nitro_pass</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The password with which to authenticate to the netscaler node.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, p, a, s, s</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nitro_protocol</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>http</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>https</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Which protocol to use when accessing the nitro API objects.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nitro_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">310</div>
                                    </td>
                                                                <td>
                                                                        <div>Time in seconds until a timeout error is thrown when establishing a new session with Netscaler</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nitro_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The username with which to authenticate to the netscaler node.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, u, s, e, r</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>nsip</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The ip address of the netscaler appliance where the nitro API calls will be made.</div>
                                                    <div>The port can be specified with the colon (:). E.g. 192.168.1.1:555.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, i, p</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>optimizepartialreqs</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Optimize handle of HTTP partial requests i.e. those with range headers.</div>
                                                    <div>Available settings are as follows:</div>
                                                    <div>* ON - Partial requests by the client result in partial requests to the backend server in most cases.</div>
                                                    <div>* OFF - Partial requests by the client are changed to full requests to the backend server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>percentdecoderecursively</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Configure whether the application firewall should use percentage recursive decoding</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>postbodylimit</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum allowed HTTP post body size, in bytes.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>refererheadercheck</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>OFF</li>
                                                                                                                                                                                                <li>if_present</li>
                                                                                                                                                                                                <li>AlwaysExceptStartURLs</li>
                                                                                                                                                                                                <li>AlwaysExceptFirstRequest</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable validation of Referer headers.</div>
                                                    <div>Referer validation ensures that a web form that a user sends to your web site originally came from web site, not an outside attacker.</div>
                                                    <div>Although this parameter is part of the Start URL check, referer validation protects against request forgery (CSRF) attacks, not Start URL attacks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>requestcontenttype</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Default Content-Type header for requests.</div>
                                                    <div>A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>responsecontenttype</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Default Content-Type header for responses.</div>
                                                    <div>A Content-Type header can contain 0-255 letters, numbers, and the hyphen (-) and underscore (_)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>safeobject_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>safeobject bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>safeobject</div>
                                                    <div>as_expression</div>
                                                    <div>maxmatchlength</div>
                                                    <div>action</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>save_config</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>If true the module will save the configuration on the netscaler node if it makes any changes.</div>
                                                    <div>The module will not save the configuration on the netscaler node if it made no changes.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>semicolonfieldseparator</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Allow &#x27;;&#x27; as a form field separator in URL queries and POST form bodies.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sessionlessfieldconsistency</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>OFF</li>
                                                                                                                                                                                                <li>ON</li>
                                                                                                                                                                                                <li>postOnly</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Perform sessionless Field Consistency Checks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sessionlessurlclosure</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable session less URL Closure Checks.</div>
                                                    <div>This check is applicable to Profile Type: HTML.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>signatures</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Object name for signatures.</div>
                                                    <div>This check is applicable to Profile Type: HTML, XML.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjection_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>sqlinjection bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>sqlinjection</div>
                                                    <div>isregex_sql</div>
                                                    <div>formactionurl_sql</div>
                                                    <div>as_scan_location_sql</div>
                                                    <div>as_value_type_sql</div>
                                                    <div>as_value_expr_sql</div>
                                                    <div>isvalueregex_sql</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectionaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more HTML SQL Injection actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -SQLInjectionAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -SQLInjectionAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectionchecksqlwildchars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check for form fields that contain SQL wild chars .</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectiononlycheckfieldswithsqlchars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check only form fields that contain SQL special strings (characters) for injected SQL code.</div>
                                                    <div>Most SQL servers require a special string to activate an SQL request, so SQL code without a special is harmless to most SQL servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectionparsecomments</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>checkall</li>
                                                                                                                                                                                                <li>ansi</li>
                                                                                                                                                                                                <li>nested</li>
                                                                                                                                                                                                <li>ansinested</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Parse HTML comments and exempt them from the HTML SQL Injection check. You must specify the type of that the application firewall is to detect and exempt from this security check. Available settings as follows:</div>
                                                    <div>* Check all - Check all content.</div>
                                                    <div>* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment.</div>
                                                    <div>* Nested - Exempt content that is part of a nested (Microsoft-style) comment.</div>
                                                    <div>* ANSI Nested - Exempt content that is part of any type of comment.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectiontransformspecialchars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Transform injected SQL code. This setting configures the application firewall to disable SQL special instead of blocking the request. Since most SQL servers require a special string to activate an SQL in most cases a request that contains injected SQL code is safe if special strings are disabled.</div>
                                                    <div>CAUTION: Make sure that this parameter is set to ON if you are configuring any SQL injection If it is set to OFF, no SQL injection transformations are performed regardless of any other settings.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sqlinjectiontype</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SQLSplChar</li>
                                                                                                                                                                                                <li>SQLKeyword</li>
                                                                                                                                                                                                <li>SQLSplCharORKeyword</li>
                                                                                                                                                                                                <li>SQLSplCharANDKeyword</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Available SQL injection types.</div>
                                                    <div>-SQLSplChar              : Checks for SQL Special Chars</div>
                                                    <div>-SQLKeyword		 : Checks for SQL Keywords</div>
                                                    <div>-SQLSplCharANDKeyword    : Checks for both and blocks if both are found</div>
                                                    <div>-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>starturl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>starturl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>starturl</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>starturlaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Start URL actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -startURLaction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -startURLaction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>starturlclosure</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Toggle  the state of Start URL Closure.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>state</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The state of the resource being configured by the module on the netscaler node.</div>
                                                    <div>When present the resource will be created if needed and configured according to the module&#x27;s parameters.</div>
                                                    <div>When absent the resource will be deleted from the netscaler node.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>streaming</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Setting this option converts content-length form submission requests (requests with content-type or &quot;multipart/form-data&quot;) to chunked requests when atleast one of the following protections : SQL protection, XSS protection, form field consistency protection, starturl closure, CSRF tagging is Please make sure that the backend server accepts chunked requests before enabling this option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>stripcomments</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Strip HTML comments.</div>
                                                    <div>This check is applicable to Profile Type: HTML.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>striphtmlcomments</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>all</li>
                                                                                                                                                                                                <li>exclude_script_tag</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Strip HTML comments before forwarding a web page sent by a protected web site in response to a user</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>stripxmlcomments</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>all</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Strip XML comments before forwarding a web page sent by a protected web site in response to a user</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>trace</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Toggle  the state of trace</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>trustedlearningclients_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>trustedlearningclients bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>trustedlearningclients</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>type</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>HTML</li>
                                                                                                                                                                                                <li>XML</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Application firewall profile type, which controls which security checks and settings are applied to that is filtered with the profile. Available settings function as follows:</div>
                                                    <div>* HTML - HTML-based web sites.</div>
                                                    <div>* XML - XML-based web sites and services.</div>
                                                    <div>* HTML XML (Web 2.0) - Sites that contain both HTML and XML content, such as ATOM feeds, blogs, and feeds.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>urldecoderequestcookies</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>URL Decode request cookies before subjecting them to SQL and cross-site scripting checks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>usehtmlerrorobject</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Send an imported HTML Error object to a user when a request is blocked, instead of redirecting the to the designated Error URL.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>validate_certs</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                                <td>
                                                                        <div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlattachmentaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML Attachment actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLAttachmentAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -XMLAttachmentAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlattachmenturl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmlattachmenturl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmlattachmenturl</div>
                                                    <div>xmlmaxattachmentsizecheck</div>
                                                    <div>xmlmaxattachmentsize</div>
                                                    <div>xmlattachmentcontenttypecheck</div>
                                                    <div>xmlattachmentcontenttype</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmldosaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML Denial-of-Service (XDoS) actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLDoSAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -XMLDoSAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmldosurl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmldosurl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmldosurl</div>
                                                    <div>xmlmaxelementdepthcheck</div>
                                                    <div>xmlmaxelementdepth</div>
                                                    <div>xmlmaxelementnamelengthcheck</div>
                                                    <div>xmlmaxelementnamelength</div>
                                                    <div>xmlmaxelementscheck</div>
                                                    <div>xmlmaxelements</div>
                                                    <div>xmlmaxelementchildrencheck</div>
                                                    <div>xmlmaxelementchildren</div>
                                                    <div>xmlmaxnodescheck</div>
                                                    <div>xmlmaxnodes</div>
                                                    <div>xmlmaxentityexpansionscheck</div>
                                                    <div>xmlmaxentityexpansions</div>
                                                    <div>xmlmaxentityexpansiondepthcheck</div>
                                                    <div>xmlmaxentityexpansiondepth</div>
                                                    <div>xmlmaxattributescheck</div>
                                                    <div>xmlmaxattributes</div>
                                                    <div>xmlmaxattributenamelengthcheck</div>
                                                    <div>xmlmaxattributenamelength</div>
                                                    <div>xmlmaxattributevaluelengthcheck</div>
                                                    <div>xmlmaxattributevaluelength</div>
                                                    <div>xmlmaxnamespacescheck</div>
                                                    <div>xmlmaxnamespaces</div>
                                                    <div>xmlmaxnamespaceurilengthcheck</div>
                                                    <div>xmlmaxnamespaceurilength</div>
                                                    <div>xmlmaxchardatalengthcheck</div>
                                                    <div>xmlmaxchardatalength</div>
                                                    <div>xmlmaxfilesizecheck</div>
                                                    <div>xmlmaxfilesize</div>
                                                    <div>xmlminfilesizecheck</div>
                                                    <div>xmlminfilesize</div>
                                                    <div>xmlblockpi</div>
                                                    <div>xmlblockdtd</div>
                                                    <div>xmlblockexternalentities</div>
                                                    <div>xmlsoaparraycheck</div>
                                                    <div>xmlmaxsoaparraysize</div>
                                                    <div>xmlmaxsoaparrayrank</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmlerrorobject</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name to assign to the XML Error Object, which the application firewall displays when a user request blocked.</div>
                                                    <div>Must begin with a letter, number, or the underscore character \(_\), and must contain only letters, and the hyphen \(-\), period \(.\) pound \(\#\), space \( \), at (@), equals \(=\), colon \(:\), and characters. Cannot be changed after the XML error object is added.</div>
                                                    <div></div>
                                                    <div>The following requirement applies only to the NetScaler CLI:</div>
                                                    <div>If the name includes one or more spaces, enclose the name in double or single quotation marks \(for &quot;my XML error object&quot; or &#x27;my XML error object&#x27;\).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlformataction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML Format actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLFormatAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -XMLFormatAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsoapfaultaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>remove</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML SOAP Fault Filtering actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div>* Remove - Remove all violations for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLSOAPFaultAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -XMLSOAPFaultAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjection_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmlsqlinjection bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmlsqlinjection</div>
                                                    <div>isregex_xmlsql</div>
                                                    <div>as_scan_location_xmlsql</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjectionaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML SQL Injection actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLSQLInjectionAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -XMLSQLInjectionAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjectionchecksqlwildchars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check for form fields that contain SQL wild chars .</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjectiononlycheckfieldswithsqlchars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Check only form fields that contain SQL special characters, which most SQL servers require before an SQL command, for injected SQL.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjectionparsecomments</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>checkall</li>
                                                                                                                                                                                                <li>ansi</li>
                                                                                                                                                                                                <li>nested</li>
                                                                                                                                                                                                <li>ansinested</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Parse comments in XML Data and exempt those sections of the request that are from the XML SQL check. You must configure the type of comments that the application firewall is to detect and exempt this security check. Available settings function as follows:</div>
                                                    <div>* Check all - Check all content.</div>
                                                    <div>* ANSI - Exempt content that is part of an ANSI (Mozilla-style) comment.</div>
                                                    <div>* Nested - Exempt content that is part of a nested (Microsoft-style) comment.</div>
                                                    <div>* ANSI Nested - Exempt content that is part of any type of comment.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlsqlinjectiontype</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SQLSplChar</li>
                                                                                                                                                                                                <li>SQLKeyword</li>
                                                                                                                                                                                                <li>SQLSplCharORKeyword</li>
                                                                                                                                                                                                <li>SQLSplCharANDKeyword</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Available SQL injection types.</div>
                                                    <div>-SQLSplChar              : Checks for SQL Special Chars</div>
                                                    <div>-SQLKeyword              : Checks for SQL Keywords</div>
                                                    <div>-SQLSplCharANDKeyword    : Checks for both and blocks if both are found</div>
                                                    <div>-SQLSplCharORKeyword     : Checks for both and blocks if anyone is found</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlvalidationaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML Validation actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLValidationAction&quot; followed by actions to be enabled. To turn off all actions, type &quot;set appfw profile -XMLValidationAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlvalidationurl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmlvalidationurl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmlvalidationurl</div>
                                                    <div>xmlvalidateresponse</div>
                                                    <div>xmlwsdl</div>
                                                    <div>xmladditionalsoapheaders</div>
                                                    <div>xmlendpointcheck</div>
                                                    <div>xmlrequestschema</div>
                                                    <div>xmlresponseschema</div>
                                                    <div>xmlvalidatesoapenvelope</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmlwsiaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more Web Services Interoperability (WSI) actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Learn - Use the learning engine to generate a list of exceptions to this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLWSIAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -XMLWSIAction none&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>xmlwsiurl_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmlwsiurl bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmlwsiurl</div>
                                                    <div>xmlwsichecks</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmlxss_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>xmlxss bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>exact</li>
                                                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>exact</code>&#x27;: None}</div>
                                                    <div>Any bindings existing in the target Citrix ADC that are not defined in the attributes list will be removed.</div>
                                                    <div>Any bindings not existing in the target Citrix ADC that are defined in the attributes list will be created.</div>
                                                    <div>Any existing bindings that are defined in the attributes list but have differing attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Any bindings defined in the attributes list that exist on the target Citrix ADC but have different attribute values will first be deleted and then recreated with the defined attribute values.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>xmlxss</div>
                                                    <div>isregex_xmlxss</div>
                                                    <div>as_scan_location_xmlxss</div>
                                                    <div>state</div>
                                                    <div>comment</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>xmlxssaction</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>block</li>
                                                                                                                                                                                                <li>learn</li>
                                                                                                                                                                                                <li>log</li>
                                                                                                                                                                                                <li>stats</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>One or more XML Cross-Site Scripting actions. Available settings function as follows:</div>
                                                    <div>* Block - Block connections that violate this security check.</div>
                                                    <div>* Log - Log violations of this security check.</div>
                                                    <div>* Stats - Generate statistics for this security check.</div>
                                                    <div>* None - Disable all actions for this security check.</div>
                                                    <div></div>
                                                    <div>CLI users: To enable one or more actions, type &quot;set appfw profile -XMLXSSAction&quot; followed by the to be enabled. To turn off all actions, type &quot;set appfw profile -XMLXSSAction none&quot;.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - For more information on using Ansible to manage Citrix NetScaler Network devices see https://www.ansible.com/ansible-netscaler.


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
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>loglines</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>list of logged messages by the module</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;message 1&#x27;, &#x27;message 2&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>msg</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>failure</td>
                <td>
                                            <div>Message detailing the failure reason</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Action does not exist</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



Maintenance
-----------

This module is flagged as **community** which means that it is maintained by the Ansible Community. See :ref:`Module Maintenance & Support <modules_support>` for more info.

For a list of other modules that are also maintained by the Ansible Community, see :ref:`here <community_supported>`.





Author
~~~~~~

- George Nikolopoulos (@giorgos-nikolopoulos)
- Sumanth Lingappa (@sumanth-lingappa)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_appfw_profile.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
