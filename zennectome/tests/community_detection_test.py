from unittest import TestCase

from zennectome.community_detection import *
from zennectome.graph import Zengraph

class TestZenCommunityDetection(TestCase):
    def test_walktrap(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        clustering = walktrap(zengraph)

        self.assertEquals(clustering.number_of_clusters, 3)

    def test_spinglass(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        clustering = spinglass(zengraph)

        # spinglass is stochastic so should fall within range
        self.assertTrue(5 <= clustering.number_of_clusters <= 10)

    def test_louvain(self):
        zengraph = Zengraph.from_file('./examples/example.csv', sep=";")

        # Assert that the data was loaded properly
        clustering = louvain(zengraph)
        
        self.assertEquals(clustering.number_of_clusters, 5)
