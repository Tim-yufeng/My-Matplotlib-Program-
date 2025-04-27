import matplotlib.pyplot as plt
x_point=[]
y_point=[]
def onmotion(event):
    global x_point,y_point
    if event.inaxes:
        print(f'Mouse at {event.xdata}, {event.ydata}')
# 作线图！
        x_point.append(event.xdata)
        y_point.append(event.ydata)
        plt.plot(x_point,y_point,c='r')
        plt.draw()
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
cid = fig.canvas.mpl_connect('motion_notify_event', onmotion)
plt.show()
