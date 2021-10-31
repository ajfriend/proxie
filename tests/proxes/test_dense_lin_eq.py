from pytest import approx
import numpy as np
from proxie.proxes.dense_lin_eq import form_prox

def test():
    np.random.seed(101)

    m,n = 200,300

    A = np.random.randn(m,n)
    b = np.random.randn(m)

    prox = form_prox(A,b)


    for _ in range(20):
        x0 = np.random.randn(n)
        x = prox(x0)
        assert A@x == approx(b)
