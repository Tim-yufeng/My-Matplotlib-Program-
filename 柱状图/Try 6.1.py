import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
categories=['A','B','C','D','E']
data=[100,200,400,350,600]
ax.barh(categories,data,height=0.8, align='center')
for i, v in enumerate(data):
    plt.text(v + 1,i, str(v), ha='center')
plt.show()



# plt.text(0,data[0],'A',ha='center')
# plt.legend(['Series 1'])
# x_pos = np.arange(len(categories))

# plt.bar(x_pos, data)

