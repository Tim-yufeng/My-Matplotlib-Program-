import matplotlib.pyplot as plt

def onkeypress(event):
    if event.key == 'up':
        ax.set_ylim(ax.get_ylim()[0] + 0.1, ax.get_ylim()[1] + 0.1)
    elif event.key == 'down':
        ax.set_ylim(ax.get_ylim()[0] - 0.1, ax.get_ylim()[1] - 0.1)
    elif event.key == 'left':
        ax.set_xlim(ax.get_xlim()[0] - 0.1, ax.get_xlim()[1] - 0.1)
    elif event.key == 'right':
        ax.set_xlim(ax.get_xlim()[0] + 0.1, ax.get_xlim()[1] + 0.1)
    fig.canvas.draw()

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
cid = fig.canvas.mpl_connect('key_press_event', onkeypress)
plt.show()
