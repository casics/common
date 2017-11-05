# -*- python-indent-offset: 4 -*-
'''
messages: utilities for printing messages and other similar tasks
'''

__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import six
try:
    from termcolor import colored
except:
    pass


# Utility functions.
# .............................................................................

def update_progress(progress):
    '''Value of "progress" should be a float from 0 to 1.'''
    six.print_('\r[{0:10}] {1:.0f}%'.format('#' * int(progress * 10),
                                            progress*100), end='', flush=True)

def msg(text, flags=None, colorize=True):
    '''Like the standard print(), but flushes the output immediately and
    colorizes the output by default. Flushing immediately is useful when
    piping the output of a script, because Python by default will buffer the
    output in that situation and this makes it very difficult to see what is
    happening in real time.
    '''
    if colorize:
        print(colorcode(text, flags), flush=True)
    else:
        print(text, flush=True)


def colorcode(text, flags=None, colorize=True):
    (prefix, color, attributes) = color_codes(flags)
    if colorize:
        if attributes and color:
            return colored(text, color, attrs=attributes)
        elif color:
            return colored(text, color)
        elif attributes:
            return colored(text, attrs=attributes)
        else:
            return text
    elif prefix:
        return prefix + ': ' + text
    else:
        return text


def color_codes(flags):
    color  = ''
    prefix = ''
    attrib = []
    if type(flags) is not list:
        flags = [flags]
    if 'error' in flags:
        prefix = 'ERROR'
        color = 'red'
    if 'warning' in flags:
        prefix = 'WARNING'
        color = 'yellow'
    if 'info' in flags:
        color = 'green'
    if 'white' in flags:
        color = 'white'
    if 'blue' in flags:
        color = 'blue'
    if 'grey' in flags:
        color = 'grey'
    if 'cyan' in flags:
        color = 'cyan'
    if 'underline' in flags:
        attrib.append('underline')
    if 'bold' in flags:
        attrib.append('bold')
    if 'reverse' in flags:
        attrib.append('reverse')
    if 'dark' in flags:
        attrib.append('dark')
    return (prefix, color, attrib)
