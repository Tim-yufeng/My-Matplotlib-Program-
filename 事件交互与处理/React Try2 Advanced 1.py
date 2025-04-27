import  matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
class DrawState:
    def __init__(self):
        self.pressed=0
        self.line_number=0
        self.circle_number=0
        self.x_list=[]
        self.y_list=[]
        self.lines=[]
        self.radius_values=[]
        self.exist_lines=[]
        self.circles=[]
        self.exist_circles=[]
        self.figure_pattern='typical'
        self.x1,y1,x2,y2,r_value=None,None,None,None,None

state = DrawState()
ax.set_title(f"Current Mode: {state.figure_pattern}", color='blue')
def on_click(event):   ####鼠标点击事件
    ax.scatter(event.xdata,event.ydata,color='r',s=10)
    plt.draw()
    state.pressed=1-state.pressed

def on_released(event):    #### 鼠标松开事件
    ax.scatter(event.xdata,event.ydata,color='r',s=10)
    plt.draw()
    state.pressed=1-state.pressed
    state.x_list=[]
    state.y_list=[]
    if state.figure_pattern=='linear':
        state.line_number += 1
        state.exist_lines.append(state.lines[-1])
        if state.line_number >= 1:
            for line in state.exist_lines[-state.line_number:]:
                ax.add_line(line)
            fig.canvas.draw()
    if state.figure_pattern=='circle':
        state.circle_number+=1
        state.exist_circles.append(state.circles[-1])
        if state.circle_number>1:
            for circle in state.exist_circles[-state.circle_number:]:
                ax.add_line(circle)
            fig.canvas.draw()

def typical_move(event):       ###  一般曲线绘制函数
    if state.pressed==1:
        state.x_list.append(event.xdata)
        state.y_list.append(event.ydata)
        ax.plot(state.x_list,state.y_list,c='r')
        plt.draw()

def linear_move(event):          ###   直线绘制函数
    if event.name == 'motion_notify_event' and state.pressed==1 and event.inaxes is not None:
        state.x_list.append(event.xdata)
        state.y_list.append(event.ydata)
        state.x1 = state.x_list[0]
        state.y1 = state.y_list[0]
        state.x2 = state.x_list[-1]
        state.y2 = state.y_list[-1]
        if None in (state.x1, state.x2, state.y1,state.y2):
            raise ValueError("One or more coordinates are None. Please check the input data.")
        state.r_value = np.sqrt((state.x2 - state.x1) ** 2 + (state.y2 - state.y1) ** 2)
        line,=ax.plot([state.x1,state.x2],[state.y1,state.y2],c='r')
        state.lines.append(line)
        r = ax.text((state.x1 + state.x2) / 2 + 0.5, (state.y1 + state.y2) / 2 + 0.5, 'r={}'
                    .format(round(state.r_value, 2)),
                    fontdict={'fontsize': 10, 'fontweight': 'light', 'color': 'blue'})
        state.radius_values.append(r)
        if len(state.lines)>1:
            for line in state.lines[:-1]:
                line.remove()
            state.lines=state.lines[-1:]
            plt.draw()

        if len(state.radius_values)>1:
            for r in state.radius_values[:-1]:
                r.remove()
            state.radius_values=state.radius_values[-1:]
            plt.draw()
        plt.draw()
    return state.x1,state.x2,state.y1,state.y2,state.r_value

def circle_move(event):    ### 圆形绘制函数
    x1,x2,y1,y2,r_value=linear_move(event)
    theta=np.linspace(0,2*np.pi,100)
    circle,=ax.plot(x1+r_value*np.cos(theta),y1+r_value*np.sin(theta),c='r')
    state.circles.append(circle)
    if len(state.circles)>1:
        for circle in state.circles[:-1]:
            circle.remove()
        state.circles=state.circles[-1:]
        plt.draw()
    plt.draw()

def on_motion(event):        ####   整合各图形绘制的函数，鼠标移动控制
    if state.pressed==1:
        if state.figure_pattern =='typical':
            typical_move(event)
            plt.draw()
        if state.figure_pattern=='linear':
            linear_move(event)
            plt.draw()
        if state.figure_pattern=='circle':
            circle_move(event)
            plt.draw()

def pattern_change(event):   ### 键盘事件控制函数
    if event.name=='key_press_event' and event.key=='l':  ###直线
        state.figure_pattern='linear'
    elif event.name=='key_press_event' and event.key=='r':   ###圆
        state.figure_pattern='circle'
    elif event.name == 'key_press_event' and event.key == 't':   ###一般曲线
        state.figure_pattern='typical'
    if event.key == 'delete':   #### 清空 但是模式不变
        ax.clear()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
        state.pressed = 0
        state.line_number = 0
        state.circle_number = 0
        state.x_list = []
        state.y_list = []
        state.lines = []
        state.radius_values = []
        state.exist_lines = []
        state.circles = []
        state.exist_circles = []
    if event.key == 'up':
        ax.set_ylim(ax.get_ylim()[0] + 0.1, ax.get_ylim()[1] + 0.1)
    if event.key == 'down':
        ax.set_ylim(ax.get_ylim()[0] - 0.1, ax.get_ylim()[1] - 0.1)
    if event.key == 'left':
        ax.set_xlim(ax.get_xlim()[0] - 0.1, ax.get_xlim()[1] - 0.1)
    if event.key == 'right':
        ax.set_xlim(ax.get_xlim()[0] + 0.1, ax.get_xlim()[1] + 0.1)
    fig.canvas.draw()
    ax.set_title(f"Current Mode: {state.figure_pattern}", color='blue')


def on_scroll(event):
    ax.set_xlim(ax.get_xlim()[0] * (1-event.step*0.01), ax.get_xlim()[1] * (1-event.step*0.01))
    ax.set_ylim(ax.get_ylim()[0] * (1-event.step*0.01), ax.get_ylim()[1] * (1-event.step*0.01))
    fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event',on_click)
fig.canvas.mpl_connect('button_release_event',on_released)
fig.canvas.mpl_connect('motion_notify_event',on_motion)
fig.canvas.mpl_connect('key_press_event',pattern_change)
fig.canvas.mpl_connect('scroll_event', on_scroll)

plt.show()

