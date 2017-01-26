#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import wraps
import re
import logging

logger = logging.getLogger() # root logger

_debug = True if logger.getEffectiveLevel() <= logging.DEBUG else False

def time_me(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not _debug:
            return func(*args, **kwargs)
        start = time.time()
        retval = func(*args, **kwargs)
        end = time.time()
        print("Time for %s: %.2f seconds" % (func.__qualname__,end-start))
        return retval
    return wrapper

def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not _debug:
            return func(*args, **kwargs)
        pprint("Call to {}( {}, {} )".format(func.__qualname__,args, kwargs))
        return func(*args, **kwargs)
    return wrapper

def print_retval(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not _debug:
            return func(*args, **kwargs)
        retval = func(*args, **kwargs)
        pprint("{} returned {}".format(func.__qualname__,retval))
        return retval
    return wrapper

regexps = {
    'transcript_id': re.compile(r'transcript_id\s+"?(\w+)"?'),
    'exon_id': re.compile(r'exon_id\s+"?(\w+)"?'),
    'gene_name': re.compile(r'gene_name\s+"?(\w+)"?'),
}

def get_gtf_value(v,attr):
    regex = regexps.get(v,None)
    if re:
        match=regex.search(attr)
        if match:
            return match.group(1)
    return None


