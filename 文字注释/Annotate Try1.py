import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
y=x**2-2*x-3
plt.plot(x,y,c='r')
plt.scatter(1,-4,c='b',s=10)
plt.annotate('minimum point',xy=(1,-4),xytext=(-5.5,10),
             arrowprops={'arrowstyle':'->','color':'blue'})
plt.show()

