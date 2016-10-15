import community
import igraph
import networkx as nx

def walktrap(zengraph):
    igraph_G = zengraph.as_igraph()
    walktrap_cluster = igraph_G.community_walktrap('weight')
    return Cluster.from_igraph_clustering(walktrap_cluster.as_clustering())

def spinglass(zengraph):
    igraph_G = zengraph.as_igraph()
    spinglass_cluster = igraph_G.community_spinglass('weight')
    return Cluster.from_igraph_clustering(spinglass_cluster)

def louvain(zengraph):
    nx_graph = zengraph.as_nx_graph()

    g = nx.Graph()
    g.add_edges_from(nx_graph.edges_iter(), weight=0)

    for u, v, d in nx_graph.edges_iter(data=True):
        g[u][v]['weight'] += d['weight']

    community_dict_modularity = community.best_partition(g)
    return Cluster.from_nx_community(community_dict_modularity)

class Cluster:
    def __init__(self, cluster):
        self.cluster = cluster

    @property
    def number_of_clusters(self):
        return len(self.cluster)

    @classmethod
    def from_nx_community(cls, nx_community):
        cluster = {}
        for node in nx_community.keys():
            if not nx_community[node] in cluster:
                cluster[nx_community[node]] = []
            cluster[nx_community[node]].append(node)

        return cls(cluster)

    @classmethod
    def from_igraph_clustering(cls, clustering):
        cluster = {}
        i = 0
        for subgraph in clustering.subgraphs():
            i += 1
            cluster[i] = []
            for v in subgraph.vs["name"]:
                cluster[i].append(v)
        return cls(cluster)
