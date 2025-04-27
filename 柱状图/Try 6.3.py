import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()

speeds = [39.6,28.6,42.2,35.4,30.7,28.7,30.6,29.4,31.0,28.5,35.6,37.0,36.5,24.7,27.1,
          31.7,27.4,34.5,36.0,28.9,27.6,25.9,39.4,37.0,27.8,43.9,38.6,33.1,30.7,31.1,
          35.2,39.6,38.9,29.7,37.5,26.3,27.0,25.2,33.2,28.2,34.3,40.8,26.4,36.1,43.1,
          35.8,26.5,29.1,37.7,42.2,27.2,35.7,28.9,32,27.3,27.6,30.0,29.6,29.7,28.5]
ax.boxplot(speeds,notch=True, vert=True, patch_artist=True)
plt.show()


# plt.hist(np.array(speeds),bins=15,color='r',histtype='step',cumulative=0)
# plt.step(np.linspace(1,15,60),speeds)
# notch=True, vert=True, patch_artist=True
# ,histtype='bar',cumulative=1,density=1