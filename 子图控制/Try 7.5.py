import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.00001,5,100)
y1=np.log(x)
y2=np.exp(x)
y3=np.sin(x)
y4=np.cos(x)
fig=plt.figure()
fig.add_axes([0,0.5,0.5,0.5]).plot(x,y1)
fig.add_axes([0.5,0.5,0.5,0.5]).plot(x,y2)
fig.add_axes([0.5,0,0.5,0.5]).plot(x,y3)
fig.add_axes([0,0,0.5,0.5]).plot(x,y4)
plt.show()


