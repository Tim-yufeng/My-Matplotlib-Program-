import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, SymLogNorm
from mpl_toolkits.mplot3d import Axes3D

# 创建数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.exp(x**2 + y**2)

# 创建图形和轴
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# 使用 LogNorm
norm1 = LogNorm()
surf1 = ax1.plot_surface(x, y, z, cmap='viridis', norm=norm1)
fig.colorbar(surf1, ax=ax1)
ax1.set_title('LogNorm')

# 使用 SymLogNorm
norm2 = SymLogNorm(linthresh=10, linscale=1, base=np.e)
surf2 = ax2.plot_surface(x, y, z, cmap='viridis', norm=norm2)
fig.colorbar(surf2, ax=ax2)
ax2.set_title('SymLogNorm')

plt.show()
