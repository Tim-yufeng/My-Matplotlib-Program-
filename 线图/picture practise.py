import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
x=np.linspace(-5,5,50)
# plt.xticks([-3.5,-2.5,-1.5,-0.5,0,0.5,1.5,2.5,3.5])
fig=plt.figure()
y=x**2
x0=2
y0=x0**2
g=2*x0*(x-x0)+y0
plt.scatter(x0,y0,s=50,color='blue')
plt.plot([x0,x0],[y0,0],'k--',lw=2)
plt.plot([x0,0],[y0,y0],'k--',lw=2)
plt.plot(x,y,label='the function')
plt.plot(x,g,label='the tangent')
plt.legend(loc='best')
ax=plt.gca()
# l1=plt.axhline(0)
# l2=plt.axvline(0)
# ax.xaxis.set_ticks_position('l1')
# ax.yaxis.set_ticks_position('l2')
axx = fig.add_axes([0.5, 0.5, 0.8, 0.8])
rect = axx.patch
rect.set_alpha(0)
plt.xticks(())
plt.yticks(())
for spine in ax.spines.values():
    spine.set_lw(5)
    spine.set_color('purple')
plt.show()