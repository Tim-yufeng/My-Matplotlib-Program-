import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-5,5,0.01)
function=np.poly1d([1,0,0,0])
plt.plot(x,function(x),c='m',lw=1)
plt.show()
