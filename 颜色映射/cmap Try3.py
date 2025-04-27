import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm
linthresh=10
linscale=1000                # 方便修改
ax=plt.subplot(projection='3d')
x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
x,y=np.meshgrid(x,y)
z=np.exp(x**2+y**2)          # 定义函数
norm1=LogNorm()
norm2=SymLogNorm(linthresh=10,linscale=linscale,base=np.e)  # 定义两个norm
ax.plot_surface(x,y,z,cmap='viridis',norm=norm2,alpha=0.8,
                label='$z=np.exp(x^2+y^2)$')         # 主要图像
theta=np.linspace(0,2*np.pi,100)
r=np.sqrt(np.log(linthresh))
plt.plot(r*np.sin(theta),r*np.cos(theta),c='k',lw=2,
         label='$x^2+y^2=ln(linthresh)$')                # 黑圈标明阈值范围
plt.title(f'linthresh=10,linscale={linscale}')
plt.legend()                 # 标题与图例
plt.show()

