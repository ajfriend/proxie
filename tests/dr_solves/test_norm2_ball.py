from pytest import approx

from proxie import dr
from proxie.proxes.norm2_ball import form_prox

def test1():
    prox1 = form_prox((0,0), 1)
    prox2 = form_prox((2.0,0), 1)

    x0 = (17,45)
    x, info = dr.solver(prox1, prox2, x0, tol=1e-10)

    assert info.converged
    assert info.num_iters < 500

    assert prox1(x) == approx(x)
    assert prox2(x) == approx(x)


def test2():
    prox1 = form_prox((0,0), 1)
    prox2 = form_prox((1.9,0), 1)

    x0 = (17,45)
    x, info = dr.solver(prox1, prox2, x0, tol=1e-10)

    assert info.converged
    assert info.num_iters < 500

    assert prox1(x) == approx(x)
    assert prox2(x) == approx(x)


def test3():
    prox1 = form_prox((0,0), 1)
    prox2 = form_prox((1.8,0), 1)

    x0 = (17,45)
    x, info = dr.solver(prox1, prox2, x0, tol=1e-10)

    assert info.converged
    assert info.num_iters < 500

    assert prox1(x) == approx(x)
    assert prox2(x) == approx(x)
