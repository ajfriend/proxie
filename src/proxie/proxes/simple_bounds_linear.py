import numpy as np
import cvxpy as cvx

def form_prox(c, a=None, b=None, tau=1):
    """
    prox for:

    min   tau*c^T x
    st.   a <= x <= b

    """
    tau_c = tau*c

    def prox(x0):
        x = x0 - tau_c
        x = np.clip(x, a, b)

        return x

    return prox

def _cvxpy_prox(x0, c, a, b, tau=1):
    x = cvx.Variable(len(x0))
    obj = cvx.Minimize(c@x + cvx.sum_squares(x - x0)/(2*tau) )
    cst = [a <= x, x <= b]

    prob = cvx.Problem(obj, cst)
    prob.solve()
    x = x.value

    return x

