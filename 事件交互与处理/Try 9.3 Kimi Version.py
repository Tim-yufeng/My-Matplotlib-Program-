# import matplotlib.pyplot as plt
# import numpy as np
#
# class InteractivePlot:
#     def __init__(self):
#         self.fig, self.ax = plt.subplots()
#         self.ax.set_xlim(-10, 10)
#         self.ax.set_ylim(-10, 10)
#         self.ax.set_aspect('equal')
#         self.is_drawing = False
#         self.is_drawing_circle = False
#         self.is_drawing_line = False
#         self.x_data = []
#         self.y_data = []
#         self.lines = []
#         self.radius_texts = []
#         self.connect_events()
#
#     def connect_events(self):
#         self.fig.canvas.mpl_connect('button_press_event', self.clickon)
#         self.fig.canvas.mpl_connect('button_release_event', self.release)
#         self.fig.canvas.mpl_connect('motion_notify_event', self.moving)
#         self.fig.canvas.mpl_connect('key_press_event', self.handle_key_press)
#
#     def clickon(self, event):
#         if event.inaxes is not None:
#             self.ax.scatter(event.xdata, event.ydata, c='m', s=10)
#             self.is_drawing = True
#             self.x_data.append(event.xdata)
#             self.y_data.append(event.ydata)
#             self.fig.canvas.draw()
#
#     def release(self, event):
#         if event.inaxes is not None and self.is_drawing:
#             self.ax.scatter(event.xdata, event.ydata, c='m', s=10)
#             self.is_drawing = False
#             if self.is_drawing_circle or self.is_drawing_line:
#                 self.draw_shape()
#             self.x_data = []
#             self.y_data = []
#             self.fig.canvas.draw()
#
#     def moving(self, event):
#         if event.name == 'motion_notify_event' and self.is_drawing and event.inaxes is not None:
#             self.x_data.append(event.xdata)
#             self.y_data.append(event.ydata)
#             if self.is_drawing_circle or self.is_drawing_line:
#                 self.update_shape()
#             self.fig.canvas.draw()
#
#     def draw_shape(self):
#         x1, y1 = self.x_data[0], self.y_data[0]
#         x2, y2 = self.x_data[-1], self.y_data[-1]
#         distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#         if self.is_drawing_circle:
#             theta = np.linspace(0, 2 * np.pi, 100)
#             x_circle = x1 + distance * np.cos(theta)
#             y_circle = y1 + distance * np.sin(theta)
#             self.ax.plot(x_circle, y_circle, c='m')
#             self.radius_texts.append(self.ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 'r={}'.format(round(distance, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'}))
#         elif self.is_drawing_line:
#             line, = self.ax.plot([x1, x2], [y1, y2], c='m')
#             self.lines.append(line)
#             self.radius_texts.append(self.ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 's={}'.format(round(distance, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'}))
#
#     def update_shape(self):
#         if self.lines:
#             self.lines[-1].set_data(self.x_data, self.y_data)
#         if self.radius_texts:
#             x1, y1 = self.x_data[0], self.y_data[0]
#             x2, y2 = self.x_data[-1], self.y_data[-1]
#             distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#             self.radius_texts[-1].set_text('r={}'.format(round(distance, 2)) if self.is_drawing_circle else 's={}'.format(round(distance, 2)))
#             self.radius_texts[-1].set_position(((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5))
#
#     def handle_key_press(self, event):
#         if event.key == 'r':
#             self.is_drawing_circle = not self.is_drawing_circle
#             self.is_drawing_line = False
#         elif event.key == 'l':
#             self.is_drawing_line = not self.is_drawing_line
#             self.is_drawing_circle = False
#         elif event.key == 'delete':
#             self.clear_all()
#
#     def clear_all(self):
#         self.ax.clear()
#         self.ax.set_xlim(-10, 10)
#         self.ax.set_ylim(-10, 10)
#         self.ax.set_aspect('equal')
#         self.fig.canvas.draw()
#         self.lines = []
#         self.radius_texts = []
#
# plot = InteractivePlot()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

class InteractivePlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_aspect('equal')
        self.is_drawing = False
        self.is_drawing_circle = False
        self.is_drawing_line = False
        self.x_data = []
        self.y_data = []
        self.lines = []
        self.radius_texts = []
        self.connect_events()

    def connect_events(self):
        self.fig.canvas.mpl_connect('button_press_event', self.clickon)
        self.fig.canvas.mpl_connect('button_release_event', self.release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.moving)
        self.fig.canvas.mpl_connect('key_press_event', self.handle_key_press)

    def clickon(self, event):
        if event.inaxes is not None:
            self.ax.scatter(event.xdata, event.ydata, c='m', s=10)
            self.is_drawing = True
            self.x_data.append(event.xdata)
            self.y_data.append(event.ydata)
            if self.is_drawing_circle or self.is_drawing_line:
                # 预先创建一个线条对象并将其添加到 self.lines 列表中
                line, = self.ax.plot([], [], c='m')
                self.lines.append(line)
            self.fig.canvas.draw()

    def release(self, event):
        if event.inaxes is not None and self.is_drawing:
            self.ax.scatter(event.xdata, event.ydata, c='m', s=10)
            self.is_drawing = False
            if self.is_drawing_circle or self.is_drawing_line:
                self.draw_shape()
            self.x_data = []
            self.y_data = []
            self.fig.canvas.draw()

    def moving(self, event):
        if event.name == 'motion_notify_event' and self.is_drawing and event.inaxes is not None:
            self.x_data.append(event.xdata)
            self.y_data.append(event.ydata)
            if self.is_drawing_circle or self.is_drawing_line:
                self.update_shape()
            self.fig.canvas.draw()

    def draw_shape(self):
        x1, y1 = self.x_data[0], self.y_data[0]
        x2, y2 = self.x_data[-1], self.y_data[-1]
        distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if self.is_drawing_circle:
            theta = np.linspace(0, 2 * np.pi, 100)
            x_circle = x1 + distance * np.cos(theta)
            y_circle = y1 + distance * np.sin(theta)
            self.lines[-1].set_data(x_circle, y_circle)
            text = self.ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 'r={}'.format(round(distance, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
            self.radius_texts.append(text)
        elif self.is_drawing_line:
            self.lines[-1].set_data([x1, x2], [y1, y2])
            text = self.ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, 's={}'.format(round(distance, 2)), fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
            self.radius_texts.append(text)
        self.fig.canvas.draw()

    def update_shape(self):
        if self.lines:
            self.lines[-1].set_data(self.x_data, self.y_data)
        if self.radius_texts:
            x1, y1 = self.x_data[0], self.y_data[0]
            x2, y2 = self.x_data[-1], self.y_data[-1]
            distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            self.radius_texts[-1].set_text('r={}'.format(round(distance, 2)) if self.is_drawing_circle else 's={}'.format(round(distance, 2)))
            self.radius_texts[-1].set_position(((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5))

    def handle_key_press(self, event):
        if event.key == 'r':
            self.is_drawing_circle = not self.is_drawing_circle
            self.is_drawing_line = False
        elif event.key == 'l':
            self.is_drawing_line = not self.is_drawing_line
            self.is_drawing_circle = False
        elif event.key == 'delete':
            self.clear_all()

    def clear_all(self):
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_aspect('equal')
        self.fig.canvas.draw()
        self.lines = []
        self.radius_texts = []

plot = InteractivePlot()
plt.show()
