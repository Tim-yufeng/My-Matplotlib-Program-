import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# 定义项目任务和时间
tasks = [
    {'任务': '任务1', '开始': datetime(2024, 11, 1), '结束': datetime(2024, 11, 5)},
    {'任务': '任务2', '开始': datetime(2024, 11, 3), '结束': datetime(2024, 11, 7)},
    {'任务': '任务3', '开始': datetime(2024, 11, 6), '结束': datetime(2024, 11, 10)},
]

# 设置图形
fig, ax = plt.subplots(figsize=(10, 6))

# 设置日期格式
date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)

# 设置x轴的显示范围
ax.set_xlim([datetime(2024, 10, 31), datetime(2024, 11, 15)])

# 设置y轴的刻度位置
yticks = range(len(tasks))

# 设置y轴的刻度标签
ax.set_yticks(yticks)
ax.set_yticklabels([task['任务'] for task in tasks])

# 绘制甘特图
for i, task in enumerate(tasks):
    # 将日期转换为matplotlib的数值格式
    start_num = mdates.date2num(task['开始'])
    end_num = mdates.date2num(task['结束'])
    # 计算任务的持续时间
    duration = end_num - start_num
    # 绘制任务条形
    ax.broken_barh([(start_num, duration)], (i, 0.8), facecolors='tab:blue')

# 设置网格
ax.grid(True)

# 显示图形
plt.show()