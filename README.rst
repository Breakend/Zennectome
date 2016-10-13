zennectome [![Build Status](https://travis-ci.org/Breakend/Zennectome.svg?branch=master)](https://travis-ci.org/Breakend/Zennectome)
========================

This is a tool for analyzing networks in connectomics and neuroscience
research. It takes as input a connectivity matrix as a csv and outputs the
specified network analysis.


Usage
-----

Clone the repository:

    $ git clone <TODO>
    $ make install

Behavior
--------

Flexible invocation
*******************

The application can be run right from the source directory, in two different
ways:

1) Treating the bootstrap directory as a package *and* as the main script::

    $ python -m bootstrap arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f43d9f65a90>

2) Using the bootstrap-runner.py wrapper::

    $ ./bootstrap-runner.py arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f149554ead0>


Installation sets up bootstrap command
**************************************

Situation before installation::

    $ bootstrap
    bash: bootstrap: command not found

Installation right from the source tree (or via pip from PyPI)::

    $ python setup.py install

Now, the ``bootstrap`` command is available::

    $ bootstrap arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f366749a190>


On Unix-like systems, the installation places a ``bootstrap`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``bootstrap.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.
