import matplotlib.pyplot as plt
import numpy as np

def on_scroll(event):
    # if event.button == 'up':
    ax.set_xlim(ax.get_xlim()[0] * (1-event.step*0.01), ax.get_xlim()[1] * (1-event.step*0.01))
    ax.set_ylim(ax.get_ylim()[0] * (1-event.step*0.01), ax.get_ylim()[1] * (1-event.step*0.01))
    fig.canvas.draw()
    # if event.button == 'down':
    #     ax.set_xlim(ax.get_xlim()[0] * (1+event.step*0.01), ax.get_xlim()[1] * (1+event.step*0.01))
    #     ax.set_ylim(ax.get_ylim()[0] * (1+event.step*0.01), ax.get_ylim()[1] * (1+event.step*0.01))
    fig.canvas.draw()
fig, ax = plt.subplots()
ax.imshow(np.random.rand(100, 100))
fig.canvas.mpl_connect('scroll_event', on_scroll)
plt.show()


