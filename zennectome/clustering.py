from networkx.algorithms.cluster import average_clustering

def average_clustering_coefficient(zengraph):
    """ Average clustering coefficient using NetworkX implementation"""
    return average_clustering(zengraph.as_nx_graph(convert_to_undirected=True), weight='weight')
