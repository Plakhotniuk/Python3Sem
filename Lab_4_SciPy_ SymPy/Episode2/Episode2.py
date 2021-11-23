from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
with open('Episode2/small.txt') as file:
    data = np.array([[float(j) for j in i.split()] for i in file], dtype=object)
    A = np.array([i for i in data[1:data.size-1]])
    b = np.array([i for i in data[-1]])
    x = linalg.solve(A, b)
    plt.bar(np.arange(1, x.size + 1), x)
    plt.grid()
    plt.savefig('Episode2/small.png')
    plt.show()
