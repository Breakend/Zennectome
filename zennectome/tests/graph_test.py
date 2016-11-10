from unittest import TestCase

from zennectome.graph import Zengraph
import numpy as np
import networkx as nx

class TestZengraph(TestCase):
    def test_loading_from_file(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        self.assertEquals(zengraph.connectivity_matrix.shape, (49,49))

    def test_loading_from_igraph(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        self.assertEquals(zengraph.connectivity_matrix.shape, (49,49))
        G = zengraph.as_igraph()
        zengraph2 = Zengraph.from_igraph(G)
        self.assertEquals(zengraph.connectivity_matrix.shape, (49,49))
        self.assertEquals(zengraph2.connectivity_matrix.shape, (49,49))
        em = nx.algorithms.isomorphism.numerical_edge_match('weight', 1)
        np.testing.assert_array_equal(zengraph.connectivity_matrix.as_matrix(), zengraph2.connectivity_matrix.as_matrix())
        self.assertTrue(nx.is_isomorphic(zengraph.as_nx_graph(), zengraph2.as_nx_graph(), edge_match=em))

    def test_load_from_stream(self):
        from cStringIO import StringIO
        csv_data = """labels, label1, label2
                      label1, 0.47094534,  0.40249001
                      label2, 0.45562164,  0.37275901"""

        zengraph = Zengraph.from_stream(StringIO(csv_data))
        self.assertEquals(zengraph.connectivity_matrix.shape, (2,2))

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
