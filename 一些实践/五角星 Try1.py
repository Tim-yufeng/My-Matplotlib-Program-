import matplotlib.pyplot as plt
import numpy as np
# a=1
# b=((np.sqrt(5)-1)/4+a)/np.sin(0.4*np.pi)
fig,ax=plt.subplots()
# ax.set_xlim(-2,2)
# ax.set_ylim(-2,2)
# ax.set_aspect('equal')
# x_1=np.linspace(-np.cos(0.3*np.pi)*b,np.cos(0.3*np.pi)*b,20)
# y_1=-np.tan(0.4*np.pi)*np.abs(x_1)+b
# ax.plot(x_1,y_1,c='m')
# ax.plot([-np.cos(0.3*np.pi)*b,np.cos(0.1*np.pi)*b],[-np.sin(0.3*np.pi)*b,np.sin(0.1*np.pi)*b],c='m')
# ax.plot([np.cos(0.3*np.pi)*b,-np.cos(0.1*np.pi)*b],[-np.sin(0.3*np.pi)*b,np.sin(0.1*np.pi)*b],c='m')
# ax.plot([-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b],[np.sin(0.1*np.pi)*b,np.sin(0.1*np.pi)*b],c='m')
# plt.show()

a = 0.5
b = ((np.sqrt(5) - 1) / 4 + a) / np.sin(0.4 * np.pi)

x_1_1=np.linspace(-np.cos(0.3*np.pi)*b,np.cos(0.3*np.pi)*b,20)
x_2_1=np.linspace(-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b,20)
x_1_1+=5.5
x_2_1+=5.5

y_1_1=-np.tan(0.4*np.pi)*np.abs(x_1_1)+b
y_1_2=-np.tan(0.2*np.pi)*np.abs(x_1_1)-b*np.cos(0.4*np.pi)
y_2_2=np.tan(0.2*np.pi)*np.abs(x_2_1)-b*np.cos(0.4*np.pi)
y_2_1=b*np.cos(0.4*np.pi)
# y_1_1+=6
# y_1_2+=6
# y_2_1+=6
# y_2_2+=6

ax.plot(x_1_1,y_1_1,c='r')

ax.plot(x_1_1,y_1_2,c='r')
ax.fill_between(x_1_1,y_1_1,y_1_2,color='r')


ax.plot([-np.cos(0.1*np.pi)*b,np.cos(0.1*np.pi)*b],[y_2_1,y_2_1],c='r')
ax.plot(x_2_1,y_2_2,c='r')
ax.fill_between(x_2_1,y_2_1,y_2_2,color='r')
plt.show()