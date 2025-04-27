import numpy as np
import matplotlib.pyplot as plt
# 定义函数
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))
# 创建网格数据
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 绘制线框图
ax = plt.subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='blue', linewidth=1, linestyle='-', alpha=0.8)
# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# 设置标题
ax.set_title('3D Wireframe Plot')
plt.show()
