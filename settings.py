# (c) Fugro GeoServices. MIT licensed, see LICENSE.rst.
from __future__ import absolute_import

import os


SOCKS = {
    'host': 'socket.dijkdata.nl',  # socket server host
    'port': 5008,
    'test_file_dst': '/home/shaoqing/testdata/socket/',
    'timeout': 200,
}


try:
    # Allow each environment to override these settings.
    from localsettings import *  # NOQA
except ImportError:
    pass
