import pandas as pd
import StringIO
import igraph
import networkx as nx

class ZenGraph:

    def __init__(self):
        self.connectivity_matrix = None
        self.igraph_representation = None

    def from_csv_stream(self, stream, sep=","):
        #TODO: check dimensionality, should be square
        self.connectivity_matrix = pd.read_csv(StringIO(stream), sep=sep, header=None, chunksize=1)

    def from_csv_file(self, filename, sep=","):
        self.connectivity_matrix = pd.read_csv("mmc2.csv", sep=sep)

    def as_igraph(self):
        if not self.igraph_representation:
            A = self.connectivity_matrix.values
            g = igraph.Graph.Adjacency((A > 0).tolist())
            g.es['weight'] = A[A.nonzero()]
            g.vs['label'] = node_names
            self.igraph_representation = g 
        return self.igraph_representation

    def as_nx_graph(self):
        if not self.networkx_representation:
            G = nx.DiGraph()
            for col in df:
            if col == "labels":
                continue
            for x in range(0,len(df["labels"])):
                if df[col][x] != 0.0:
                G.add_edge(df["labels"][x],col, weight=df[col][x])
            self.networkx_representation = G
        return self.networkx_representation
