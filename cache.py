# -*- python-indent-offset: 4 -*-
'''
cache_utils: utilities for caching data in pickle files.

'''
__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

from   .logger import *
import os
import pickle


# Cache utilities.
# .............................................................................

def cache_dir(orig_dir):
    path = orig_dir
    if path.endswith('/'):
        path = path[:-1]
    return path + '.casics_cache'


def cache_file(orig_dir, cache_name):
    file = cache_name + '.pickle'
    return os.path.join(cache_dir(orig_dir), file)


def save_cached_value(orig_dir, cache_name, data_structure):
    dest_dir  = cache_dir(orig_dir)
    dest_file = cache_file(orig_dir, cache_name)
    try:
        os.makedirs(dest_dir, exist_ok=True)
        with open(dest_file, 'wb') as pickle_file:
            pickle.dump(data_structure, pickle_file)
    except IOError as err:
        log = Logger().get_log()
        log.error('encountered error trying to dump pickle {}'.format(dest_file))
        log.error(err)
    except PickleError as err:
        log = Logger().get_log()
        log.error('pickling error for {}'.format(dest_file))
        log.error(err)


def cached_value(orig_dir, cache_name):
    cache = cache_file(orig_dir, cache_name)
    if not os.path.exists(cache):
        return None
    try:
        with open(cache, 'rb') as saved_elements:
            return pickle.load(saved_elements)
    except Exception as err:
        log = Logger().get_log()
        log.error('cache exists but unpickle failed for {}'.format(cache))
        log.error(err)
        return None
