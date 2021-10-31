from .util import pairs, SolverInfo

from numpy.linalg import norm


def dr_iter(prox1, prox2, z):
    """ Infinite DR iterator

    Note that z is the actual iteration variable. x,y are auxiliary.

    http://www.seas.ucla.edu/~vandenbe/236C/lectures/dr.pdf
    """
    while True:
        y = prox1(z)
        x = prox2(2*y - z)
        # don't overwrite input!
        z = z + x - y

        yield x, y, z


def resids(seq):
    seq = pairs(seq)

    for e0, e1 in seq:
        x0, _,  _ = e0
        x1, y1, _ = e1

        r = norm(x1 - y1)
        s = norm(x1 - x0)

        yield r, s


def terminate(seq, tol, N):
    for i, (r, s) in enumerate(seq):
        yield r, s

        if i >= N:
            break
        if max(r, s) <= tol:
            break


def solver(prox1, prox2, z0, tol=1e-5, max_iters=5000):
    its = dr_iter(prox1, prox2, z0)

    rs = resids(its)
    rs = terminate(rs, tol, max_iters)
    r, s = zip(*rs)

    exit_tol = max(r[-1], s[-1])
    converged = (exit_tol <= tol)

    x, _, z = next(its)

    info = SolverInfo(
        resid_r = r,
        resid_s = s,
        num_iters = len(r),
        exit_tol = exit_tol,
        converged = converged,
        z=z,
    )

    return x, info
