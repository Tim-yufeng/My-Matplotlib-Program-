# import matplotlib.pyplot as plt
# import numpy as np
# ax=plt.subplot(111,projection='3d')
# for x in np.linspace(-1,1,10):
#     for y in np.linspace(-1, 1, 10):
#         for z in np.linspace(-1, 1, 10):
#             if x**2+y**2+z**2<=1:
#                 ax.plot(x,y,z,lw=5)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
axis_range=3
# 创建 3D 子图
fig = plt.figure()
# ax = fig.add_subplot(211, projection='3d')
ax2= fig.add_subplot(111, projection='3d')
# 生成球体的网格数据
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

x2=np.linspace(-axis_range,axis_range,100)
y2=np.linspace(-axis_range,axis_range,100)
z2=np.linspace(-axis_range,axis_range,100)

# 绘制球体
# # ax.plot_surface(x, y, z, color='b', alpha=1)
# ax.set_aspect('equal')
# ax.plot(x2,0,0,c='k')
# ax.plot(0,y2,0,c='k')
# ax.plot(0,0,z2,c='k')
# # 设置轴标签
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_zlabel('Z Label')
x2,y2=np.meshgrid(x2,y2)
ax2.scatter(x2,y2,z2)
# ax2.view_init(0,-90)
# 显示图像
plt.show()


