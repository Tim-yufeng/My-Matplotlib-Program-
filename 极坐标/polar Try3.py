import matplotlib.pyplot as plt
import numpy as np
thu_color=(0.42,0.21,0.63)
nju_color=(0.41,0.17,0.50)
pku_color=(0.45,0,0)
sjtu_color=(0.7,0,0)
ustc_color=(0.12,0.36,0.48)
zju_color=(0.2,0.3,0.5)
hit_color=(0.64,0.64,0.68)
fdu_color=(0.24,0.36,0.57)
xjtu_color=(0.7,0,0)   # c9高校颜色一览
theta=np.linspace(0,np.pi*2,100)
r1=1-np.sin(theta)
r2=0
ax1=plt.subplot(111,projection='polar')
label_list=['THU','PKU','SJTU','ZJU','NJU','FDU','HIT','USTC','XJTU']
colorlist_2=[thu_color,pku_color,sjtu_color,zju_color,nju_color,
             fdu_color,hit_color,ustc_color,xjtu_color]
for i in np.linspace(0,8,9):
    ax1.plot(theta, r1*(i+1), c=colorlist_2[int(i)],alpha=1,label=label_list[int(i)])
    ax1.fill_between(theta,r1*i,r1*(i+1), color=colorlist_2[int(i)],alpha=1)
ax1.set_thetagrids(np.degrees(np.linspace(0, 2*np.pi, 12, endpoint=False)),
                   labels=['JYF','JYF','JYF','90','WLR','WLR','WLR','WLR','WLR','270','JYF','JYF'])
# 获取所有角度标签
labels = ax1.get_xticklabels()
colors = [sjtu_color,sjtu_color,sjtu_color,'k',nju_color,nju_color,nju_color,nju_color,
          nju_color,'k',sjtu_color,sjtu_color]
for label, color in zip(labels, colors):
    label.set_color(color)
labels2 = ax1.get_yticklabels()
for label, color in zip(labels2, colors):
    label.set_color('None')    # 去掉圆周标签
ax1.grid(False)     # 去掉网格
plt.legend(loc='upper center',ncol=2)
plt.show()

