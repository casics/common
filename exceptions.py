# -*- python-indent-offset: 4 -*-
'''
exceptions: exceptions used for general purposes in CASICS.
'''

__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'



# Exception classes.
# .............................................................................

class ShellCommandException(Exception):
    '''Exception indicating a shell command has failed.'''
    pass
