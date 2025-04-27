import matplotlib.pyplot as plt
import numpy as np

def on_scroll(event):
    if event.button == 'up':
        ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
        ax.set_ylim(ax.get_ylim()[0] * 0.9, ax.get_ylim()[1] * 0.9)
        fig.canvas.draw()
    if event.button == 'down':
        ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
        ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
        fig.canvas.draw()
fig, ax = plt.subplots()
ax.imshow(np.random.rand(100, 100))
fig.canvas.mpl_connect('scroll_event', on_scroll)
plt.show()


