import numpy as np
import matplotlib.pyplot as plt
x=range(0,6)
y=range(0,6)
x, y = np.meshgrid(x, y)
print(x)
print(y)
ax=plt.subplot()
ax.set_aspect('equal')
ax.xaxis.set_ticks_position('top')
plt.xticks(np.linspace(0,5,6))
plt.yticks(list(np.linspace(0,5,6)))
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_color('None')
for i in range(0,6):
    for j in range(0,6):
        if i!=j:
            plt.text(i,j,'({},{})'.format(i,j),color='b')
            plt.text(j,i,'({},{})'.format(j,i),color='b')
        else:
            plt.text(i,j,'({},{})'.format(i,j),color='b')
ax.grid(True)
plt.show()




# ax1=plt.subplot(211)
# ax2=plt.subplot(212)
# ax1.grid(True)
# ax2.grid(1)
# ax1.spines['bottom'].set_position(('data', 0))
# ax1.spines['left'].set_position(('data',0))
# ax1.spines['top'].set_color('None')
# ax1.spines['right'].set_color('None')
# plt.show()


# for i in range(0,6):
#     ax.spines['top'].set_position(('data', i))
# for i in range(0,6):
#     ax.spines['left'].set_position((i,'data'))
# # ax.spines['top'].set_position(('data',3))

# x=[1,2,3]
# y=[4,5,6]
# x,y=np.meshgrid(x,y)
# print(x)
# print(y)
# print(x[1,2])
# print(x[2,1])
# x=np.linspace(0,10,11)
# y=np.linspace(0,10,11)
# x,y=np.meshgrid(x,y)
# x_i=int(input('x坐标是'))
# y_j=int(input('y坐标是'))
# # print('({},{})'.format(x[10-y_j,x_i],y[x_i,y_j]))
# print(f'({x[10-y_j,x_i]},{y[y_j,x_i]})')
# print(y[x_i,y_j])