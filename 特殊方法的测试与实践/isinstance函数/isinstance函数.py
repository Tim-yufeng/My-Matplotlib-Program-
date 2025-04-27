import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection
def onpick(event):
    artist = event.artist
    if isinstance(artist, plt.Line2D):
        print("You picked a line")
    elif isinstance(artist, PathCollection):
        print("You picked a scatter point")
    elif isinstance(artist, plt.Rectangle):
        print("You picked a rectangle")
    else:
        print("You picked an unknown artist")

fig, ax = plt.subplots()
line, = ax.plot([0, 1], [0, 1], picker=5)
scatter = ax.scatter([0.4], [1], picker=5)
rect = plt.Rectangle((0.2, 0.2), 0.4, 0.4, picker=5)
ax.add_patch(rect)

fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
