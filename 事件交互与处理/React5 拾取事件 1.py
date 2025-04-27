import numpy as np
import matplotlib.pyplot as plt

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    # 先将 zip 转为列表，针对每个元素进行 round()
    points = list(zip(xdata[ind], ydata[ind]))
    # 对每个坐标 (x, y) 单独四舍五入
    rounded_points = [(float(round(x, 2)), float(round(y, 2))) for x, y in points]
    print(f'You picked {len(ind)} points: {rounded_points}')
fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(100),'o', picker=5)
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()

