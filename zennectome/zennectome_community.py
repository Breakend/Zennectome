# -*- coding: utf-8 -*-


"""zennectome.zennectome_community: provides entry point for the community detection CLI"""


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
    group.add_argument('--louvain', '-l', action='store_true', dest='louvain', default=False,
                    help='Run Louvain community detection on the given graph.')
    group.add_argument('--walktrap', '-w', action='store_true', dest='walktrap', default=False,
                    help='Run Walktrap community detection on the given graph.')
    group.add_argument('--spinglass', '-s', action='store_true', dest='spinglass', default=False,
                    help='Run spinglass community detection on the given graph.')

    results = parser.parse_args()

    if results.matrix_filepath:
        # Not piping
        zengraph = Zengraph.from_file(results.matrix_filepath, results.separator)
    elif not sys.stdin.isatty():
        zengraph = Zengraph.from_stream(sys.stdin, results.separator)
    else:
        parser.print_help()
        return 1

    if results.louvain:
        clustering = louvain(zengraph)
        clustering.print_cluster_as_csv()
    elif results.walktrap:
        clustering = walktrap(zengraph)
        clustering.print_cluster_as_csv()
    elif results.spinglass:
        clustering = spinglass(zengraph)
        clustering.print_cluster_as_csv()
    else:
        print("\nSpecify community detection algorithm to use...\n")
        parser.print_help()
        return 1

    return 0


if __name__ == '__main__':
    main()
