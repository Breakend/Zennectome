Tutorials
**************************

=================
Community Detection CLI
=================

Let's use the community detection CLI provided with Zennectome to find some communities!

For your convenience, an example.csv has been provided in the Zennectome/examples directory.

To get started simply run:

.. code-block:: console

    >>> git clone https://github.com/Breakend/Zennectome.git
    >>> cd Zennectome
    >>> python setup.py install

Once the tool is installed you should now have the zennectome-community CLI tool.

Let's go ahead and find some communities in the example.csv we gave you.

.. code-block:: console

    >>> zennectome-community examples/example.csv --separator ";" --louvain

Notice here we're passing in a custom separator because we use ";" in the csv to
delimit the items. And we are using Louvain Modularity Maximization to find a community.
This can similarly be done with other algorithms, for information see the help.

.. code-block:: console

    >>> zennectome-community --help

Alternatively, if you want to use this tool in a pipeline, you can pipe the CSV to the tool:

.. code-block:: console

    >>> cat examples/example.csv | zennectome-community --separator ";" --louvain

Which will do the exact same thing as reading the csv from the specified filename.
