import igraph
from networkx import betweenness_centrality

def betweenness(zennectome, average=True):
    """ Calculates the betweenness centrality of the zengraph"""
    return betweenness_centrality(zennectome.as_nx_graph(invert_weights=True), weight='weight')
