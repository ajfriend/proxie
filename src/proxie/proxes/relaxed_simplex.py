import numpy as np
from scipy.optimize import bisect

def pos(x):
    return np.clip(x, 0, None)

def prox(x0):
    """ Project x0 onto {x >= 0, sum(x) <= 1}.

    Note that the strict simplex would have sum(x) == 1.
    """
    x = pos(x0)
    if np.sum(x) <= 1:
        return x

    def foo(mu):
        return np.sum(pos(x0 - mu)) -  1

    max_val = np.max(x0)
    mu = bisect(foo, 0, max_val)

    return pos(x0 - mu)
