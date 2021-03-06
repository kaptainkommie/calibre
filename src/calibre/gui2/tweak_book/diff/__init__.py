#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2014, Kovid Goyal <kovid at kovidgoyal.net>'

from calibre.constants import plugins

def load_patience_module():
    p, err = plugins['_patiencediff_c']
    if err:
        raise ImportError('Failed to import the PatienceDiff C module with error: %r' % err)
    return p

def get_sequence_matcher():
    return load_patience_module().PatienceSequenceMatcher_c

