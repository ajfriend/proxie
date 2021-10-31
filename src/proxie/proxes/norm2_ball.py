import numpy as np

def form_prox(c, r=1):
    """
    Return prox function for circle centered at c in R^n,
    with radius r.
    """
    c = np.array(c)

    def prox(x0):
        x0 = np.array(x0)
        y = x0 - c

        norm = np.linalg.norm(y)

        if norm <= r:
            return x0
        else:
            x = y*(r/norm) + c

            return x

    return prox
