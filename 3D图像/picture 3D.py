import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
# ax=Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')

X=np.arange(-4,4,0.1)
# Y=0
Y=np.arange(-4,4,0.1)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
# plt.plot([0,0,0],[3,4,5],'k-.',lw=1)
# ax.plot3D([0,0,0],[3,4,5],'k-.',lw=1)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# ax.plot3D(X,Y,Z,c='b',lw=1)

######################################什么是子图
# 创建一个figure对象
#

# 显示图形
##########################################

plt.show()