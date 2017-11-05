# -*- python-indent-offset: 4 -*-
'''
dataset_pickle.py: Compressed pickle handling code.
'''
__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import os
import sys
import gzip
import pickle

if '__file__' in globals():
    thisdir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(thisdir, '../common'))
else:
    sys.path.append('../common')

from logger import *
from utils import full_path


def dataset_from_pickle(file):
    '''Return the contents of the compressed pickle file in 'file'.  The
    pickle is assumed to contain only one data structure.
    '''
    log = Logger().get_log()
    file = full_path(file)
    try:
        log.debug('reading data set from pickle file {}'.format(file))
        with gzip.open(file, 'rb') as pickle_file:
            return pickle.load(pickle_file)
    except pickle.PickleError as err:
        log.error('unpickle failed for {}'.format(file))
        log.error(err)
        return ({}, None)


def dataset_to_pickle(file, data_set):
    '''Save the contents of 'data_set' to the compressed pickle file 'file'.
    The pickle is assumed to contain only one data structure.
    '''
    log = Logger().get_log()
    file = full_path(file)
    try:
        log.debug('saving data set to pickle file {}'.format(file))
        with gzip.open(file, 'wb') as pickle_file:
            pickle.dump(data_set, pickle_file)
    except IOError as err:
        log.error('encountered error trying to dump pickle {}'.format(file))
        log.error(err)
    except pickle.PickleError as err:
        log.error('pickling error for {}'.format(file))
        log.error(err)
