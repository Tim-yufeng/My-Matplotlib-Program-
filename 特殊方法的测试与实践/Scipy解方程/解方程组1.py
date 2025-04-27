from scipy.optimize import fsolve
from math import log
P_a=94.6*101325/76
P_b=29.1*101325/76
dH_a=30.8*10**3
dH_b=33.2*10**3
# 定义方程组
def func(x):
    return [log(x[0]/P_a)*dH_a-log(x[1]/P_b)*dH_b,x[0]+x[1]-101325]

# 解方程组
solution = fsolve(func, [1, 1])
Pab=solution[0]
Pbb=solution[1]
print(Pab)
print(Pbb)