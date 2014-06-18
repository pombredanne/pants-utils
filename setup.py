#!/usr/bin/env python

from distutils.core import setup

import pants_utils

setup(
    name='pants_utils',
    version=pants_utils.VERSION,
    packages=['pants_utils'],
)
