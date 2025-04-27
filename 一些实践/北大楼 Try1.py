# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()
# ax.set_xlim(0,11)
# ax.plot([1,1],[0,1],c='purple')
# ax.plot([10,10],[0,1],c='purple')
# ax.plot([0.5,4],[1,1],c='purple')
# ax.plot([10.5,7],[1,1],c='purple')
# ax.plot([1.5,4],[2,2],c='purple')
# ax.plot([9.5,7],[2,2],c='purple')
# # ax.plot(np.sin((np.pi/2)*(np.linspace(0.5,1.5,20)-1.5))+2,c='purple')
# # ax.plot(np.sin((np.pi/2)*(12.5-np.linspace(0.5,1.5,20)))+2,c='purple')
# ax.plot([4,4],[0,5],c='purple')
# ax.plot([7,7],[0,5],c='purple')
# ax.plot([4,3.3],[5,5.5],c='purple')
# ax.plot([7,7.7],[5,5.5],c='purple')
# ax.plot([3.3,4.5],[5.5,5.5],c='purple')
# ax.plot([7.7,6.5],[5.5,5.5],c='purple')
# # ax.plot(6.5-np.abs(np.linspace(4.5,6.5,20)-5.5),c='purple')
# x_1=np.linspace(0.5,1.5,20)
# y_1=np.sin((np.pi/2)*(x_1-1.5))+2
# ax.plot(x_1,y_1,c='purple')
# x_2=np.linspace(9.5,10.5,20)
# y_2=np.sin((np.pi/2)*(x_2-11.5))+2
# ax.plot(x_2,y_2,c='purple')
# x_3=np.linspace(4.5,6.5,20)
# y_3=6.5-np.abs(x_3-5.5)
# ax.plot(x_3,y_3,c='purple')
#
# a = 0.5
# b = ((np.sqrt(5) - 1) / 4 + a) / np.sin(0.4 * np.pi)
#
# x_1_1=np.linspace(-np.cos(0.3*np.pi)*b,np.cos(0.3*np.pi)*b,20)
# x_2_1=np.linspace(-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b,20)
# x_1_1+=5.5*np.linspace(1,1,20)
# x_2_1+=5.5*np.linspace(1,1,20)
#
# y_1_1=-np.tan(0.4*np.pi)*np.abs(x_1_1)+b
# y_1_2=-np.tan(0.2*np.pi)*np.abs(x_1_1)-b*np.cos(0.4*np.pi)
# y_2_2=np.tan(0.2*np.pi)*np.abs(x_2_1)-b*np.cos(0.4*np.pi)
# y_2_1=b*np.cos(0.4*np.pi)
# y_1_1+=6*np.linspace(1,1,20)
# y_1_2+=6*np.linspace(1,1,20)
# y_2_1+=6*np.linspace(1,1,20)
# y_2_2+=6*np.linspace(1,1,20)
#
# ax.plot(x_1_1,y_1_1,c='r')
#
# ax.plot(x_1_1,y_1_2,c='r')
# ax.fill_between(x_1_1,y_1_1,y_1_2,color='r')
#
#
# ax.plot([-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b],[y_2_1,y_2_1],c='r')
# ax.plot(x_2_1,y_2_2,c='r')
# ax.fill_between(x_2_1,y_2_1,y_2_2,color='r')
#
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 设置画布
fig, ax = plt.subplots()
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.set_aspect('equal')

# 绘制其他图形
ax.plot([1, 1], [0, 1.8], c='purple')
ax.plot([10, 10], [0, 1.8], c='purple')
ax.plot([0.5, 4.5], [1.8, 1.8], c='purple')
ax.plot([10.5, 6.5], [1.8, 1.8], c='purple')
ax.plot([1.5, 4.5], [2.8, 2.8], c='purple')
ax.plot([9.5, 6.5], [2.8, 2.8], c='purple')
ax.plot([4.5, 4.5], [0, 5], c='purple')
ax.plot([6.5, 6.5], [0, 5], c='purple')
ax.plot([4.5, 3.8], [5, 5.5], c='purple')
ax.plot([6.5, 7.2], [5, 5.5], c='purple')
ax.plot([3.8, 4.5], [5.5, 5.5], c='purple')
ax.plot([7.2, 6.5], [5.5, 5.5], c='purple')

# 绘制曲线
x_1 = np.linspace(0.5, 1.5, 20)
y_1 = np.sin((np.pi / 2) * (x_1 - 1.5)) + 2.8
ax.plot(x_1, y_1, c='purple')

x_2 = np.linspace(9.5, 10.5, 20)
y_2 = np.sin((np.pi / 2) * (x_2 - 11.5)) + 2.8
ax.plot(x_2, y_2, c='purple')

x_3 = np.linspace(4.5, 6.5, 20)
y_3 = 6.5 - np.abs(x_3 - 5.5)
ax.plot(x_3, y_3, c='purple')

# 五角星参数
a = 0.15
b = ((np.sqrt(5) - 1) / 4 + a) / np.sin(0.4 * np.pi)

# 计算五角星的顶点
# angles = np.linspace(0, 2 * np.pi, 6)[:-1]  # 五个顶点
# x_star = np.cos(angles) * b
# y_star = np.sin(angles) * b
x_star=[]
y_star=[]
for t in range(0,10):
    if t%2==0:
        x_star.append(np.cos(t*0.2*np.pi)*b)
        y_star.append(np.sin(t * 0.2 * np.pi) * b)
    if t%2!=0:
        x_star.append(np.cos(t*0.2*np.pi)*b*np.cos(0.4*np.pi))
        y_star.append(np.sin(t * 0.2 * np.pi) * b * np.cos(0.4 * np.pi))
x_star=np.array(x_star)
y_star=np.array(y_star)
# 将五角星移动到指定位置 (5.5, 6)
x_star += 5.5
y_star += 5.7

# 绘制五角星并填充红色
ax.fill(x_star, y_star, color='red')

# 显示图形
plt.show()

