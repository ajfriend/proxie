from dataclasses import dataclass
from functools import wraps
from collections import OrderedDict

import numpy as np

from .util import pairs


def form_slices(d):
    x = d.values()
    x = [0] + list(x)
    x = np.cumsum(x)
    x = pairs(x)

    slices = (slice(a,b) for a,b in x)
    slices = zip(d.keys(), slices)
    slices = dict(slices)

    return slices


@dataclass
class Stuffer:
    var_sizes: 'dict[str, int]'

    def __post_init__(self):
        # Make it clear that we're fixing the key order.
        # This is actually a no-op in modern python.
        self.var_sizes = OrderedDict(self.var_sizes)
        self.N = sum(self.var_sizes.values())
        self.slices = form_slices(self.var_sizes)


    def from_vec(self, vec):
        out = {
            k: vec[s]
            for k,s in self.slices.items()
        }

        return out


    def to_vec(self, **kwargs):
        vec = np.zeros(self.N)

        for k,s in self.slices.items():
            vec[s] = kwargs[k]

        return vec


    def wrapper(self, func):
        """ Handles stuffing and unstuffing with a function.

        Example usage

        @vec_wrapper
        def prox(x, y):
            # previously set up sub-proxes A and B

            x = prox_A(x)
            y = prox_B(y)

            return {'x': x, 'y': y}
        """
        @wraps(func)
        def wrapping_func(vec):
            inputs  = self.from_vec(vec)
            outputs = func(**inputs)
            vec     = self.to_vec(**outputs)

            return vec

        return wrapping_func
