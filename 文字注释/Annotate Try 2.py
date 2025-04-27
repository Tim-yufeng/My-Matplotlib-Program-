import matplotlib.pyplot as plt
import numpy as np
theta=360/11
plt.xlim(-0.75,0.75)
plt.ylim(-0.75,0.75)
r1=0.5
r2=0.1
plt.scatter(0,0,s=15,c='g')
plt.text(0,0,'(0,0)')
arrow_types_list=['-','->','<-','<->','-[',']-','-|>','<|-|>','fancy','simple','wedge']
for i in range(11):
    plt.annotate(f'{arrow_types_list[i]}',xy=(r2*np.cos(theta*i),r2*np.sin(theta*i)),xytext=
    (r1*np.cos(theta*i),r1*np.sin(theta*i)),arrowprops={'arrowstyle':arrow_types_list[i],'color':'blue'})
# plt.axis('equal')
plt.show()