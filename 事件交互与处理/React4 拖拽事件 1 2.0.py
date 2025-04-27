import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    def __init__(self, rect):
        global bbox
        self.rect = rect
        self.press = None
        self.cidpress = self.rect.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        bbox = self.rect.get_bbox()

        # self.x_left_upper




    def on_press(self, event):
        if event.inaxes != self.rect.axes:
            return
        contains, attrd = self.rect.contains(event)
        if not contains:
            return
        self.press = self.rect.xy, (event.xdata, event.ydata)

    def on_motion(self, event):
        global bbox
        if self.press is None or event.inaxes != self.rect.axes or (ax.contains_point((bbox.x0,bbox.y0)))+(ax.contains_point((bbox.x0,bbox.y1)))+(ax.contains_point((bbox.x1,bbox.y0)))+(ax.contains_point((bbox.x1,bbox.y1)))<4:
            return
        (x0, y0), (xpress, ypress) = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0 + dx)
        self.rect.set_y(y0 + dy)
        self.rect.figure.canvas.draw()
        bbox = self.rect.get_bbox()
    def on_release(self, event):
        self.press = None
        self.rect.figure.canvas.draw()

fig, ax = plt.subplots()
rect = plt.Rectangle((0.1, 0.1), 0.2, 0.2, facecolor='red')
ax.add_patch(rect)
dr = DraggableRectangle(rect)
plt.show()
