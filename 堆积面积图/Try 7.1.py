import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()

# 数据
labels = ['G1', 'G2', 'G3', 'G4']
data = np.array([[20, 34, 30, 35], [25, 32, 34, 20], [21, 31, 37, 21], [26, 31, 35, 27]])
x = np.arange(len(labels))
# 绘制堆积面积图
ax.stackplot(x, data, labels=labels)
ax.legend()
plt.show()


