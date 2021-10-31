```{math}
\DeclareMathOperator{\minimize}{minimize}
```

# Single linear equality with linear objective


We want a prox for

$$
\begin{array}{ll}
\underset{x}\minimize &
c^T x\\
\mbox{subject to}
& a^T x = 0\\
\end{array}
$$

With regularization parameter $\tau > 0$ the prox problem is

$$
\begin{array}{ll}
\underset{x}\minimize &
c^T x + \frac{1}{2\tau} \| x - x^0 \|_2^2 \\
\mbox{subject to}
& a^T x = 0\\
\end{array}
$$

Lagrangian:

$$
c^T x + \frac{1}{2\tau} \| x - x^0 \|_2^2 + \lambda a^T x
$$

KKT:

$$
c + \frac{1}{\tau} (x - x^0)+ \lambda a = 0\\
a^T x = 0
$$

Implies:

$$
a^T c - \frac{1}{\tau} a^Tx^0 + \lambda a^T a = 0
$$

Implies:

$$
\lambda  = \frac{a}{\| a\|^2} \left(\frac{1}{\tau}x^0 - c \right)
$$

$$
\lambda  = \frac{1}{\| a\|^2} \left(\frac{1}{\tau}a^Tx^0 - a^Tc \right)
$$

And from above, we have that:

$$
x = x^0 - \tau(\lambda a + c)
$$

which gives:

$$
x = \left(I - \frac{1}{\|a\|^2} a a^T \right)(x^0 - \tau c)
$$
