import matplotlib.pyplot as plt
import numpy as np


# 使用类管理状态
class DrawState:
    def __init__(self):
        self.pressed = False
        self.mode = 'typical'
        self.current_shape = []
        self.history = []
        self.lines = []
        self.circles = []
        self.radius_values = []


# 初始化
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
state = DrawState()


# 鼠标点击事件
def on_click(event):
    if event.inaxes is None:
        return
    state.pressed = not state.pressed
    ax.scatter(event.xdata, event.ydata, color='r', s=10)
    plt.draw()


# 鼠标释放事件
def on_released(event):
    if event.inaxes is None:
        return
    state.pressed = not state.pressed
    ax.scatter(event.xdata, event.ydata, color='r', s=10)
    plt.draw()
    state.current_shape = []
    if state.mode == 'linear':
        state.history.append(state.lines[-1])
    elif state.mode == 'circle':
        state.history.append(state.circles[-1])


# 一般曲线绘制
def typical_move(event):
    if state.pressed and event.inaxes is not None:
        state.current_shape.append((event.xdata, event.ydata))
        x, y = zip(*state.current_shape)
        ax.plot(x, y, c='r')
        plt.draw()


# 直线绘制
def linear_move(event):
    if state.pressed and event.inaxes is not None:
        if len(state.current_shape) < 2:
            state.current_shape.append((event.xdata, event.ydata))
        else:
            state.current_shape[-1] = (event.xdata, event.ydata)

        x1, y1 = state.current_shape[0]
        x2, y2 = state.current_shape[-1]
        r_value = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # 更新直线
        if state.lines:
            state.lines[-1].set_data([x1, x2], [y1, y2])
        else:
            line, = ax.plot([x1, x2], [y1, y2], c='r')
            state.lines.append(line)

        # 更新半径标注
        if state.radius_values:
            state.radius_values[-1].set_position(((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5))
            state.radius_values[-1].set_text(f'r={round(r_value, 2)}')
        else:
            r = ax.text((x1 + x2) / 2 + 0.5, (y1 + y2) / 2 + 0.5, f'r={round(r_value, 2)}',
                        fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
            state.radius_values.append(r)

        plt.draw()


# 圆形绘制
def circle_move(event):
    linear_move(event)
    if len(state.current_shape) == 2:
        x1, y1 = state.current_shape[0]
        x2, y2 = state.current_shape[-1]
        r_value = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        theta = np.linspace(0, 2 * np.pi, 100)

        # 更新圆形
        if state.circles:
            state.circles[-1].set_data(x1 + r_value * np.cos(theta), y1 + r_value * np.sin(theta))
        else:
            circle, = ax.plot(x1 + r_value * np.cos(theta), y1 + r_value * np.sin(theta), c='r')
            state.circles.append(circle)

        plt.draw()


# 鼠标移动事件
def on_motion(event):
    if event.inaxes is None:
        return
    if state.mode == 'typical':
        typical_move(event)
    elif state.mode == 'linear':
        linear_move(event)
    elif state.mode == 'circle':
        circle_move(event)


# 键盘事件
def pattern_change(event):
    if event.key == 'l':  # 直线模式
        state.mode = 'linear'
    elif event.key == 'r':  # 圆形模式
        state.mode = 'circle'
    elif event.key == 't':  # 一般曲线模式
        state.mode = 'typical'
    elif event.key == 'delete':  # 清空画布
        ax.clear()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
        state.history = []
        state.lines = []
        state.circles = []
        state.radius_values = []
    elif event.key in ['up', 'down', 'left', 'right']:  # 平移画布
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        dx = (xlim[1] - xlim[0]) * 0.1
        dy = (ylim[1] - ylim[0]) * 0.1
        if event.key == 'up':
            ax.set_ylim(ylim[0] + dy, ylim[1] + dy)
        elif event.key == 'down':
            ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
        elif event.key == 'left':
            ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
        elif event.key == 'right':
            ax.set_xlim(xlim[0] + dx, xlim[1] + dx)
    ax.set_title(f"Current Mode: {state.mode.upper()}", color='blue')
    fig.canvas.draw()


# 滚轮缩放
def on_scroll(event):
    zoom_rate = 0.1
    x_center = (ax.get_xlim()[0] + ax.get_xlim()[1]) / 2
    y_center = (ax.get_ylim()[0] + ax.get_ylim()[1]) / 2
    new_width = ax.get_xlim()[1] - ax.get_xlim()[0]
    new_height = ax.get_ylim()[1] - ax.get_ylim()[0]

    if event.step > 0:
        new_width *= (1 - zoom_rate)
        new_height *= (1 - zoom_rate)
    else:
        new_width *= (1 + zoom_rate)
        new_height *= (1 + zoom_rate)

    ax.set_xlim(x_center - new_width / 2, x_center + new_width / 2)
    ax.set_ylim(y_center - new_height / 2, y_center + new_height / 2)
    fig.canvas.draw()


# 绑定事件
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('button_release_event', on_released)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('key_press_event', pattern_change)
fig.canvas.mpl_connect('scroll_event', on_scroll)

plt.show()