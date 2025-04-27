import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.00001,5,100)
y1=np.log(x)
y2=np.exp(x)
y3=np.sin(x)
y4=np.cos(x)
y_list=[y1,y2,y3,y4]
color=['r','m','purple','b']
for i in range(1,5):
    plt.subplot(2,2,i).plot(x,y_list[i-1],c=color[i-1])
plt.show()
# axe1=plt.subplot(2,2,1)
# axe2=plt.subplot(2,2,2)
# axe3=plt.subplot(2,2,3)
# axe4=plt.subplot(2,2,4)
# x=np.linspace(0.00001,5,100)
# y1=np.log(x)
# y2=np.exp(x)
# y3=np.sin(x)
# y4=np.cos(x)
# axe1.plot(x,y1,c='r')
# axe2.plot(x,y2,c='m')
# axe3.plot(x,y3,c='purple')
# axe4.plot(x,y4,c='b')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
fig1,axes=plt.subplots(2,2,sharex=False,sharey=False)
x=np.linspace(0.00001,5,100)
y1=np.log(x)
y2=np.exp(x)
y3=np.sin(x)
y4=np.cos(x)
axes[0,0].plot(x,y1,c='r')
axes[0,1].plot(x,y2,c='m')
axes[1,0].plot(x,y3,c='purple')
axes[1,1].plot(x,y4,c='b')
# plt.show()
fig2,axes=plt.subplots(2,2,sharex=True,sharey=True)
y_list=[y1,y2,y3,y4]
color_list=['r','m','purple','b']
for i in range(4):
    axes.flatten()[i].plot(x,y_list[i],color_list[i])
plt.show()
#

