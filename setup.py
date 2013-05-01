#!/usr/bin/env python

from distutils.core import setup

import sys
sys.path.append('src/')
from fetcher.version import __version__


setup(name='torrent_fetcher',
      version=__version__,
      description='Tool to fetch torrents from www.onlinetvrecorder.de.',
      author='Sven Klomp',
      author_email='mail@klomp.eu',
      url='https://none',
      packages=['fetcher'],
      package_dir={'fetcher': 'src/fetcher'},
      scripts=['src/bin/fetcher'],
      data_files=[('config', ['config/fetcher.cfg'])],
      license="GPLv2",
      platforms=["Linux"],
      long_description=""
     )

