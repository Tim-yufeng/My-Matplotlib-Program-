# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))
# pressed=0
# x_points = []
# y_points = []
# cir=0
# x_initial = None
# y_initial = None
# x_final = None
# y_final = None
# def on_click(event):
#     global pressed,cir,x_initial,y_initial,x_final,y_final
#     if event.inaxes is not None:
#         # print(f'Clicked at ({event.xdata}, {event.ydata})')
#         ax.plot(event.xdata, event.ydata, 'ro')
#         plt.draw()
#         pressed=1
#         x_initial=event.xdata
#         y_initial=event.ydata
#         if event.key == 'r':
#             cir = 1
#         # cir=1
# def moving(event):
#     global cir,x_initial,y_initial,x_final,y_final
#     if event.name == 'motion_notify_event'  and event.inaxes is not None and pressed==1:
#         x_points.append(event.xdata)
#         y_points.append(event.ydata)
#         # ax.plot(event.xdata, event.ydata, 'ro')
#         ax.plot(x_points,y_points,c='r')
#         plt.draw()
#
#
# def release(event):
#     global pressed,x_points,y_points,cir,x_initial,y_initial,x_final,y_final
#     if event.inaxes is not None:
#         # print(f'Clicked at ({event.xdata}, {event.ydata})')
#         ax.plot(event.xdata, event.ydata, 'ro')
#         plt.draw()
#         pressed=0
#         x_final=event.xdata
#         y_final=event.ydata
#         x_points = []
#         y_points = []
#         cir=0
# def circle(event):
#     global pressed,x_points,y_points,cir,x_initial,y_initial,x_final,y_final
#     if event.name == 'motion_notify_event'  and event.inaxes is not None and cir==1:
#         # x_points.append(event.xdata)
#         # y_points.append(event.ydata)
#         # x_initial=x_points[0]
#         # x_final=x_points[-1]
#         # y_initial=y_points[0]
#         # y_final=y_points[-1]
#         r=np.sqrt((x_initial-x_final)**2+(y_initial-y_final)**2)
#         x=np.linspace(x_initial-r,x_initial+r)
#         y1=np.sqrt(r**2-(x-x_initial)**2)
#         y2 = -np.sqrt(r ** 2 - (x - x_initial) ** 2)
#         ax.plot(x,y1,c='m')
#         ax.plot(x,y2,c='m')
#         plt.draw()
#
#
# cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
# cid2 = fig.canvas.mpl_connect('button_release_event', release)
# cid3 = fig.canvas.mpl_connect('motion_notify_event', moving)
# cid4 = fig.canvas.mpl_connect('motion_notify_event', circle)
#
#
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
# ax.plot(np.random.rand(10))
# ax.set_navigate(True)
# ax.set_aspect('equal')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_aspect('equal')
pressed = 0
x_points = []
y_points = []
cir = 0
x_initial = None
y_initial = None

def on_click(event):
    global pressed, x_initial, y_initial
    if event.inaxes is not None:
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        pressed = 1
        x_initial = event.xdata
        y_initial = event.ydata

def moving(event):
    global x_points, y_points, x_initial, y_initial, cir
    if event.name == 'motion_notify_event' and event.inaxes is not None and pressed == 1:
        if cir == 0:
            x_points.append(event.xdata)
            y_points.append(event.ydata)
            ax.plot(x_points, y_points, c='r')
            plt.draw()
        else:
            x_final = event.xdata
            y_final = event.ydata
            r = np.sqrt((x_initial - x_final) ** 2 + (y_initial - y_final) ** 2)
            theta = np.linspace(0, 2 * np.pi, 100)
            x_circle = x_initial + r * np.cos(theta)
            y_circle = y_initial + r * np.sin(theta)
            # ax.clear()  # 清除之前的绘制
            # ax.plot(np.random.rand(10))  # 重新绘制初始曲线
            ax.plot(x_circle, y_circle, c='m')  # 绘制圆
            plt.draw()

def release(event):
    global pressed, x_points, y_points, cir
    if event.inaxes is not None:
        ax.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        pressed = 0
        x_points = []
        y_points = []
        cir = 0

def on_key(event):
    global cir
    if event.key == 'r':
        cir = 1 - cir  # Toggle cir between 0 and 1

cid1 = fig.canvas.mpl_connect('button_press_event', on_click)
cid2 = fig.canvas.mpl_connect('button_release_event', release)
cid3 = fig.canvas.mpl_connect('motion_notify_event', moving)
cid4 = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
