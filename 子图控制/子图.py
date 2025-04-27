import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()

# 添加第一个子图，位于2行2列布局的第一个位置
ax1 = fig.add_subplot(221)
ax1.plot([1, 2, 3], [1, 4, 9])

# 添加第二个子图，位于2行2列布局的第二个位置
ax2 = fig.add_subplot(222)
ax2.plot([1, 2, 3], [9, 4, 1])

# 添加第三个子图，位于2行2列布局的第三个位置
ax3 = fig.add_subplot(223)
ax3.plot([1, 2, 3], [1, 2, 3])

# 添加第四个子图，位于2行2列布局的第四个位置
ax4 = fig.add_subplot(224)
ax4.plot([1, 2, 3], [3, 2, 1])
plt.show()