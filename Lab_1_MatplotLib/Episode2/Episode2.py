import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
x = []
y = []

with open('frames.dat', 'r') as file:
    print(enumerate(file))
    for ind, lines in enumerate(file):
        if not ind % 2:
            x.append([float(i) for i in lines.split()])
        else:
            y.append([float(i) for i in lines.split()])

fig = plt.figure()
ax = plt.axes(xlim=(min([min(i) for i in x]), max([max(i) for i in x])),
              ylim=(min([min(i) for i in y]) * 1.2, max([max(i) for i in y]) * 1.2))
line, = ax.plot([], [])
plt.grid()
plt.yticks(np.arange(min([min(i) for i in y]) * 1.2, max([max(i) for i in y]) * 1.2, 2))


def init():
    line.set_data([], [])
    return line,


def animate(i):
    plt.title('Frame ' + str(i))
    line.set_data(x[i], y[i])
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=6, interval=500, blit=True)

anim.save(os.path.join('Episode2', 'graphics.gif'), writer='pillow')
