zennectome
========================

.. image:: https://travis-ci.org/Breakend/Zennectome.svg?branch=master
    :target: https://travis-ci.org/Breakend/Zennectome

This is a tool for analyzing networks in connectomics and neuroscience
research. It takes as input a connectivity matrix as a csv and outputs the
specified network analysis.


Install and Usage
-----

Note that installation assumes that you already have python and setuptools installed. Depending on your setup, may require sudo make install.

Clone the repository:

.. code-block:: console

    $ git clone https://github.com/Breakend/Zennectome.git && cd Zennectome
    $ make install
    $ zennectome-community examples/example.csv --separator ";" --walktrap

Tests
-----

Running tests requires having the dependencies installed on the system.
Nose is required to run the tests.

.. code-block:: tests

    make test

CLIs
-----

CLI tools are provided to interact with the library:

.. code-block:: console

    $ zennectome-community --help
    usage: zennectome-community [-h] [--separator SEPARATOR]
                                [--louvain | --walktrap | --spinglass]
                                [matrix_filepath]

    positional arguments:
      matrix_filepath       The filepath to the connectivity matrix. Must be all-
                            to-all and in delimited format. Alternatively, the
                            file may be streamed to stdin and piped here.

    optional arguments:
      -h, --help            show this help message and exit
      --separator SEPARATOR, -p SEPARATOR
                            Specify the separator used in the file, defaults to
                            ","
      --louvain, -l         Run Louvain community detection on the given graph.
      --walktrap, -w        Run Walktrap community detection on the given graph.
      --spinglass, -s       Run spinglass community detection on the given graph.

Docs
-----

See: https://breakend.github.io/Zennectome

Man Pages
-----
So installation doesn't require sudo and because every system is different, we don't
automatically install the man pages, but you may view them in the root directory of the
repository via:

.. code-block:: console

    $ man ./man/zennectome-community.man
