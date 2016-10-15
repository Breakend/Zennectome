from unittest import TestCase

from zennectome.graph import Zengraph

class TestZenraph(TestCase):
    def test_loading_from_file(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        self.assertEquals(zengraph.connectivity_matrix.shape, (49,49))

    def try_loading_non_square_connectivity_matrix(self):
        self.assertRaises(Exception, Zengraph.from_file('./examples/bad.csv'))

    def test_igraph_representation(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        igraph_G = zengraph.as_igraph()
        self.assertEquals(len(igraph_G.vs), 49)
        # All zero weighted edges are pruned
        self.assertEquals(len(igraph_G.es), 1950)

    def test_networkx_representation(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")
        nx_G = zengraph.as_nx_graph()
        self.assertEquals(len(nx_G.nodes()), 49)
        # All zero weighted edges are pruned
        self.assertEquals(len(nx_G.edges()), 1950)
