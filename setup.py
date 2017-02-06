"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import macholib_patch

APP = ['src/LogHound.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': False, 'iconfile': 'icons/loghound.icns'}

setup(
    name="LogHound",
    version="1.0",
    description="WMBR Log Generator",
    author="Ali Mohammad and Dan Wheeler",
    url="http://code.google.com/p/loghound/",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)