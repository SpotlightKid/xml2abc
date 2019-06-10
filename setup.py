#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from io import open
from setuptools import setup


def read(*paths):
    with open(os.path.join(*paths), encoding='utf-8') as fp:
        return fp.read()


classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Other Audience
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Operating System :: MacOS
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: POSIX :: Linux
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: Implementation :: CPython
Topic :: Multimedia :: Sound/Audio :: Conversion
Topic :: Text Processing
Topic :: Utilities
"""

setup(
    name='xml2abc',
    version='139',
    author='Willem G. Vree',
    author_email='willem179 <at> yahoo <dot> com',
    description='A command line utility that translates MusicXML into ABC+ notation',
    maintainer='Christopher Arndt',
    maintainer_email='info@chrisarndt.de',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license='LGPL',
    url='https://wim.vree.org/svgParse/xml2abc.html',
    classifiers=[c for c in (c.strip() for c in classifiers.splitlines())
                 if c and not c.startswith('#')],
    py_modules=['xml2abc'],
    entry_points={
        'console_scripts': [
            'xml2abc = xml2abc:main',
        ]
    },
    zip_safe=True
)
