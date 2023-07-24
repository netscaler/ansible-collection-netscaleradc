# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type

loglines = []


def log(msg):
    debug_level = msg.split(": ", 1)[0]
    if debug_level not in ["TRACE", "INFO", "WARNING", "ERROR", "DEBUG"]:
        msg = "DEBUG: " + msg
    loglines.append(msg)
