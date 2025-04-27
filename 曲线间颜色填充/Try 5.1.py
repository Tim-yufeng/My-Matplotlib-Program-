# import matplotlib.pyplot as plt
# import numpy as np
# x=1
# y=2
# plt.scatter(x,y,label='(1,2)')
# plt.legend(loc=(0.5,0.5),frameon=1,labels='coordination')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
# fig=plt.figure()
fig,ax=plt.subplots()
# 创建一些数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# 绘制两条线，并为它们添加标签
ax.plot(x, y1,'r-', label='sin(x)')
ax.plot(x, y2, label='cos(x)')
ax.fill_between(x, y1, y2, color='yellow', alpha=0.3)
# 添加图例，设置无边框，两列显示
plt.legend(frameon=0, ncol=1,fontsize=10,edgecolor='b',facecolor='y')
plt.show()




#where = (y1 > y2),

