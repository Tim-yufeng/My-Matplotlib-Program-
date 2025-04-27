import matplotlib.pyplot as plt
import numpy as np

a = 1
b = ((np.sqrt(5) - 1) / 4 + a) / np.sin(0.4 * np.pi)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# # 计算五角星的顶点坐标
# x1 = np.linspace(-np.cos(0.3 * np.pi) * b, np.cos(0.3 * np.pi) * b, 20)
# y1 = -np.tan(0.4 * np.pi) * np.abs(x1) + b
#
# x2 = [-np.cos(0.3 * np.pi) * b, np.cos(0.1 * np.pi) * b]
# y2 = [-np.sin(0.3 * np.pi) * b, np.sin(0.1 * np.pi) * b]
#
# x3 = [np.cos(0.3 * np.pi) * b, -np.cos(0.1 * np.pi) * b]
# y3 = [-np.sin(0.3 * np.pi) * b, np.sin(0.1 * np.pi) * b]
#
# x4 = [-np.cos(0.1 * np.pi) * b, np.cos(0.1 * np.pi) * b]
# y4 = [np.sin(0.1 * np.pi) * b, np.sin(0.1 * np.pi) * b]
#
# # 提取五角星的所有顶点
# x = np.concatenate([x1, x2, x3, x4])
# y = np.concatenate([y1, y2, y3, y4])
#
# # 绘制五角星并填充红色
# ax.fill(x, y, color='red')
#
# # 绘制五角星的边界
# ax.plot(x1, y1, c='m')
# ax.plot(x2, y2, c='m')
# ax.plot(x3, y3, c='m')
# ax.plot(x4, y4, c='m')

# plt.show()

x_1=np.linspace(-np.cos(0.3*np.pi)*b,np.cos(0.3*np.pi)*b,20)
y_1=-np.tan(0.4*np.pi)*np.abs(x_1)+b
ax.plot(x_1,y_1,c='m')
y_1_2=-np.tan(0.2*np.pi)*np.abs(x_1)-b*np.cos(0.4*np.pi)
ax.plot(x_1,y_1_2,c='m')
ax.fill_between(x_1,y_1,y_1_2,color='r')
x_2=np.linspace(-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b,20)
y_2_2=np.tan(0.2*np.pi)*np.abs(x_2)-b*np.cos(0.4*np.pi)
y_2=b*np.cos(0.4*np.pi)
ax.plot([-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b],[y_2,y_2],c='m')
ax.plot(x_2,y_2_2,c='m')
ax.fill_between(x_2,y_2,y_2_2,color='r')
plt.show()