import community
import igraph
import networkx as nx

def walktrap(zengraph):
    """returns a Cluster object containing the communities found via walktrap

    Uses the walktrap implementation from igraph:

    http://igraph.org/python/doc/igraph.Graph-class.html

    Based on:

    Pons, Pascal, and Matthieu Latapy. "Computing communities in large networks
    using random walks." International Symposium on Computer and Information
    Sciences. Springer Berlin Heidelberg, 2005.

    :param zengraph: zengraph connecting the connectivity matrix to use
    :type arg1: :class:`zennectome.graph.Zengraph`
    :returns: communities found
    :rtype: :class:`zennectome.community_detection.Cluster`

    :Example:

    >>> from zennectome.graph import Zengraph
    >>> from zennectome.community_detection import walktrap
    >>> zengraph = Zengraph.from_file('./examples/example.csv', sep=";")
    >>> clustering = walktrap(zengraph)
    """
    igraph_G = zengraph.as_igraph()
    walktrap_cluster = igraph_G.community_walktrap('weight')
    return Cluster.from_igraph_clustering(walktrap_cluster.as_clustering())

def spinglass(zengraph):
    """returns a Cluster object containing the communities found via spinglass

    Uses the walktrap implementation from igraph:

    http://igraph.org/python/doc/igraph.Graph-class.html

    Based on:

    Reichardt, Jorg, and Stefan Bornholdt. "Statistical mechanics of community
    detection." Physical Review E 74.1 (2006): 016110.

    :param zengraph: zengraph connecting the connectivity matrix to use
    :type arg1: :class:`zennectome.graph.Zengraph`
    :returns: communities found
    :rtype: :class:`zennectome.community_detection.Cluster`

    :Example:

    >>> from zennectome.graph import Zengraph
    >>> from zennectome.community_detection import spinglass
    >>> zengraph = Zengraph.from_file('./examples/example.csv', sep=";")
    >>> clustering = spinglass(zengraph)


    .. note:: Currently uses default values for all spinglass algorithm parameters
    """
    igraph_G = zengraph.as_igraph()
    spinglass_cluster = igraph_G.community_spinglass('weight')
    return Cluster.from_igraph_clustering(spinglass_cluster)

def louvain(zengraph):
    """returns a Cluster object containing the communities found via louvain

    Uses the louvain implementation from the networkx community package:

    http://perso.crans.org/aynaud/communities/

    Based on:

    Blondel, Vincent D., et al. "Fast unfolding of communities in
    large networks." Journal of statistical mechanics:
    theory and experiment 2008.10 (2008): P10008.

    :param zengraph: zengraph connecting the connectivity matrix to use
    :type arg1: :class:`zennectome.graph.Zengraph`
    :returns: communities found
    :rtype: :class:`zennectome.community_detection.Cluster`

    :Example:

    >>> from zennectome.graph import Zengraph
    >>> from zennectome.community_detection import louvain
    >>> zengraph = Zengraph.from_file('./examples/example.csv', sep=";")
    >>> clustering = louvain(zengraph)

    .. note:: This converts a directed graph to an undirected graph via
        summation of the edge weights before running louvain modularity
        maximization.
    """
    nx_graph = zengraph.as_nx_graph()

    g = nx.Graph()
    g.add_edges_from(nx_graph.edges_iter(), weight=0)

    for u, v, d in nx_graph.edges_iter(data=True):
        g[u][v]['weight'] += d['weight']

    community_dict_modularity = community.best_partition(g)
    return Cluster.from_nx_community(community_dict_modularity)

class Cluster:
    """Provides a wrapper for various community representations in different packages
    """
    def __init__(self, cluster):
        self.cluster = cluster

    @property
    def number_of_clusters(self):
        """Provides the number of communities in this clustering
        """
        return len(self.cluster)

    @classmethod
    def from_nx_community(cls, nx_community):
        """Creates a Cluster object from a network_x returned community
        """
        cluster = {}
        for node in nx_community.keys():
            if not nx_community[node] in cluster:
                cluster[nx_community[node]] = []
            cluster[nx_community[node]].append(node)

        return cls(cluster)

    @classmethod
    def from_igraph_clustering(cls, clustering):
        """Creates a Cluster object from an igraph returned community
        """
        cluster = {}
        i = 0
        for subgraph in clustering.subgraphs():
            cluster[i] = []
            for v in subgraph.vs["name"]:
                cluster[i].append(v)
            i += 1
        return cls(cluster)

    def print_cluster_as_csv(self):
        """Prints the cluster in csv format.

        Format is as follows:

        NodeA,CommunityLabel
        NodeB,CommunityLabelB
        """
        for community in self.cluster.keys():
            for node in self.cluster[community]:
                print("%s, %s" % (node, community))
