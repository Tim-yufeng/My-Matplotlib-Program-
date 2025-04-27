import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
speeds = [39.6,28.6,42.2,35.4,30.7,28.7,30.6,29.4,31.0,28.5,35.6,37.0,36.5,24.7,27.1,31.7
    ,27.4,34.5,36.0,28.9,27.6,25.9,39.4,37.0,27.8,43.9,38.6,33.1,30.7,31.1,35.2,39.6,38.9,
          29.7,37.5,26.3,27.0,25.2,33.2,28.2,34.3,40.8,26.4,36.1,43.1,35.8,26.5,29.1,37.7,
          42.2,27.2,35.7,28.9,32,27.3,27.6,30.0,29.6,29.7,28.5]  # 正态分布数据，平均35，标准差5
# fig=plt.figure()
fig=plt.figure(figsize=(10, 6))
ax1=fig.add_subplot(221)

# 绘制散点图，设置透明度
ax1.scatter(range(1, 61), speeds, alpha=0.6)

# 计算并显示平均速度
average_speed = np.mean(speeds)
plt.axhline(average_speed, color='red', linestyle='--', label='Average Speed')
# 设置标题和坐标轴标签
plt.title('Water Bullet Speed Test Results')
plt.xlabel('Bullet Number')
plt.ylabel('Speed (m/s)')

# 显示网格
plt.grid(True)
ax2=fig.add_subplot(222)

# 使用Seaborn生成箱型图
# ax2.figure(figsize=(10, 6))
sns.boxplot(data=speeds,ax=ax2)
plt.title('Boxplot of Water Bullet Speeds')
plt.ylabel('Speed (m/s)')

ax3=fig.add_subplot(223)
# ax3.figure(figsize=(10, 6))
sns.violinplot(data=speeds,ax=ax3)
plt.title('Violinplot of Water Bullet Speeds')
plt.ylabel('Speed (m/s)')

ax4=fig.add_subplot(224)
plt.hist(speeds,bins=20,color='r',alpha=0.7)
plt.title('Histogram of Water Bullet Speeds')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.show()
# 显示图例
