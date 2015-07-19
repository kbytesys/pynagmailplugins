# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='pynagmailplugins',
    packages=find_packages(),
    version='0.0.1',
    #scripts=['bin/pynagsystemd.py'],
    install_requires=[
        'nagiosplugin>=1.2',
    ],
    description='Nagios plugins that detect unusual mail flow.',
    author='Andrea Briganti',
    author_email='kbytesys@gmail.com',
    url='https://github.com/kbytesys/pynagmailplugins',
    download_url='https://github.com/kbytesys/pynagmailplugins/tarball/v0.0.1',
    keywords=['nagios', 'systemd', 'postfix', 'mail'],
    license='GNU GPL v2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Networking :: Monitoring'
    ],
)