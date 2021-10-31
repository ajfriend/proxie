from collections import OrderedDict

import pytest
import numpy as np

from proxie import Stuffer


def test_init():
    d = {
        'a': 10,
        'b': 4,
        'c': 20,
    }

    stuff = Stuffer(d)

    assert stuff.var_sizes == OrderedDict(d)
    assert stuff.N == sum(d.values())
    assert stuff.slices == {'a': slice(0, 10, None), 'b': slice(10, 14, None), 'c': slice(14, 34, None)}

def test_funcs():
    stuff = Stuffer({
        'a': 10,
        'b': 4,
        'c': 20,
    })

    x = np.arange(34)

    out = stuff.from_vec(x)

    expected = {
        'a': np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        'b': np.array([10, 11, 12, 13]),
        'c': np.array([14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
    }

    assert out.keys() == expected.keys()
    for k in expected:
        assert (out[k] == expected[k]).all()

    # should get back the original array
    out = stuff.to_vec(**out)
    assert (out == x).all()


def test_wrapper():
    stuff = Stuffer({
        'x': 4,
        'y': 2,
        'z': 3,
    })

    @stuff.wrapper
    def foo(x,y,z):
        return {'x': x*2, 'y': y*3, 'z': z*4}

    out = foo(np.ones(9))

    expected = np.array([2,2,2,2,3,3,4,4,4])

    assert out == pytest.approx(expected)




