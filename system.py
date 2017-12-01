# -*- python-indent-offset: 4 -*-
'''
system: utilities for interacting with the computer system
'''

__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import contextlib
import magic
import os
from   subprocess import PIPE, DEVNULL, Popen
import sys
from   threading import Timer


# Utility functions.
# .............................................................................

def shell_cmd(args, max_time=5, env=None):
    # 'max_time' is in sec.
    # 'env' is a dictionary of extra environment variables to set.
    #   Values in 'env' will override values in the current environment.
    # Extended from original code at http://stackoverflow.com/a/10768774/743730

    def kill_proc(proc, timeout):
        timeout['value'] = True
        proc.kill()

    if env:
        new_env = os.environ.copy()
        for key, value in env.items():
            new_env[key] = value
        proc = Popen(args, stdout=PIPE, stderr=PIPE, stdin=PIPE,
                     preexec_fn=os.setsid, env=new_env)
    else:
        proc = Popen(args, stdout=PIPE, stderr=PIPE, stdin=PIPE,
                     preexec_fn=os.setsid)
    timeout = {'value': False}
    timer = Timer(max_time, kill_proc, [proc, timeout])
    timer.start()
    stdout, stderr = proc.communicate()
    timer.cancel()
    return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8")


def run(cmd, file):
    '''Run a command on the given file, using a temporary file to catch the
    output. Reads the converted file and returns the text.  Throws an
    exception if something goes wrong.  The text of cmd should use {0} for
    the input file and {1} for the temporary output file.
    '''
    out_file = os.path.join(os.getcwd(), file) + '.__tmp__'
    cmd_line = cmd.format(out_file, file)
    try:
        retval = os.system(cmd)
        if retval == 0:
            with open(out_file) as f:
                text = f.read()
                return text
        else:
            msg('*** command "{}" returned {}'.format(cmd, retval))
            return ''
    finally:
        os.unlink(out_file)


def file_magic(file):
    '''Deal with differences in Python magic's return value on different OSes.
    '''
    value = magic.from_file(file)
    if isinstance(value, str):
        return value
    else:
        try:
            return value.decode('utf-8')
        except UnicodeError:
            return value.decode('iso8859-1')


# We mainly need to redirect stderr, but best get everything into a file.
# This solution is from http://stackoverflow.com/a/6796752/743730

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


# This is from http://stackoverflow.com/a/22348885/743730

class Timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)