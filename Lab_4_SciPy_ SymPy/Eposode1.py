import sympy as sp

data = sp.zeros(3)
mu, rho, l = sp.Symbol('mu'), sp.Symbol('rho'), sp.Symbol('lambda')
data = data.row_join(sp.diag(-1/rho, -1/rho, -1/rho).row_join(sp.zeros(3)))
data = data.col_join(sp.diag(-(l + 2 * mu), -mu, -mu).row_join(sp.zeros(3, 6)))
data = data.col_join(sp.Matrix([-l, 0, -l]).row_join(sp.zeros(3, 8)))
data = sp.Matrix(data)
sp.pprint(data.eigenvals())



