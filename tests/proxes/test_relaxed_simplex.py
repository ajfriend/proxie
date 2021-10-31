import pytest

import numpy as np

from proxie.proxes.relaxed_simplex import prox


def test_simplex():
    np.random.seed(0)
    N = 5
    tol = 1e-5

    for _ in range(1000):
        x0 = np.random.randn(N)*10

        x = prox(x0)

        assert np.sum(x) <= 1.0 + tol
        assert (x + tol >= 0).all()


def test_simplex_big():
    np.random.seed(0)
    N = 1000
    tol = 1e-5

    for _ in range(1000):
        x0 = np.random.randn(N)*10

        x = prox(x0)

        assert np.sum(x) <= 1.0 + tol
        assert (x + tol >= 0).all()
