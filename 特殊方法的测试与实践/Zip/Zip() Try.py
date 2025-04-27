import numpy as np
list_1=list(np.linspace(1,5,5).astype(int))
list_2=['yjl','fxc','wlr','lyl','wy']
for i in zip(list_1,list_2):
    print(i)