zennectome
========================

.. image:: https://travis-ci.org/Breakend/Zennectome.svg?branch=master
    :target: https://travis-ci.org/Breakend/Zennectome

This is a tool for analyzing networks in connectomics and neuroscience
research. It takes as input a connectivity matrix as a csv and outputs the
specified network analysis.


Install and Usage
-----

For Ubuntu:

Note that installation assumes that you already have python and setuptools installed.

Clone the repository:

.. code-block:: console

    $ git clone https://github.com/Breakend/Zennectome.git && cd Zennectome
    $ sudo make install
    $ zennectome-community examples/example.csv --separator ";" --walktrap

NOTE: On ubuntu systems there is a problem installing igraph (see link below). A workaround has been added to the Makefile which should resolve the issue. Because of this, make requires sudo now.

http://stackoverflow.com/questions/28435418/failing-to-install-python-igraph

.. code-block:: console

    sudo apt-get install -y libigraph0-dev

For macOS (because no workaround needed):

.. code-block:: console

    $ git clone https://github.com/Breakend/Zennectome.git && cd Zennectome
    $ sudo python setup.py install 
    $ zennectome-community examples/example.csv --separator ";" --walktrap

Tests
-----

Running tests requires having the dependencies installed on the system (note, may need sudo to run or install nose testing tool).

To run the tests:

.. code-block:: console

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

NOTE: Currently, all inputs are required to be in the csv format seen in examples/example.csv

Docs
-----

See: https://breakend.github.io/Zennectome

Examples
-----

Note, the examples/example.csv file was taken from the Supplementary material of: https://www.ncbi.nlm.nih.gov/pubmed/25866397

It was modified to avoid replicating the work.

Man Pages
-----
So installation doesn't require sudo and because every system is different, we don't
automatically install the man pages, but you may view them in the root directory of the
repository via:

.. code-block:: console

    $ man ./man/zennectome-community.man
