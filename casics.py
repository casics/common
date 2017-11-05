# -*- python-indent-offset: 4 -*-
'''
casics: utilities for common CASICS-specific operations
'''
__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import os
import sys


# Utility functions for dealing with repo entries in our MongoDB database.
# -----------------------------------------------------------------------------

def e_path(entry):
    '''Given an entry, return a full path of the form "owner/repo-name".'''
    return entry['owner'] + '/' + entry['name']


def e_summary(entry):
    '''Summarize the full path and id number of the given entry.'''
    summary = '{} (#{})'.format(e_path(entry), entry['_id'])
    return summary.encode(sys.stdout.encoding, errors='replace').decode('ascii')


def e_languages(entry):
    '''Return the list of languages as a plain list of strings.'''
    if not entry['languages']:
        return []
    elif entry['languages'] == -1:
        return -1
    elif isinstance(entry['languages'], list):
        return [lang['name'] for lang in entry['languages']]
    else:
        # This shouldn't happen.
        return entry['languages']


# Other utilities to encapsulate common operations.
# .............................................................................

def generate_path(root, repo_id):
    '''Creates a path of the following form:
        nn/nn/nn/nn
    where n is an integer 0..9.  For example,
        00/00/00/01
        00/00/00/62
        00/15/63/99
    The full number read left to right (without the slashes) is the identifier
    of the repository (which is the same as the database key in our database).
    The numbers are zero-padded.  So for example, repository entry #7182480
    leads to a path of "07/18/24/80".

    The first argument, 'root', is a prefix added to the id-based path to
    create the complete final path.
    '''
    s = '{:08}'.format(int(repo_id))
    return os.path.join(root, s[0:2], s[2:4], s[4:6], s[6:8])
