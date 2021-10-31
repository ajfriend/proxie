import pytest

import numpy as np

from proxie.proxes.single_lin_eq import form_prox, _cvxpy_prox

def test_simplex():
    np.random.seed(0)
    N = 8
    tol = 1e-12

    for _ in range(100):
        x0 = np.random.randn(N)
        c = np.random.randn(N)
        a = np.random.randn(N)
        tau = np.random.rand() + .1

        prox = form_prox(c, a, tau=tau)

        diff = _cvxpy_prox(x0, c, a, tau) - prox(x0)

        assert np.linalg.norm(diff) <= tol
