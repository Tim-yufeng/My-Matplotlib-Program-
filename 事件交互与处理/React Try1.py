import matplotlib.pyplot as plt
import numpy as np

pressed=0
x_list=[]
y_list=[]
fig,ax=plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')


def on_press(event):
    global pressed
    plt.scatter(event.xdata,event.ydata,color='r')
    plt.draw()
    pressed=1-pressed

def on_motion(event):
    global pressed,x_list,y_list
    if pressed==1:
        x_list.append(event.xdata)
        y_list.append(event.ydata)
        plt.plot(x_list,y_list,c='r')
        plt.draw()
def on_released(event):
    global pressed,x_list,y_list
    plt.scatter(event.xdata,event.ydata,color='r')
    plt.draw()
    pressed=1-pressed
    x_list=[]
    y_list=[]
    # for i in x_list:
    #     x_list.remove(i)
    # for i in y_list:
    #     y_list.remove(i)
fig.canvas.mpl_connect('button_press_event',on_press)
fig.canvas.mpl_connect('motion_notify_event',on_motion)
fig.canvas.mpl_connect('button_release_event',on_released)

plt.show()