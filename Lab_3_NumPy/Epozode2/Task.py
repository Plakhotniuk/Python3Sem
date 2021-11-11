import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
for i in range(3):
    data = np.loadtxt(f'signal0{i + 1}.dat')
    new_data = np.array([data[max(0, j - 10):j].mean() for j in range(1, data.size)])
    ax[0].plot(np.linspace(0, 100, data.size), data)
    ax[0].set_title('Initial signal')
    ax[0].grid()
    ax[1].plot(np.linspace(0, 100, new_data.size), new_data)
    ax[1].set_title('Averaged signal')
    ax[1].grid()
    plt.savefig(f'averaged_signal0{i + 1}.png')
    ax[0].clear()
    ax[1].clear()
