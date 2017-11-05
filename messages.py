# -*- python-indent-offset: 4 -*-
'''
messages: utilities for printing messages and other similar tasks
'''

__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import six


# Utility functions.
# .............................................................................

def msg(*args):
    '''Like the standard print(), but flushes the output immediately.
    This is useful when piping the output of a script, because Python by
    default will buffer the output in that situation and this makes it very
    difficult to see what is happening in real time.
    '''
    six.print_(*args, flush=True)


def update_progress(progress):
    '''Value of "progress" should be a float from 0 to 1.'''
    six.print_('\r[{0:10}] {1:.0f}%'.format('#' * int(progress * 10),
                                            progress*100), end='', flush=True)
