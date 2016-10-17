.. Zennectome documentation master file, created by
   sphinx-quickstart on Sun Oct 16 20:52:17 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Zennectome's documentation!
======================================

The goal of the Zennectome project is to create a python toolbox for graph theoretical
analysis of connectomes, focusing on neuroscience research. A secondary goal is to unify
the various graph analysis frameworks to make tools accessible in one place. Several command
line tools are provided for this purpose:

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
      
Contents:

.. toctree::
   :maxdepth: 2

   community_detection
   graph



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
