import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.plot(np.random.rand(10))
pressed=0
x_points = []
y_points = []
def on_click(event):
    global pressed
    if event.inaxes is not None:
        # print(f'Clicked at ({event.xdata}, {event.ydata})')
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        pressed=1
def moving(event):

    if event.name == 'motion_notify_event'  and event.inaxes is not None and pressed==1:
        x_points.append(event.xdata)
        y_points.append(event.ydata)
        # ax.plot(event.xdata, event.ydata, 'ro')
        ax.plot(x_points,y_points,c='r')
        plt.draw()


def release(event):
    global pressed,x_points,y_points
    if event.inaxes is not None:
        # print(f'Clicked at ({event.xdata}, {event.ydata})')
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        pressed=0
        x_points = []
        y_points = []

cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
cid2 = fig.canvas.mpl_connect('button_release_event', release)
cid3 = fig.canvas.mpl_connect('motion_notify_event', moving)


plt.show()
