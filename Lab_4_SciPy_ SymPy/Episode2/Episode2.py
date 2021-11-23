from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Episode2/large.txt', skiprows=1)
A = data[:-1]
b = data[-1]
x = linalg.solve(A, b)
plt.bar(np.arange(1, x.size + 1), x)
plt.grid()
plt.savefig('Episode2/large.png')
plt.show()
