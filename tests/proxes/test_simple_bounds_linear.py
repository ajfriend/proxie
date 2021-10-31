import pytest

import numpy as np

from proxie.proxes.simple_bounds_linear import form_prox, _cvxpy_prox

def test_simplex():
    np.random.seed(0)
    N = 100
    tol = 1e-6

    for _ in range(100):
        x0 = np.random.randn(N)
        c = np.random.randn(N)
        a = np.random.rand(N)
        b = a + np.random.rand(N)
        tau = np.random.rand() + .1

        prox = form_prox(c, a, b, tau=tau)

        diff = _cvxpy_prox(x0, c, a, b, tau) - prox(x0)

        assert np.linalg.norm(diff) <= tol
