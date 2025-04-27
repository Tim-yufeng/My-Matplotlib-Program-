import matplotlib.pyplot as plt
import numpy as np
ax=plt.subplot(111,projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
z=-z
color=(0.33,0,0.15)
ax.plot(x,y,z,c=color,lw=40)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.title('你的物理作业写得就是一坨这个！！')
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.collections import LineCollection
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# z = np.linspace(0, 1, 100)
# x = z * np.sin(20 * z)
# y = z * np.cos(20 * z)
# z = -z
# lw = 40 / (39 * (1 - x) + 1)
#
# # 创建线段
# points = np.array([x, y, z]).T.reshape(-1, 1, 3)
# segments = np.concatenate([points[:-1], points[1:]], axis=1)
#
# # 创建LineCollection
# lc = LineCollection(segments, linewidths=lw[:-1], colors='brown')
# ax.add_collection3d(lc)
#
# ax.set_xlim(x.min(), x.max())
# ax.set_ylim(y.min(), y.max())
# ax.set_zlim(z.min(), z.max())
#
# plt.show()
