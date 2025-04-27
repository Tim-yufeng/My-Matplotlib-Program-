import numpy as np
import matplotlib.pyplot as plt
cmap='viridis'
fig1=plt.figure()
fig2=plt.figure()
ax1=fig1.add_subplot()
ax2=fig2.add_subplot(projection='3d')
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)
# 绘制等高线图并添加等高线标签
contours = ax1.contour(X,Y, Z,  levels=10, cmap=cmap, linewidths=1.5, linestyles='solid')
ax1.clabel(contours, inline=True, fmt='%1.1f', fontsize=10)
# 设置标题和坐标轴标签
ax1.set_title('Contour Plot Example')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax2.set_title('Contour Plot 3D Origin')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.plot_surface(X,Y,Z,cmap=cmap)
plt.show()


