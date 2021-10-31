from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt


def pairs(seq):
    """ Take a sequence like e0, e1, e2, e3... and return
    a sequence of pairs like

    (e0, e1), (e1, e2), (e2, e3), ...
    """
    seq = iter(seq)
    e1 = next(seq)
    for e2 in seq:
        yield (e1, e2)
        e1 = e2


@dataclass
class SolverInfo:
    resid_r: 'list[float]' = None
    resid_s: 'list[float]' = None
    num_iters: int = 0
    exit_tol: float = 0
    converged: bool = False
    z: 'np.ndarray[float]' = None


    def plot_resids(self):
        plt.plot(np.log10(self.resid_r))
        plt.plot(np.log10(self.resid_s))

    def __repr__(self):
        items = [
            f'converged={self.converged}',
            f'exit_tol={self.exit_tol:.1e}',
            f'num_iters={self.num_iters}',
        ]
        items = ', '.join(items)

        s = f'{self.__class__.__name__}({items},...)'

        return s
