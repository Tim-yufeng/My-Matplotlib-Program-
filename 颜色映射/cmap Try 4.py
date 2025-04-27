import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import BoundaryNorm, ListedColormap
# 创建数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(x**2 + y**2)  # 数据范围在 [-1, 1]

# 定义颜色边界
# boundaries = [-1, -0.5, 0, 0.5, 1]
boundaries = np.linspace(-1, 1, 11)  # 10 个区间
cmap = ListedColormap(['blue', 'green', 'yellow', 'red'])  # 4 种颜色
# 创建 BoundaryNorm 对象，指定颜色数量
norm = BoundaryNorm(boundaries, ncolors=10)
# cmap = plt.cm.viridis_r
# 创建图形和轴
ax = plt.subplot(projection='3d')

# 使用 BoundaryNorm 绘制图像
surf=ax.plot_surface(x,y,z,cmap=cmap, norm=norm)
# surf = ax.imshow(z, cmap='viridis', norm=norm)
plt.colorbar(surf, ax=ax, boundaries=boundaries, ticks=boundaries)
plt.title('BoundaryNorm with viridis')
plt.show()
