import matplotlib.pyplot as plt
import numpy as np
ax1=plt.subplot(111,projection='3d')
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)
z1=x**2-y**2
ax1.plot_wireframe(x, y, z1, rstride=5, cstride=5, cmap='hot')
plt.show()

# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_zlabel('z')
# ax1.view_init(elev=90, azim=-90)
# ax2=plt.subplot(212)
# ax2.plot(x,y,lw=1)

# ax2.set_xlabel('x')
# ax2.set_ylabel('y')


# fig=plt.figure()
# ax1=fig.gca(projection='3d')
# ax2=plt.subplot(222,projection='3d')
# ax3=plt.subplot(223,projection='3d')
# ax4=plt.subplot(224,projection='3d')

# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)

# z2=1/(x*y)
# z3=x/y
# z4=y/x

# ax1.scatter(x,y,z1)

# ax1.plot_surface(x, y, z1, rstride=1, cstride=1, cmap='hot')
# ax1.plot_wireframe(x, y, z1, rstride=20, cstride=20,cmap='hot')
# ax2.plot_surface(x, y, z2, rstride=1, cstride=1, cmap='hot')
# ax3.plot_surface(x, y, z3, rstride=1, cstride=1, cmap='hot')
# ax4.plot_surface(x, y, z4, rstride=1, cstride=1, cmap='hot')
# ax1.scatter(np.linspace(0,10,5),np.linspace(0,10,5),np.linspace(0,10,5),c='r')
