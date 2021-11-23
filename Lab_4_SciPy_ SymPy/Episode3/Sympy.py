import sympy as sp
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8,8))
x = sp.Symbol('x')
y = sp.Function('y')(x)

diff = sp.Eq(y.diff(x) + 2 * y, 0)
eq = sp.dsolve(diff, ics={y.subs(x, 0): sp.sqrt(2)})
x_1 = np.linspace(0, 10, 100)
y_1 = [eq.evalf(subs={x: i}).args[1] for i in x_1]
ax[0].plot(x_1, y_1, '--', label='Sympy')
ax[0].grid()


def problem(y, x):
    dydx = -2 * y
    return dydx


y0 = np.sqrt(2)
y_2 = scipy.integrate.odeint(problem, y0, x_1)
ax[0].plot(x_1, y_2, label='Scipy')
ax[0].set_title('Solution of Sympy and Scipy')
ax[0].legend()

y_3 = [abs(y_1[i] - y_2[i]) for i in range(len(y_1))]
ax[1].plot(x_1, y_3)
ax[1].set_title('Difference between Sympy and Scipy')
ax[1].grid()
plt.savefig('graphics.png')
plt.show()