import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

for i in range(3):
    data = np.loadtxt(f'signal0{i + 1}.dat')
    new_data = np.concatenate((np.array([data[0:j].mean() for j in range(1, 11)]),
                               np.convolve(data, np.ones(10) / 10, mode='full')[10:-9]), axis=0)
    ax[0].plot(np.linspace(0, 100, data.size), data)
    ax[0].set_title('Initial signal')
    ax[0].grid()
    ax[1].plot(np.linspace(0, 100, new_data.size), new_data)
    ax[1].set_title('Averaged signal')
    ax[1].grid()
    plt.savefig(f'averaged_signal0{i + 1}.png')
    ax[0].clear()
    ax[1].clear()

# Посчитал среднее врямя работы за 30 считываний данных из файлов:
#  Все в list comprehension:
# 100 элементов:
# 0.000495298703511556
# 400 элементов:
# 0.0025328318277994793
# Только 10 элементов в list comprehension, остальое считаю через np.convolve:
# 100 элементов:
# 0.0002837260564168294
# 400 элементов:
# 0.00031061967213948566
