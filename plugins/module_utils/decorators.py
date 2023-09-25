# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import functools

from .logger import log


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log("TRACE: ENTRY: {}() called with {}, {}".format(func.__name__, args, kwargs))
        original_result = func(*args, **kwargs)
        log("TRACE: EXIT: {}() returned {}".format(func.__name__, original_result))
        return original_result

    return wrapper
