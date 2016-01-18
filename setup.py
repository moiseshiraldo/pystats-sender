import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name='stats-sender',
  version='0.2.0-alpha',
  description='A Python stats collector and sender for Statsd',
  long_description=read('README.rst'),
  url='https://github.com/moiseshiraldo/pystats-sender',
  author='Moises Hiraldo',
  author_email='moiseshiraldo@gmail.com',
  license='Apache Software License 2.0',
  packages=['stats_sender'],
  install_requires=['statsd'],
  scripts=['bin/stats-sender.py'],
  data_files=[('/etc/stats-sender/', ['stats_sender/settings.py'])],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: System :: Monitoring',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Programming Language :: Python :: 2.7',
  ],
)