import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2,5,50)
y=x**2
plt.figure(1)
plt.plot(x,y)
new_ticks=np.linspace(-2.5,2.5,5)
# print(new_ticks)
plt.xticks(new_ticks)
plt.xlabel('$jyf$',color='red')
plt.ylabel('$wlr$',color='purple')
ax=plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('purple')
ax.spines['bottom'].set_color('red')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# ax.spines['left'].set_linewidth(20)
for spine in ax.spines.values():
    spine.set_linewidth(2)
    # spine.set_capstyle('butt')
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# 创建一个图形窗口
plt.figure(2,figsize=(10, 6))

# 生成一些数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 在图形中绘制数据
plt.plot(x, y)

# 设置标题和标签
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()