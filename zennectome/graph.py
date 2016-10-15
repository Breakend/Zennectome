import pandas as pd
from StringIO import StringIO
import igraph
import networkx as nx

class Zengraph:

    def __init__(self, connectivity_matrix):
        self.connectivity_matrix = connectivity_matrix
        self.igraph_representation = None
        self.networkx_representation = None

    @classmethod
    def from_stream(cls, stream, sep=","):
        if not stream:
            raise Exception("No data available. Please provide a filepath or a piped input for the connectivity matrix.")

        connectivity_matrix = pd.read_csv(StringIO(stream), sep=sep, chunksize=1, index_col=0)

        if connectivity_matrix.shape[0] != connectivity_matrix.shape[1]:
            raise Exception("The connectivity matrix must be square. Current shape: (%d, %d)" % connectivity_matrix.values.shape)

        return cls(connectivity_matrix)

    @classmethod
    def from_file(cls, filepath, sep=","):
        connectivity_matrix = pd.read_csv(filepath, sep=sep, index_col=0)

        if connectivity_matrix.values.shape[0] != connectivity_matrix.values.shape[1]:
            raise Exception("The connectivity matrix must be square. Current shape: (%d, %d)" % connectivity_matrix.values.shape)
        return cls(connectivity_matrix)

    def as_igraph(self):
        if not self.igraph_representation:
            A = self.connectivity_matrix.values
            g = igraph.Graph.Adjacency((A>0).tolist())
            g.es['weight'] = A[A.nonzero()]
            g.vs['name'] = self.connectivity_matrix.columns
            self.igraph_representation = g
        return self.igraph_representation

    def as_nx_graph(self):
        if not self.networkx_representation:
            G = nx.DiGraph()
            df = self.connectivity_matrix
            for col in df.columns:
                for x in range(0,len(df.columns)):
                    if df[col][x] != 0.0:
                        G.add_edge(df.columns[x],col, weight=df[col][x])
            self.networkx_representation = G
        return self.networkx_representation
