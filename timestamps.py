# -*- python-indent-offset: 4 -*-
'''
timestamps: utilities for working with timestamps
'''
__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

from datetime import datetime
from dateutil import parser
from time     import time, mktime


# Main code.
# .............................................................................
# Mongo date & time objects are in UTC.  (See here for examples:
# https://api.mongodb.org/python/current/examples/datetimes.html)
# However, those objects take up 48 bytes.  If we store date/time values
# as floats, they only take up 24 bytes.  Since every entry in the database
# has at least 2 dates, that means we can save 48 * 25,000,000 bytes = 1.2 GB
# (at least) by storing them as floats instead of the default date objects.

def canonicalize_timestamp(value):
    '''Returns a POSIX timestamp value in UTC.
    The value can be inverted using the following:

       from datetime import datetime
       datetime.utcfromtimestamp(thevalue)
    '''
    if isinstance(value, float):
        # Assume it's already a POSIX timestamp float in UTC.
        return value
    elif isinstance(value, str):
        # Assume ISO8601 format such as GitHub's: "2012-07-20T01:19:13Z"
        datetime_created_at = parser.parse(value)
        return mktime(datetime_created_at.utctimetuple())
    elif isinstance(value, datetime):
        return mktime(value.utctimetuple())
    else:
        # Should do more here, but not sure what.

        return value

def now_timestamp():
    '''Returns a UTC-aware POSIX date/time stamp for "now", as a float.'''
    return mktime(datetime.now().utctimetuple())


def timestamp_str(value):
    '''Returns a readable string from a floating point POSIX date/time stamp.'''
    if not value:
        return ''
    elif isinstance(value, float):
        # 2012-07-20T01:19:13Z
        return datetime.utcfromtimestamp(value).isoformat()
    else:
        raise ValueError('Expected a float but got "{}"'.format(value))
