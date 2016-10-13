# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('zennectome/zennectome.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "zennectome",
    packages = ["zennectome"],
    entry_points = {
        "console_scripts": ['zennectome = zennectome.bootstrap:main']
        },
    version = version,
    description = "Command line tool for analyzing connectivity matrices.",
    long_description = long_descr,
    author = "Peter Henderson",
    author_email = "peter.henderson@mail.mcgill.ca",
    url = "https://github.com/Breakend/Zennectome",
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'Cython',
        'pandas',
        'networkx',
        'python-igraph',
        'python-louvain'
    ],
    )
