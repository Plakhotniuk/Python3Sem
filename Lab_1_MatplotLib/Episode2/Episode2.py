import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = []
y = []

with open('frames.dat', 'r') as file:
    for ind, lines in enumerate(file):
        if not ind % 2:
            x.append([float(i) for i in lines.split()])
        else:
            y.append([float(i) for i in lines.split()])

fig = plt.figure()

x_lim = [min([min(i) for i in x]), max([max(i) for i in x])]
y_lim = [min([min(i) for i in y]), max([max(i) for i in y])]

ax = plt.axes(xlim=(x_lim[0], x_lim[1]),
              ylim=(y_lim[0] * 1.2, y_lim[1] * 1.2))
line, = ax.plot([], [])
plt.grid()
plt.yticks(np.arange(y_lim[0] * 1.2, y_lim[1] * 1.2, 2))


def init():
    line.set_data([], [])
    return line,


def animate(i):
    plt.title('Frame ' + str(i))
    line.set_data(x[i], y[i])
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=6, interval=500, blit=True)

anim.save('graphics.gif', writer='pillow')
