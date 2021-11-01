import numpy as np
import scipy.sparse as sp
import qdldl as ldl


def form_prox(A, b):
    """
    Sparse LA prox for Ax=b.
    """

    m,n = A.shape

    I = sp.eye(n)
    Z = sp.coo_matrix((m,m))

    K = (
        [I, A.T],
        [A, Z  ],
    )
    K = sp.bmat(K, format='csc', dtype='float64')

    F = ldl.Solver(K)
    rhs = np.zeros(m + n)
    rhs[n:] = b

    del K
    del I
    del Z

    def prox(x0):
        rhs[:n] = x0
        x = F.solve(rhs)
        return x[:n]

    return prox
