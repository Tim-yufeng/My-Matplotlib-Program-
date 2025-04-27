import matplotlib.pyplot as plt

def onclick(event):
    print(f'You clicked at {event.xdata}, {event.ydata}')
    plt.scatter(event.xdata,event.ydata,c='r',s=5)
    fig.canvas.draw()
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
