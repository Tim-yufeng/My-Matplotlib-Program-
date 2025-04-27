import matplotlib.pyplot as plt
import numpy as np
n=12
X=np.arange(n)
Y=10/X
plt.bar(X,Y,facecolor='purple',edgecolor='w')
ax=plt.gca()
for spine in ax.spines.values():
    spine.set_color('none')
plt.xticks(())
plt.yticks(())
plt.show()