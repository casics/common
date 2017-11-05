# -*- python-indent-offset: 4 -*-
'''
network: network utilities
'''

__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import requests
from   requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings


# Utility functions.
# .............................................................................

def timed_get(url, timeout=10, verify=True):
    # Wrap requests.get() with a timeout.  Time is in sec.
    # 'verify' means whether to perform HTTPS certificate verification.
    with warnings.catch_warnings():
        # When we use verify=False, the underlying urllib3 library used by
        # the Python requests module will issue a warning about unverified
        # HTTPS requests.  If we don't care, then the warnings are a constant
        # annoyance.  See also this for a discussion:
        # https://github.com/kennethreitz/requests/issues/2214
        warnings.simplefilter("ignore", InsecureRequestWarning)
        return requests.get(url, timeout=timeout, verify=False)
