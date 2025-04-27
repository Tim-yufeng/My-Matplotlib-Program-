import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,np.pi*2,100)
r1=1-np.sin(theta)
r2=0
ax1=plt.subplot(221,projection='polar')
ax2=plt.subplot(222,projection='polar')
ax3=plt.subplot(223,projection='polar')
ax4=plt.subplot(224,projection='polar')  # 分别创建四个子图
ax1.plot(theta, r1, marker='^', ms=5, mfc='red',
          mec='blue', color='green', linestyle='--', linewidth=2,
          label='示例曲线', alpha=0.8)    # 子图1
colorlist_1=['g','b','m']
for i in np.linspace(0,2,3):
    ax2.plot(theta+i*np.pi*2/3, r1, c=colorlist_1[int(i)],alpha=0.5)
    ax2.fill_between(theta+i*np.pi*2/3,r1,r2, color=colorlist_1[int(i)],alpha=0.5) # 子图2
colorlist_2=['r','orange','y','g','c','b','m','purple']
for i in np.linspace(0,7,8):
    ax3.plot(theta, r1*(i+1), c=colorlist_2[int(i)],alpha=1,label='whatsername')
    ax3.fill_between(theta,r1*i,r1*(i+1), color=colorlist_2[int(i)],alpha=1) # 子图3
for i in np.linspace(0,7,8):
    ax4.plot(theta+i*np.pi/4, r1, c=colorlist_2[int(i)],alpha=0.5,label='whatsername')
    ax4.fill_between(theta+i*np.pi/4,r1,r2, color=colorlist_2[int(i)],alpha=0.5) # 子图4
plt.show()



