import numpy as np
import matplotlib.pyplot as plt
class DraggableRectangle:
    def __init__(self, rect, ax):
        self.rect = rect
        self.ax = ax
        self.press = None
        self.cidpress = self.rect.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
    def on_press(self, event):
        if event.inaxes != self.rect.axes:
            return
        contains, attrd = self.rect.contains(event)
        if not contains:
            return
        self.press = self.rect.xy, (event.xdata, event.ydata)
    def on_motion(self, event):
        if self.press is None or event.inaxes != self.rect.axes:
            return
        (x0, y0), (xpress, ypress) = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        # 获取轴的范围
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        # 获取矩形宽高
        rect_width = self.rect.get_width()
        rect_height = self.rect.get_height()
        # 计算新的位置，并限制范围
        new_x = np.clip(x0 + dx, xlim[0], xlim[1] - rect_width)
        new_y = np.clip(y0 + dy, ylim[0], ylim[1] - rect_height)
        self.rect.set_x(new_x)
        self.rect.set_y(new_y)
        self.rect.figure.canvas.draw()
    def on_release(self, event):
        self.press = None
        self.rect.figure.canvas.draw()

# 创建图形
fig, ax = plt.subplots()
ax.set_xlim(0, 1)  # 限制x轴范围
ax.set_ylim(0, 1)  # 限制y轴范围

# 创建矩形
rect = plt.Rectangle((0.1, 0.1), 0.2, 0.2, facecolor='red')
ax.add_patch(rect)

# 使矩形可拖动
dr = DraggableRectangle(rect, ax)

plt.show()
