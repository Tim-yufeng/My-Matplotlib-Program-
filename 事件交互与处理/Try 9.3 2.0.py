import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
pressed = 0
x_data = []
y_data = []
cir = 0
lin = 0
lines = []
radius = []
exist_radius = []
exist_lines = []
exist_linear=[]
circle_number = 0
line_number = 0

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

def clickon(event):
    global pressed, x_data, y_data, cir
    if event.inaxes is not None and cir == 0:
        ax.scatter(event.xdata, event.ydata, c='m', s=10)
        pressed = 1
        plt.draw()
    if event.inaxes is not None and cir == 1:
        ax.scatter(event.xdata, event.ydata, c='m', s=10)
        ax.text(event.xdata + 0.5, event.ydata + 0.5, '({},{})'.format(round(event.xdata, 2), round(event.ydata, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
        pressed = 1
        plt.draw()

def release(event):
    global pressed, x_data, y_data, cir, circle_number, line_number, exist_radius, exist_lines,exist_linear
    if event.inaxes is not None and cir+lin == 0:
        ax.scatter(event.xdata, event.ydata, c='m', s=10)
        pressed = 0
        plt.draw()
        x_data = []
        y_data = []
    elif event.inaxes is not None and len(x_data) >= 2 and cir+lin == 1:
        x1, y1 = x_data[0], y_data[0]
        x2, y2 = x_data[-1], y_data[-1]
        r = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if cir==1:
            theta = np.linspace(0, 2 * np.pi, 100)
            x_circle = x1 + r * np.cos(theta)
            y_circle = y1 + r * np.sin(theta)
            ax.plot(x_circle, y_circle, c='m')  # 绘制圆
        line_number += 1
        exist_lines.append(lines[-1])
        exist_linear.append(r)
        if line_number >= 1:
            for line in exist_lines[-line_number:]:
                ax.add_line(line)
            fig.canvas.draw()
        plt.draw()
        x_data = []
        y_data = []
        pressed = 0
    elif len(x_data) < 2 or lin==1:
        ax.scatter(event.xdata, event.ydata, c='m')
        plt.draw()

def moving(event):
    global pressed, x_data, y_data, cir, lines, radius, exist_lines, exist_radius
    if event.name == 'motion_notify_event' and pressed == 1 and event.inaxes is not None and cir + lin == 0:
        x_data.append(event.xdata)
        y_data.append(event.ydata)
        ax.plot(x_data, y_data, c='m')
        plt.draw()
    if event.name == 'motion_notify_event' and pressed == 1 and event.inaxes is not None and cir + lin != 0:
        x_data.append(event.xdata)
        y_data.append(event.ydata)
        x1, y1 = x_data[0], y_data[0]
        x2, y2 = x_data[-1], y_data[-1]
        if cir==1:
            line, = ax.plot([x1, x2], [y1, y2], c='r')
        else:
            line, = ax.plot([x1, x2], [y1, y2], c='m')
        ra = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if cir == 1 and lin == 0:
            r = ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 'r={}'.format(round(ra, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
        if cir == 0 and lin == 1:
            r = ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 's={}'.format(round(ra, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
        lines.append(line)
        radius.append(r)
        plt.draw()
        if len(lines) > 1:
            for line in lines[:-1]:
                line.remove()
            lines = lines[-1:]  # 保留最后一个线条
            fig.canvas.draw()
        if len(radius) > 1:
            for r in radius[:-1]:
                r.remove()
            radius = radius[-1:]  # 保留最后一个文本
            fig.canvas.draw()

def circle(event):
    global cir, lin
    if event.key == 'r':
        cir = 1 - cir
        lin = 0

def linear(event):
    global lin, cir
    if event.key == 'l':
        lin = 1 - lin
        cir = 0

def clear_all(event):
    global pressed, x_data, y_data, cir, lines, radius, exist_lines, exist_radius, circle_number, line_number
    if event.key == 'delete':
        ax.clear()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
        fig.canvas.draw()
        lines = []
        radius = []
        exist_radius = []
        exist_lines = []
        circle_number = 0
        line_number = 0

cid1 = fig.canvas.mpl_connect('button_press_event', clickon)
cid2 = fig.canvas.mpl_connect('button_release_event', release)
cid3 = fig.canvas.mpl_connect('motion_notify_event', moving)
cid4 = fig.canvas.mpl_connect('key_press_event', linear)
cid5 = fig.canvas.mpl_connect('key_press_event', circle)
cid6 = fig.canvas.mpl_connect('key_press_event', clear_all)

plt.show()
