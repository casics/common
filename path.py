'''
path: file path utilities
'''
__version__ = '1.0.0'
__author__  = 'Michael Hucka <mhucka@caltech.edu>'
__email__   = 'mhucka@caltech.edu'
__license__ = 'GPLv3'

import contextlib
import os

def full_path(filename, subdir=None):
    '''Return a full path based on the current file or current working dir.
    'filename' is assumed to be a simple file name and not a path.  Optional
    'subdir' can be a subdirectory relative, to the current directory, where
    'filename' is found.
    '''
    if subdir and os.path.isabs(subdir):
        return os.path.join(subdir, filename)
    else:
        import inspect
        try:
            calling_file = inspect.getfile(sys._getframe(1))
            thisdir = os.path.dirname(os.path.realpath(calling_file))
        except:
            if '__file__' in globals():
                thisdir = os.path.dirname(os.path.realpath(__file__))
            else:
                thisdir = os.getcwd()
        if subdir:
            return os.path.join(os.path.join(thisdir, subdir), filename)
        else:
            return os.path.join(thisdir, filename)


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


@contextlib.contextmanager
def cwd_preserved():
    # Code based on http://stackoverflow.com/a/169112/743730
    curdir = os.getcwd()
    try: yield
    finally: os.chdir(curdir)
