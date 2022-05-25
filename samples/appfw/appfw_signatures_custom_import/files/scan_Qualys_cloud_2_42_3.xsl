<?xml version="1.0" encoding="utf-8"?>

<!-- This xslt is tested and verified on Qulays cloud version 2.42.3 -->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">

    <xsl:template name="f_replaceAll">
        <xsl:param name="text" />
        <xsl:param name="replace" />
        <xsl:param name="by" />
        <xsl:choose>
            <xsl:when test="contains($text, $replace)">
                <xsl:value-of select="substring-before($text,$replace)" />
                <xsl:value-of select="$by" />
                <xsl:call-template name="f_replaceAll">
                    <xsl:with-param name="text" select="substring-after($text,$replace)" />
                    <xsl:with-param name="replace" select="$replace" />
                    <xsl:with-param name="by" select="$by" />
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$text" />
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- remove last /. or . or / -->
    <xsl:template name="f_removeLastSlashDot">
        <xsl:param name="p_url"/>
        <xsl:variable name="m_len" select="string-length($p_url)"></xsl:variable>
        <xsl:choose>
            <xsl:when test="substring($p_url,$m_len - 1,2)='/.'">
                <xsl:value-of select="substring($p_url,1,$m_len - 2)"/>
            </xsl:when>
            <xsl:when test="substring($p_url,$m_len,1)='.'">
                <xsl:value-of select="substring($p_url,1,$m_len - 1)"/>
            </xsl:when>
            <xsl:when test="substring($p_url,$m_len,1)='/'">
                <xsl:value-of select="substring($p_url,1,$m_len - 1)"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$p_url"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- regex given url -->
    <xsl:template name="f_regexPath">
        <xsl:param name="p_url"/>
        <xsl:variable name="m_url">
            <xsl:call-template name="f_replaceAll">
                <xsl:with-param name="text">
                    <xsl:call-template name="f_replaceAll">
                        <xsl:with-param name="text">
                            <xsl:call-template name="f_replaceAll">
                                <xsl:with-param name="text">
                                    <xsl:call-template name="f_replaceAll">
                                        <xsl:with-param name="text">
                                            <xsl:call-template name="f_replaceAll">
                                                <xsl:with-param name="text">
                                                    <xsl:call-template name="f_replaceAll">
                                                        <xsl:with-param name="text">
                                                            <xsl:call-template name="f_replaceAll">
                                                                <xsl:with-param name="text">
                                                                    <xsl:call-template name="f_replaceAll">
                                                                        <xsl:with-param name="text">
                                                                            <xsl:call-template name="f_replaceAll">
                                                                                <xsl:with-param name="text">
                                                                                    <xsl:call-template name="f_replaceAll">
                                                                                        <xsl:with-param name="text">
                                                                                            <xsl:call-template name="f_replaceAll">
                                                                                                <xsl:with-param name="text">
                                                                                                    <xsl:call-template name="f_replaceAll">
                                                                                                        <xsl:with-param name="text" select="$p_url"/>
                                                                                                        <xsl:with-param name="replace" select="'}'"/>
                                                                                                        <xsl:with-param name="by" select="'\}'"/>
                                                                                                    </xsl:call-template>
                                                                                                </xsl:with-param>
                                                                                                <xsl:with-param name="replace" select="']'"/>
                                                                                                <xsl:with-param name="by" select="'\]'"/>
                                                                                            </xsl:call-template>
                                                                                        </xsl:with-param>
                                                                                        <xsl:with-param name="replace" select="')'"/>
                                                                                        <xsl:with-param name="by" select="'\)'"/>
                                                                                    </xsl:call-template>
                                                                                </xsl:with-param>
                                                                                <xsl:with-param name="replace" select="'*'"/>
                                                                                <xsl:with-param name="by" select="'\*'"/>
                                                                            </xsl:call-template>
                                                                        </xsl:with-param>
                                                                        <xsl:with-param name="replace" select="'+'"/>
                                                                        <xsl:with-param name="by" select="'\+'"/>
                                                                    </xsl:call-template>
                                                                </xsl:with-param>
                                                                <xsl:with-param name="replace" select="'('"/>
                                                                <xsl:with-param name="by" select="'\('"/>
                                                            </xsl:call-template>
                                                        </xsl:with-param>
                                                        <xsl:with-param name="replace" select="'|'"/>
                                                        <xsl:with-param name="by" select="'\|'"/>
                                                    </xsl:call-template>
                                                </xsl:with-param>
                                                <xsl:with-param name="replace" select="'['"/>
                                                <xsl:with-param name="by" select="'\['"/>
                                            </xsl:call-template>
                                        </xsl:with-param>
                                        <xsl:with-param name="replace" select="'$'"/>
                                        <xsl:with-param name="by" select="'\$'"/>
                                    </xsl:call-template>
                                </xsl:with-param>
                                <xsl:with-param name="replace" select="'^'"/>
                                <xsl:with-param name="by" select="'\^'"/>
                            </xsl:call-template>
                        </xsl:with-param>
                        <xsl:with-param name="replace" select="'{'"/>
                        <xsl:with-param name="by" select="'\{'"/>
                    </xsl:call-template>
                </xsl:with-param>
                <xsl:with-param name="replace" select="'.'"/>
                <xsl:with-param name="by" select="'\.'"/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:value-of select="concat('^',$m_url,'($|/$|\?|/\?)')"/>
    </xsl:template>

    <xsl:template match="/">
        <xsl:text>&#10;</xsl:text>
        <SignaturesFile version="0">
            <xsl:text>&#10;</xsl:text>
            <Comment>Qualys</Comment>
            <Signatures>
                <xsl:text>&#10;</xsl:text>
                <xsl:for-each select="WAS_SCAN_REPORT/RESULTS/VULNERABILITY_LIST/VULNERABILITY">
                    <xsl:variable name="m_QID" select="QID"></xsl:variable>
                    <xsl:variable name="m_URI" select="PAYLOADS/PAYLOAD/REQUEST/URL"></xsl:variable>
                    <xsl:variable name="m_PARAMS" select="PARAM">
                    </xsl:variable>
                    <xsl:variable name="m_GROUP" select="../../../GLOSSARY/QID_LIST/QID[QID=$m_QID]/GROUP">
                    </xsl:variable>
                    <xsl:variable name="m_TITLE" select="../../../GLOSSARY/QID_LIST/QID[QID=$m_QID]/TITLE"></xsl:variable>
                    <xsl:variable name="m_severity_no" select="../../../GLOSSARY/QID_LIST/QID[QID=$m_QID]/SEVERITY"></xsl:variable>
                    <xsl:variable name="m_severity">
                        <xsl:choose>
                            <xsl:when test="m_severity_no='1'">Low</xsl:when>
                            <xsl:when test="m_severity_no='2'">Medium</xsl:when>
                            <xsl:when test="m_severity_no='3'">Medium</xsl:when>
                            <xsl:when test="m_severity_no='4'">Medium</xsl:when>
                            <xsl:when test="m_severity_no='5'">High</xsl:when>
                            <xsl:otherwise>Low</xsl:otherwise>
                        </xsl:choose>
                    </xsl:variable>

                    <xsl:choose>
                        <xsl:when test="$m_GROUP='SQL'">
                            <SignatureRule source="Qualys">
                                <xsl:attribute name="actions">block,log</xsl:attribute>
                                <xsl:attribute name="category">
                                    <xsl:value-of select="$m_GROUP"/>
                                </xsl:attribute>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$m_TITLE"/>
                                </xsl:attribute>
                                <xsl:attribute name="severity">
                                    <xsl:value-of select="'HIGH'"/>
                                </xsl:attribute>
                                <xsl:attribute name="harmscore">
                                    <xsl:value-of select="100"/>
                                </xsl:attribute>
                                <xsl:text>&#10;</xsl:text>
                                <LogString>
                                    <xsl:value-of select="$m_TITLE" />
                                </LogString>
                                <xsl:text>&#10;</xsl:text>
                                <Comment>
                                    <xsl:value-of select="concat('Qualys QID=',$m_QID)" />
                                </Comment>
                                <xsl:text>&#10;</xsl:text>
                                <PatternList>
                                    <xsl:text>&#10;</xsl:text>
                                    <RequestPatterns>
                                        <xsl:text>&#10;</xsl:text>
                                        <Pattern>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Location area="HTTP_FORM_FIELD">
                                                <xsl:text>&#10;&#9;</xsl:text>
                                                <URL type='Literal'>
                                                    <xsl:choose>
                                                        <xsl:when test="contains($m_URI,'?')">
                                                            <xsl:value-of select="substring-before($m_URI,'?')"/>
                                                        </xsl:when>
                                                        <xsl:otherwise>
                                                            <xsl:value-of select="$m_URI"/>
                                                        </xsl:otherwise>
                                                    </xsl:choose>
                                                </URL>
                                                <xsl:text>&#10;&#9;</xsl:text>
                                                <FieldName type='Literal'>
                                                    <xsl:value-of select="$m_PARAMS"/>
                                                </FieldName>
                                                <xsl:text>&#10;&#9;</xsl:text>
                                            </Location>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Match type="Injection"/>
                                            <xsl:text>&#10;</xsl:text>
                                        </Pattern>
                                        <xsl:text>&#10;</xsl:text>
                                    </RequestPatterns>
                                    <xsl:text>&#10;</xsl:text>
                                </PatternList>
                                <xsl:text>&#10;</xsl:text>
                            </SignatureRule>
                            <xsl:text>&#10;</xsl:text>
                        </xsl:when>

                        <xsl:when test="$m_GROUP='XSS'">
                            <SignatureRule source="Qualys">
                                <xsl:attribute name="actions">block,log</xsl:attribute>
                                <xsl:attribute name="category">
                                    <xsl:value-of select="$m_GROUP"/>
                                </xsl:attribute>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$m_TITLE"/>
                                </xsl:attribute>
                                <xsl:attribute name="severity">
                                    <xsl:value-of select="$m_severity"/>
                                </xsl:attribute>
                                <xsl:attribute name="harmscore">
                                    <xsl:value-of select="100"/>
                                </xsl:attribute>
                                <xsl:text>&#10;</xsl:text>
                                <LogString>
                                    <xsl:value-of select="$m_TITLE" />
                                </LogString>
                                <xsl:text>&#10;</xsl:text>
                                <Comment>
                                    <xsl:value-of select="concat('Qualys QID=',$m_QID)" />
                                </Comment>
                                <xsl:text>&#10;</xsl:text>
                                <PatternList>
                                    <xsl:text>&#10;</xsl:text>
                                    <RequestPatterns>
                                        <xsl:text>&#10;</xsl:text>
                                        <Pattern>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Location area="HTTP_FORM_FIELD">
                                                <xsl:text>&#10;&#9;</xsl:text>
                                                <URL type='Literal'>
                                                    <xsl:choose>
                                                        <xsl:when test="contains($m_URI,'?')">
                                                            <xsl:value-of select="substring-before($m_URI,'?')"/>
                                                        </xsl:when>
                                                        <xsl:otherwise>
                                                            <xsl:value-of select="$m_URI"/>
                                                        </xsl:otherwise>
                                                    </xsl:choose>
                                                </URL>
                                                <xsl:text>&#10;&#9;</xsl:text>
                                                <FieldName type='Literal'>
                                                    <xsl:value-of select="$m_PARAMS"/>
                                                </FieldName>
                                                <xsl:text>&#10;&#9;</xsl:text>
                                            </Location>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Match type="CrossSiteScripting"/>
                                            <xsl:text>&#10;</xsl:text>
                                        </Pattern>
                                        <xsl:text>&#10;</xsl:text>
                                    </RequestPatterns>
                                    <xsl:text>&#10;</xsl:text>
                                </PatternList>
                                <xsl:text>&#10;</xsl:text>
                            </SignatureRule>
                            <xsl:text>&#10;</xsl:text>
                        </xsl:when>

                        <xsl:when test="$m_GROUP='PATH' or $m_GROUP='INFO'">
                            <xsl:variable name="m_shortURI">
                                <xsl:call-template name="f_removeLastSlashDot">
                                    <xsl:with-param name="p_url">
                                        <xsl:choose>
                                            <xsl:when test="contains($m_URI,'?')">
                                                <xsl:value-of select="substring-before($m_URI,'?')"/>
                                            </xsl:when>
                                            <xsl:otherwise>
                                                <xsl:value-of select="$m_URI"/>
                                            </xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:with-param>
                                </xsl:call-template>
                            </xsl:variable>
                            <SignatureRule source="Qualys">
                                <xsl:attribute name="actions">block,log</xsl:attribute>
                                <xsl:attribute name="category">
                                    <xsl:value-of select="$m_GROUP"/>
                                </xsl:attribute>
                                <xsl:attribute name="type">
                                    <xsl:value-of select="$m_TITLE"/>
                                </xsl:attribute>
                                <xsl:attribute name="severity">
                                    <xsl:value-of select="$m_severity"/>
                                </xsl:attribute>
                                <xsl:attribute name="harmscore">
                                    <xsl:value-of select="10"/>
                                </xsl:attribute>
                                <xsl:text>&#10;</xsl:text>
                                <LogString>
                                    <xsl:value-of select="$m_TITLE" />
                                </LogString>
                                <xsl:text>&#10;</xsl:text>
                                <Comment>
                                    <xsl:value-of select="concat('Qualys QID=',$m_QID)" />
                                </Comment>
                                <xsl:text>&#10;</xsl:text>
                                <PatternList>
                                    <xsl:text>&#10;</xsl:text>
                                    <RequestPatterns>
                                        <xsl:text>&#10;</xsl:text>
                                        <Pattern>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Location area="HTTP_URL"></Location>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Match type="Literal">
                                                <xsl:value-of select="$m_shortURI"/>
                                            </Match>
                                            <xsl:text>&#10;</xsl:text>
                                        </Pattern>
                                        <xsl:text>&#10;</xsl:text>
                                        <Pattern>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Location area="HTTP_URL"></Location>
                                            <xsl:text>&#10;&#9;</xsl:text>
                                            <Match type="PCRE">
                                                <xsl:call-template name="f_regexPath">
                                                    <xsl:with-param name="p_url" select="$m_shortURI"/>
                                                </xsl:call-template>
                                            </Match>
                                            <xsl:text>&#10;</xsl:text>
                                        </Pattern>
                                        <xsl:text>&#10;</xsl:text>
                                    </RequestPatterns>
                                    <xsl:text>&#10;</xsl:text>
                                </PatternList>
                                <xsl:text>&#10;</xsl:text>
                            </SignatureRule>
                            <xsl:text>&#10;</xsl:text>
                        </xsl:when>

                    </xsl:choose>
                </xsl:for-each>
            </Signatures>
            <xsl:text>&#10;</xsl:text>
        </SignaturesFile>
        <xsl:text>&#10;</xsl:text>
    </xsl:template>
</xsl:stylesheet>
