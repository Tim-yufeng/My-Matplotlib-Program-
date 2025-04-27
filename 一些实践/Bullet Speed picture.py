# import matplotlib.pyplot as plt
# import numpy as np
#
# # 假设speeds是一个包含60个速度值的数组
# speeds = [39.6,28.6,42.2,35.4,30.7,28.7,30.6,29.4,31.0,28.5,35.6,37.0,36.5,24.7,27.1,31.7,27.4,34.5,36.0,28.9,27.6,25.9,39.4,37.0,27.8,43.9,38.6,33.1,30.7,31.1,35.2,39.6,38.9,29.7,37.5,26.3,27.0,25.2,33.2,28.2,34.3,40.8,26.4,36.1,43.1,35.8,26.5,29.1,37.7,42.2,27.2,35.7,28.9,32,27.3,27.6,30.0,29.6,29.7,28.5]
# average=np.mean(speeds)
# plt.figure(figsize=(10, 6))
# plt.scatter(np.arange(1, 61), speeds, color='blue',)  # 使用蓝色点表示速度
# plt.title('Water Bullet Speed Test Results')
# plt.xlabel('Bullet Number')
# plt.ylabel('Speed')
# plt.grid(True)
# # plt.axhline(average,color='red',label='average speed')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 假设speeds是60组水弹枪子弹速度数据
speeds = [39.6,28.6,42.2,35.4,30.7,28.7,30.6,29.4,31.0,28.5,35.6,37.0,36.5,24.7,27.1,31.7,27.4,34.5,36.0,28.9,27.6,25.9,39.4,37.0,27.8,43.9,38.6,33.1,30.7,31.1,35.2,39.6,38.9,29.7,37.5,26.3,27.0,25.2,33.2,28.2,34.3,40.8,26.4,36.1,43.1,35.8,26.5,29.1,37.7,42.2,27.2,35.7,28.9,32,27.3,27.6,30.0,29.6,29.7,28.5]  # 正态分布数据，平均35，标准差5

# 绘制散点图，设置透明度
plt.scatter(range(1, 61), speeds, alpha=0.6)

# 计算并显示平均速度
average_speed = np.mean(speeds)
plt.axhline(average_speed, color='red', linestyle='--', label='Average Speed')

# 显示图例
plt.legend()

# 设置标题和坐标轴标签
plt.title('Water Bullet Speed Test Results')
plt.xlabel('Bullet Number')
plt.ylabel('Speed (m/s)')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()