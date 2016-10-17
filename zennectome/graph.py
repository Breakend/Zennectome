import pandas as pd
from StringIO import StringIO
import igraph
import networkx as nx

class Zengraph:
    """Provides a wrapper for various graph representations in different packages
    """

    def __init__(self, connectivity_matrix):
        self.connectivity_matrix = connectivity_matrix
        self.igraph_representation = None
        self.networkx_representation = None

    @classmethod
    def from_stream(cls, stream, sep=","):
        """Creates a zengraph object from a text stream or stdin

        :param filepath: the filepath to the csv file
        :type arg1: str
        :param sep: the optional separator (defaults to ',' for csv)
        :type arg1: str
        :returns: a zengraph object
        :rtype: :class:`zennectome.graph.Zengraph`

        :Example:

        >>> from cStringIO import StringIO

        >>> csv_data = \"\"\"labels, label1, label2
                              label1, 0.47094534,  0.40249001
                              label2, 0.45562164,  0.37275901\"\"\"

        >>> from zennectome.graph import Zengraph
        >>> zengraph = Zengraph.from_stream(StringIO(csv_data))
        """
        if not stream:
            raise Exception("No data available. Please provide a filepath or a piped input for the connectivity matrix.")

        connectivity_matrix = pd.read_csv(stream, sep=sep, index_col=0)

        if connectivity_matrix.values.shape[0] != connectivity_matrix.values.shape[1]:
            raise Exception("The connectivity matrix must be square. Current shape: (%d, %d)" % connectivity_matrix.values.shape)

        return cls(connectivity_matrix)

    @classmethod
    def from_file(cls, filepath, sep=","):
        """Creates a zengraph object from a csv file

        :param filepath: the filepath to the csv file
        :type arg1: str
        :param sep: the optional separator (defaults to ',' for csv)
        :type arg1: str
        :returns: a zengraph object
        :rtype: :class:`zennectome.graph.Zengraph`

        :Example:

        >>> from zennectome.graph import Zengraph
        >>> zengraph = Zengraph.from_file('./examples/example.csv', sep=";")
        """
        connectivity_matrix = pd.read_csv(filepath, sep=sep, index_col=0)

        if connectivity_matrix.values.shape[0] != connectivity_matrix.values.shape[1]:
            raise Exception("The connectivity matrix must be square. Current shape: (%d, %d)" % connectivity_matrix.values.shape)
        return cls(connectivity_matrix)

    def as_igraph(self):
        """Returns and igraph representation of the zengraph
        """
        if not self.igraph_representation:
            A = self.connectivity_matrix.values
            g = igraph.Graph.Adjacency((A>0).tolist())
            g.es['weight'] = A[A.nonzero()]
            g.vs['name'] = self.connectivity_matrix.columns
            self.igraph_representation = g
        return self.igraph_representation

    def as_nx_graph(self):
        """Returns a networkx representation of the zengraph
        """
        if not self.networkx_representation:
            G = nx.DiGraph()
            df = self.connectivity_matrix
            for col in df.columns:
                for x in range(0,len(df.columns)):
                    if df[col][x] != 0.0:
                        G.add_edge(df.columns[x],col, weight=df[col][x])
            self.networkx_representation = G
        return self.networkx_representation
