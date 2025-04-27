import numpy as np
import matplotlib.pyplot as plt
ax=plt.subplot(projection='3d')
z=np.linspace(0,50,500)
x=np.sin(z)
y=np.cos(z)
ax.plot(x,y,z)
plt.show()

