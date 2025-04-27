import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
# 定义x轴的数据点
x = np.linspace(-6, 6, 100)
# 定义彩虹的基础曲线
y_base = 18 - 0.5 * x**2
# 使用列表推导式创建彩虹的层次
y_rainbow = [y_base + i * 0.5 for i in range(8)]
# 获取颜色映射器
cmap = cm.get_cmap('rainbow', 8)  # 'rainbow' 是一个颜色映射的名称，8 是颜色的数量
# 使用颜色映射器生成颜色列表
colors = [cmap(i) for i in np.linspace(0, 1, 8)]
# 绘制彩虹
plt.stackplot(x, y_rainbow, colors=colors, alpha=0.8)  # 添加透明度
# 添加标题
plt.title('Rainbow')
# 显示图例
plt.legend([f'Layer {i+1}' for i in range(8)], loc='upper left')
# 显示图形
plt.show()
