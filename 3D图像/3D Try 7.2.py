import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# 绘制等高线图
plt.figure(figsize=(10, 4))

# 默认 origin='upper'
plt.subplot(1, 2, 1)
plt.contour(X, Y, Z, origin='upper', cmap='viridis')
plt.title("origin='upper'")

# 使用 origin='lower'
plt.subplot(1, 2, 2)
plt.contour(X, Y, Z, origin='lower', cmap='viridis')
plt.title("origin='lower'")

plt.tight_layout()
plt.show()
