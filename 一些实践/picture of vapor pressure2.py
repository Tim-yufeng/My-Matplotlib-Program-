import matplotlib.pyplot as plt
import numpy as np
from math import log
from scipy.optimize import fsolve
P_a=94.6*101325/760
P_b=29.1*101325/760
dH_a=30.8*10**3
dH_b=33.2*10**3

k=np.arange(0,1,0.01)
def vap1(k):
    p = []

    for x in k:
        X_a = x * P_a / (x * P_a + (1 - x) * P_b)
        X_b = x * P_b / (x * P_a + (1 - x) * P_b)  # 气体分数比

        # P1 = x * P_a + (1 - x) * P_b
        # P2 = X_a * P_a + X_b * P_b

        # dH = x * dH_a + (1 - x) * dH_b
        # np.ln(101325/P1)=(dH/8.314)*(1/298-1/y)
        def func(m):
            return np.array([log(m[0] / P_a) * dH_a - log(m[1] / P_b) * dH_b, m[0] * x + m[1] * (1 - x) - 101325])

        # 解方程组
        solution = fsolve(func, [1, 1])
        P_ab = solution[0]
        P_bb = solution[1]
        t1 = log(P_ab / P_a)
        t2 = log(P_bb / P_b)
        y = 1 / (1 / 298.15 - 8.314 / dH_a * t1) - 273.15
        y = 1 / (1 / 298.15 - 8.314 / dH_b * t1) - 273.15
        p.append(y)
    return p
def vap2(k):
    q = []

    for x in k:
        X_a = x * P_a / (x * P_a + (1 - x) * P_b)
        X_b = x * P_b / (x * P_a + (1 - x) * P_b)  # 气体分数比

        # P1 = x * P_a + (1 - x) * P_b
        # P2 = X_a * P_a + X_b * P_b

        # dH = x * dH_a + (1 - x) * dH_b
        # np.ln(101325/P1)=(dH/8.314)*(1/298-1/y)
        def func(m):
            return np.array([log(m[0] / P_a) * dH_a - log(m[1] / P_b) * dH_b, m[0] * x + m[1] * (1 - x) - 101325])

        # 解方程组
        solution = fsolve(func, [1, 1])
        P_ab = solution[0]
        P_bb = solution[1]
        t1 = log(P_ab / P_a)
        t2 = log(P_bb / P_b)
        y = 1 / (1 / 298.15 - 8.314 / dH_a * t1) - 273.15
        y = 1 / (1 / 298.15 - 8.314 / dH_b * t1) - 273.15
        q.append(X_a)
    return q
plt.plot(k,vap1(k),c='b',lw=1,label='Boiling point')
plt.plot(vap2(k),vap1(k),c='m',lw=1,label='Mole fraction in vapor,x_benzene(g)')

x0=0
x1=1
y0=vap1([x0])[0]
y1=vap1([x1])[0]
plt.scatter(x0,y0,s=50,color='b')
plt.scatter(x1,y1,s=50,color='b')
plt.plot([x0,x0],[y0,y1],'k--',lw=2)
plt.plot([x0,0],[y0,y0],'k--',lw=2)
plt.plot([x1,x1],[y1,y1],'k--',lw=2)
plt.plot([x1,1],[y1,y1],'k--',lw=2)
new_ticks=np.linspace(80,130,9)
plt.yticks(new_ticks)

plt.xlabel('Mole fraction in liquid,x_benzene(l)')
plt.ylabel('Temperature/degrees')
plt.legend()
plt.show()