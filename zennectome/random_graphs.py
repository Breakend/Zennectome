import igraph
import random

def degree_preserving_analysis(zengraph, metric, trials=1000, n=(500,5000)):
    """Runs a degree preserving rewire of the graph to generate

    :param zengraph: zengraph connecting the connectivity matrix to use
    :type arg1: :class:`zennectome.graph.Zengraph`
    :param metric: a lambda function to call of form zengraph : compute(zengraph)
    :type arg2: lambda function
    :param trials: number of randomization trials to run the metric on
    :type arg3: int
    :param n: range of rewiring trials
    :type arg4: tuple
    :returns: metric run on the real graph
    :rtype: int
    :returns: list of random graph values
    :rtype: list
    """
    # TODO: needs unit tests
    baseline = metric(zengraph)
    vals = list()
    # TODO: print progress bar
    for i in range(0, trials):
        g = zengraph.as_igraph()
        g.rewire(n=random.randrange(n[0], n[1]))
        _return = metric(zengraph.from_igraph(g))
        vals.append(_return)

    return baseline, vals
