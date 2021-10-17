import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []

with open('Episode2/frames.dat', 'r') as file:
    num = 0
    for lines in file:
        if not num % 2:
            x.append([float(i) for i in lines.split()])
        else:
            y.append([float(i) for i in lines.split()])
        num +=1

fig = plt.figure()
ax = plt.axes(xlim=(min(x[0]), max(x[0])), ylim=(-max(y[len(y) - 1]) * 1.2, max(y[len(y) - 1]) * 1.2))
line, = ax.plot([], [])
plt.grid()
plt.yticks(np.arange(-14, 16, 2))


def init():
    line.set_data([], [])
    return line,


def animate(i):
    plt.title('Frame ' + str(i))
    line.set_data(x[i], y[i])
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=6, interval=500, blit=True)

anim.save('Episode2/graphics.gif', writer='pillow')




