import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(0,np.pi*2,100)
r1=1-np.sin(theta)
r2=0
plt.polar(theta,r1,c='r')
plt.fill_between(theta,r1,r2,color='r')
plt.show()
import numpy as np



# plt.show()

# plt.polar(theta,r1,c='r')
# plt.fill_between(theta,r1,r2,color='r')