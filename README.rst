zennectome
========================

.. image:: https://travis-ci.org/Breakend/Zennectome.svg?branch=master
    :target: https://travis-ci.org/Breakend/Zennectome

This is a tool for analyzing networks in connectomics and neuroscience
research. It takes as input a connectivity matrix as a csv and outputs the
specified network analysis.


Usage
-----

Clone the repository:

    $ git clone <TODO>
    $ make install

Behavior
-----

    .. code-block:: console
    $ zennectome --help
    usage: zennectome [-h] [--separator SEPARATOR]
                                [--community_louvain | --community_walktrap | --community_spinglass]
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
      --community_louvain, -l
                            Run Louvain community detection on the given graph.
      --community_walktrap, -w
                            Run Walktrap community detection on the given graph.
      --community_spinglass, -s
                            Run spinglass community detection on the given graph.



