import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as ccolors
import random
import time

# 设置画布
fig, ax = plt.subplots()
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.set_aspect('equal')

# 绘制其他图形
ax.plot([1, 1], [0, 1.8], c='purple') #y1
ax.plot([10, 10], [0, 1.8], c='purple') #y10
line2,=ax.plot([0.5, 4.5], [1.8, 1.8], c='purple') #y2
ax.plot([10.5, 6.5], [1.8, 1.8], c='purple')  #y8
line4,=ax.plot([1.5, 4.5], [2.8, 2.8], c='purple') #y4
ax.plot([9.5, 6.5], [2.8, 2.8], c='purple') #y7
ax.plot([4.5, 4.5], [0, 5], c='purple') #y5
ax.plot([6.5, 6.5], [0, 5], c='purple') #y6
ax.plot([4.5, 3.8], [5, 5.5], c='purple') #y14
ax.plot([6.5, 7.2], [5, 5.5], c='purple') #y15
ax.plot([3.8, 4.5], [5.5, 5.5], c='purple') #y12
ax.plot([7.2, 6.5], [5.5, 5.5], c='purple') #y13

# 绘制曲线
x_1 = np.linspace(0.5, 1.5, 20)
y_1 = np.sin((np.pi / 2) * (x_1 - 1.5)) + 2.8
ax.plot(x_1, y_1, c='purple')

x_2 = np.linspace(9.5, 10.5, 20)
y_2 = np.sin((np.pi / 2) * (x_2 - 11.5)) + 2.8
ax.plot(x_2, y_2, c='purple')

x_3 = np.linspace(4.5, 6.5, 20)
y_3 = 6.5 - np.abs(x_3 - 5.5)
ax.plot(x_3, y_3, c='purple')

# 五角星参数
a = 0.1
b = ((np.sqrt(5) - 1) / 4 + a) / np.sin(0.4 * np.pi)

# 计算五角星的顶点
x_star = []
y_star = []
for t in range(0, 10):
    if t % 2 == 0:
        x_star.append(np.cos(t * 0.2 * np.pi) * b)
        y_star.append(np.sin(t * 0.2 * np.pi) * b)
    if t % 2 != 0:
        x_star.append(np.cos(t * 0.2 * np.pi) * b * np.cos(0.4 * np.pi))
        y_star.append(np.sin(t * 0.2 * np.pi) * b * np.cos(0.4 * np.pi))
x_star = np.array(x_star)
y_star = np.array(y_star)

# 定义旋转角度（例如 30 度）
theta = np.radians(18)  # 将角度转换为弧度

# 旋转五角星的顶点
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])
rotated_star = np.dot(rotation_matrix, np.vstack([x_star, y_star]))

# 将五角星移动到指定位置 (5.5, 5.7)
rotated_star[0, :] += 5.5
rotated_star[1, :] += 5.7

# 绘制五角星并填充红色
ax.fill(rotated_star[0, :], rotated_star[1, :], color='red')

# 显示图形
# plt.show()
plt.fill_between(np.linspace(1.5,4.5,20),np.linspace(2.8,2.8,20),np.linspace(1.8,1.8,20),color=(0.35, 0.45, 0.40))
plt.fill_between(np.linspace(9.5,6.5,20),np.linspace(2.8,2.8,20),np.linspace(1.8,1.8,20),color=(0.35, 0.45, 0.40))
plt.fill_between(np.linspace(0.5,1.5,20),y_1,np.linspace(1.8,1.8,20),color=(0.35, 0.45, 0.40))
plt.fill_between(np.linspace(9.5,10.5,20),y_2,np.linspace(1.8,1.8,20),color=(0.35, 0.45, 0.40))

def growth():
    global fig,ax
    i = 0
    x0 = 5.5
    y0 = 0
    a = 4.5
    b = 6.5
    h = 5
    step=0.2
    while i<=1000 and y0<h:

        t = random.randint(1, 6)  # a是范围的下限，b是范围的上限
        if t==1 and x0+step<=b:
            x1=x0+step
            y1=y0+step
        elif t==1 and x0+step>b:
            x1=x0-step
            y1=y0+step
        if t==2 and x0+step<=b:
            x1=x0+step
            y1=y0
        elif t==2 and x0+step>b:
            x1=x0-step
            y1=y0
        # if t==3:
        #     x1=x0+1
        #     y1=y0-1
        if t==3:
            x1=x0
            y1=y0+step
        if t==4:
            x1=x0
            y1=y0
        # if t==6:
        #     x1=x0
        #     y1=y0-1
        if t==5 and x0-step>=a:
            x1=x0-step
            y1=y0+step
        elif t==5 and x0-step<a:
            x1 = x0 + step
            y1 = y0 + step
        if t==6 and x0-step>=a:
            x1=x0-step
            y1=y0
        elif t==6 and x0-step<a:
            x1 = x0 + step
            y1 = y0
        # if t==9:
        #     x1=x0-1
        #     y1=y0-1
        ax.plot([x0,x1],[y0,y1],c='green',lw=1)
        x0=x1
        y0=y1
        i+=1
        # time.sleep(0.5)
    # plt.show()
j=0
plt.ion()
while j<=10:
    growth()
    # time.sleep(1)
    plt.pause(1)
    j+=1
plt.ioff()
plt.show()