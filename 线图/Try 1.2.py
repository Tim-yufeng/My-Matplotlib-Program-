import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
x=np.linspace(-3,3,100)
t=x**3
plt.plot(x,t,c='m')
# plt.xticks((-2,-1,0,1,2),['t1','t2','t3','t4','t5'],minor=0,
#            color='blue', fontsize=12, rotation=45)
plt.xlabel('axis x')
plt.ylabel('axis y')
plt.grid(True, which='both',axis='x')
# plt.axis([-3,1.5,-6,6])
plt.title('$y=x^3$',fontdict={'fontsize':18,'color':'r',
                              'fontweight':'bold'},loc='center', pad=20)
ax.minorticks_on()
# ax.set_frame_on(1)
ax.set_axis_off()
plt.show()





