import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
plt.ion()
x=np.arange(-2,2,0.01)
for a in np.arange(1,20,0.1):
    y = np.real((x**2)**(1 / 3) + np.exp(1) / 3 * np.sqrt(np.abs(np.pi - x**2))*np.sin(a*np.pi*x))
    ax.clear()
    ax.plot(x, y, c='r')
    plt.pause(0.1)

plt.ioff()
ax.set_title('Happy 520!',c='purple',loc='center')
plt.show()