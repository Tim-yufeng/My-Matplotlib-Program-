import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,6,100)
y=18-0.5*x**2
y_list=[]
for i in range(8):
    y_list.append(list(y+i*0.5))
y_array=np.array(y_list)
plt.stackplot(x,y_array,colors=['w','purple','b','c','g','y','orange','r'],baseline='zero')
# plt.legend()
plt.title('Rainbow')
plt.show()

x = np.linspace(-6, 6, 100)

# 定义彩虹的基础曲线
y_base = 18 - 0.5 * x**2

# 使用列表推导式创建彩虹的层次
y_rainbow = [y_base + i * 0.5 for i in range(8)]

# 定义彩虹的颜色
colors = ['w', 'purple', 'b', 'c', 'g', 'y', 'orange', 'r']

# 绘制彩虹
plt.stackplot(x, y_rainbow, colors=colors, alpha=0.8)  # 添加透明度

# 添加标题
plt.title('Rainbow')

# 显示图例
plt.legend([f'Layer {i+1}' for i in range(8)], loc='upper left')

# 显示图形
plt.show()