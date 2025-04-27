import matplotlib.pyplot as plt
import numpy as np
plt.axis([-0.5,1.5,-0.5,1.5])
plt.xticks((0,1))
plt.yticks((0,1))
for i in range(0,2):
    for j in range(0,2):
        plt.text(i,j,f'({i},{j})')
plt.scatter([0,0,1,1],[0,1,0,1],color='m')
plt.annotate('',xy=(0,1),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(1,0),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(1,1),xytext=(0,0), arrowprops = {'arrowstyle':'->'})

plt.grid()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
plt.axis([-0.5,2.5,-0.5,2.5])
plt.xticks((0,1,2))
plt.yticks((0,1,2))
plt.scatter([0,0,0,1,1,1,2,2,2],[0,1,2,0,1,2,0,1,2],color='m')
for i in range(0,3):
    for j in range(0,3):
        plt.text(i,j,f'({i},{j})')
plt.annotate('',xy=(0,1),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(1,0),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(1,1),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(2,1),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.annotate('',xy=(1,2),xytext=(0,0), arrowprops = {'arrowstyle':'->'})
plt.grid()
plt.show()