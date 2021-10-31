import numpy as np
import scipy.linalg as la

def form_prox(A, b):
    """
    Form prox for Ax=b, using dense linear algebra.

    [ I A.T ] * [x] = [x0]
    [ A 0   ]   [y]   [b]
    """
    m,n = A.shape

    I = np.eye(n)
    Z = np.zeros((m,m))

    S = np.block([
        [I, A.T],
        [A, Z  ]
    ])

    lu, piv = la.lu_factor(S)

    r = np.zeros(m+n)
    r[n:m+n] = b

    def prox(x0):
        r[:n] = x0
        x = la.lu_solve((lu, piv), r)

        return x[:n]

    return prox
