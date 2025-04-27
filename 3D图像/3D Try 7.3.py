import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# 绘制等高线图
plt.figure(figsize=(12, 4))

# 默认 extent
plt.subplot(1, 2, 1)
plt.contour(X, Y, Z, cmap='viridis')
plt.title("Default extent")

# 使用 extent 定义范围
plt.subplot(1, 2, 2)
plt.contour(X, Y, Z, extent=[-5, 5, -5, 5], cmap='viridis')
plt.title("extent=[-5, 5, -5, 5]")

plt.tight_layout()
plt.show()
