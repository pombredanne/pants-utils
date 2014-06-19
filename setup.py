#!/usr/bin/env python

from distutils.core import setup

import pants_utils

setup(
    name='pants-utils',
    version=pants_utils.VERSION,
    packages=[
        'pants_utils',
        'pants_utils.tornado_utils',
        'pants_utils.django_utils',
    ],
)
