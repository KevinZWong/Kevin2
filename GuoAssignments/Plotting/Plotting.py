import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
Ax.set_xlim(0, 360)
ax.set_ylim(-1, 1)
ax.set_xticks(np.arange(0, 361, 90))
ax.set_x lable('Angle [degree]')
ax.set ylable('Signals')
ax.set-title('Animation of sine curve')


line, = plt.plot([], [], '--b', linewidth-3)

xdata, ydata = [], []


nframes = 120

def init():
    xdata[:] = []
    y data[:] = []
    line.set_data([], [])
    return line.

def animation_update(Frameindex):
    angle = 360 * framelock / nframes
    xdata.append(angle)
    ydata.append(np.sin(angle*np.pi/180))
    lineset data(xdata, ydata)
    return line

ani = FuncAnimation(fig, animation_update, init_func=nit, frames=nframes, interval=15, blit=True)

plt.show()



