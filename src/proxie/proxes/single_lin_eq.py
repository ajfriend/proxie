import numpy as np
import cvxpy as cvx

def form_prox(c, a, tau=1):
    """ form prox for

    min  tau*c^T x
    st.  a^T x == 0
    """
    a /= np.linalg.norm(a)
    tau_c = tau*c

    def prox(x0):
        x = x0 - tau_c

        return x - a*np.dot(a, x)


    return prox

def _cvxpy_prox(x0, c, a, tau=1):
    x = cvx.Variable(len(x0))
    obj = cvx.Minimize(c@x + cvx.sum_squares(x - x0)/(2*tau) )
    cst = [a@x == 0]

    prob = cvx.Problem(obj, cst)
    prob.solve()
    x = x.value

    return x
