from pytest import approx
import numpy as np

from proxie.proxes.dense_lin_eq import form_prox
import proxie

def test1():
    np.random.seed(103)

    m = 10
    n = 2*m

    A = np.random.randn(m,n)
    a = np.random.randn(m)

    B = np.random.randn(m,n)
    b = np.random.randn(m)

    C = np.vstack([A,B])
    c = np.hstack([a,b])

    x_sol = np.linalg.solve(C,c)

    prox1 = form_prox(A,a)
    prox2 = form_prox(B,b)

    tol = 1e-5
    x, info = proxie.dr.solver(prox1, prox2, np.zeros(n), tol=tol)

    assert info.converged
    assert x == approx(x_sol, abs=tol*10)
