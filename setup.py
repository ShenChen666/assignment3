#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for assignment3.

    This file was generated with PyScaffold 3.0.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
# script_name = assignment3.module:function
# For example:
# fibonacci = assignment3.skeleton:run
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points={
              'console_scripts':['solve_led=led.led:main']
        },
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
