from pytest import approx
import numpy as np


def test():
    np.random.seed(101)

    m,n = 200,300

    A = np.random.randn(m,n)
    b = np.random.randn(m)

    from proxie.proxes.dense_lin_eq import form_prox
    prox = form_prox(A,b)


    for _ in range(20):
        x0 = np.random.randn(n)
        x = prox(x0)
        assert A@x == approx(b)


def test_sparse():
    np.random.seed(101)

    m,n = 200,300

    A = np.random.randn(m,n)
    b = np.random.randn(m)

    from proxie.proxes.proj_ldl import form_prox
    prox = form_prox(A,b)


    for _ in range(20):
        x0 = np.random.randn(n)
        x = prox(x0)
        assert A@x == approx(b)
