import numpy as np
import matplotlib.pyplot as plt
ax=plt.subplot(211,projection='3d')
ax2=plt.subplot(221,projection='3d')

x=np.linspace(-10,10,100)
y=np.linspace(-5,5,100)
x,y=np.meshgrid(x,y)
z=x**2+y**2

ax.plot_surface(x,y,z,cmap='hot',lw=0,shade=1,rcount=50, ccount=50)
ax2.plot_surface(x,y,z,cmap='hot',lw=0,shade=0,rcount=50, ccount=50)
ax.set_title('shade=1')
ax2.set_title('shade=0')
# ax.plot(x,y,z)rcount=50, ccount=50    cmap='hot',
plt.show()
# # x=np.linspace(-10,10,100),antialiased=0
# # y=np.linspace(-10,10,100)lw=5,
# x = np.linspace(-12, 12, 100)
# y = np.linspace(-12, 12, 100)
# x,y=np.meshgrid(x,y)
#
# z1=np.sqrt(np.clip(100-x**2-y**2, 0, None))
# z2=-np.sqrt(np.clip(100-x**2-y**2, 0, None))
# z1[x**2 + y**2 > 100] = np.nan
# z2[x**2 + y**2 > 100] = np.nan
# ax.plot_surface(x,y,z1,cmap='hot')
# # ax.plot_surface(x,y,z2,cmap='hot')
# # plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 创建一个 3D 子图
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # 定义 x 和 y 的范围，确保范围足够大
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
#
# # 生成网格数据
# X, Y = np.meshgrid(x, y)
#
# # 计算 z1 和 z2，确保根号内的值非负
# radius_squared = 100  # 球体半径的平方
# Z1 = np.sqrt(radius_squared - X**2 - Y**2)  # 上半球
# Z2 = -np.sqrt(radius_squared - X**2 - Y**2)  # 下半球
#
# # 将不满足条件的点设置为 NaN（这样它们在绘图时会被忽略）
# Z1[X**2 + Y**2 > radius_squared] = np.nan
# Z2[X**2 + Y**2 > radius_squared] = np.nan
#
# # 绘制两个半球面
# ax.plot_surface(X, Y, Z1, cmap='hot', alpha=0.7)  # 上半球
# ax.plot_surface(X, Y, Z2, cmap='hot', alpha=0.7)  # 下半球
#
# # 设置标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # 显示图形
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 创建一个 3D 子图
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # 定义 x 和 y 的范围
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
#
# # 生成网格数据
# X, Y = np.meshgrid(x, y)
#
# # 计算 z1 和 z2，确保根号内的值非负
# radius = 10  # 球体半径
# Z1 = np.sqrt(radius**2 - X**2 - Y**2)
# Z1 = np.where((X**2 + Y**2) <= radius**2, Z1, np.nan)  # 确保只在球体内部计算
# Z2 = -np.sqrt(radius**2 - X**2 - Y**2)
# Z2 = np.where((X**2 + Y**2) <= radius**2, Z2, np.nan)  # 确保只在球体内部计算
#
# # 绘制两个半球面
# ax.plot_surface(X, Y, Z1, cmap='hot', alpha=0.7)  # 上半球
# ax.plot_surface(X, Y, Z2, cmap='hot', alpha=0.7)  # 下半球
#
# # 设置标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# # 显示图形
# plt.show()

