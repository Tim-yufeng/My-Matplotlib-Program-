# import matplotlib.pyplot as plt
# import numpy as np
# t=1
# colo=np.array([0.1,0,0.1])
# col=tuple(colo*t)
# theta=np.linspace(0,np.pi*2,100)
# r1=1-np.sin(theta)
# r2=0
# # plt.polar(theta,r1,c=col)
# # plt.fill_between(theta,r1,r2,color=col)
# # plt.title("t={}".format(t))
# # fig=plt.figure()
# fig,ax=plt.subplots(1,10,projection='polar')
# for i in range(1,10):
#     colo = np.array([0.1, 0, 0.1])
#     col = tuple(colo * i)
#     ax[i].plot(theta,r1,c=col)
#     plt.fill_between(theta, r1, r2, color=col)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(0,np.pi*2,100)
r1=1-np.sin(theta)
r2=0

plt.figure(figsize=(15, 15))  # 设置整个图形的大小
for t in range(10):
    for i in range(10):
        ax = plt.subplot(10, 10, t*10+i + 1, polar=True)  # 创建极坐标子图
        colo = np.array([0.1, 0, 0.1/(t+1)])
        col = tuple(colo * (i + 1))
        ax.plot(theta, r1, c=col)
        ax.fill_between(theta, r1, r2, color=col)
        labels = ax.get_xticklabels()
        for label in labels:
            label.set_color('None')
        labels2 = ax.get_yticklabels()
        for label in labels2:
            label.set_color('None')  # 去掉圆周标签
        ax.grid(False)
plt.show()
