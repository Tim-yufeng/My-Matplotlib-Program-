import numpy as np
import matplotlib.pyplot as plt

# 定义标签
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# 定义数据
first = [20, 34, 30, 35, 27]
second = [25, 32, 34, 20, 25]
third = [21, 31, 37, 21, 28]
fourth = [26, 31, 35, 27, 21]
data = [first, second, third, fourth]
x = range(len(labels))
data = np.array(data)

# 定义基线类型
baseline = ['zero', 'sym', 'wiggle', 'weighted_wiggle']

# 创建图形和子图
fig, axes = plt.subplots(1, 4, figsize=(13, 3))

# 绘制堆积面积图
for ax, b in zip(axes, baseline):
    ax.stackplot(x, data, labels=labels, baseline=b)
    ax.set_xlim(0, 4)
    ax.set_xticks(x)
    ax.set_title(b)
    ax.legend()

# 显示图形
plt.show()
