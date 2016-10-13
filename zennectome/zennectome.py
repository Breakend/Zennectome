# -*- coding: utf-8 -*-


"""zennectome.zennectome: provides entry point main()."""


__version__ = "0.1.0"


import sys
import argparse
from pprint import pprint

from .graph import Zengraph
from .community_detection import *

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('matrix_filepath', nargs='?', default=None, action="store",
                    help=('The filepath to the connectivity matrix. Must be all-to-all and in delimited format. '
                         'Alternatively, the file may be streamed to stdin and piped here.'))

    parser.add_argument('--separator', '-p', action='store', dest='separator', default=',',
                    help='Specify the separator used in the file, defaults to ","')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--community_louvain', '-l', action='store_true', dest='louvain', default=False,
                    help='Run Louvain community detection on the given graph.')
    group.add_argument('--community_walktrap', '-w', action='store_true', dest='walktrap', default=False,
                    help='Run Walktrap community detection on the given graph.')
    group.add_argument('--community_spinglass', '-s', action='store_true', dest='spinglass', default=False,
                    help='Run spinglass community detection on the given graph.')

    results = parser.parse_args()
    import pdb; pdb.set_trace()

    if results.matrix_filepath:
        # Not piping
        zengraph = Zengraph.from_file(results.matrix_filepath, results.separator)
    else:
        zengraph = Zengraph.from_stream(sys.stdin, results.separator)

    if results.louvain:
        clustering = louvain(zengraph) 
        pprint(clustering.cluster)
    elif results.walktrap:
        clustering = walktrap(zengraph) 
        pprint(clustering.cluster)
    elif results.spinglass:
        clustering = spinglass(zengraph) 
        pprint(clustering.cluster)

    return 0
