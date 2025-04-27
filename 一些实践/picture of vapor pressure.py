import matplotlib.pyplot as plt
import numpy as np
from math import log
from scipy.optimize import fsolve
# from scipy.optimize import root
# P_a=94.6*101325/760
# P_b=29.1*101325/760
# dH_a=30.8*10**3
# dH_b=33.2*10**3
#
# k=np.arange(0,1,0.01)
# p=[]
# q=[]
# for x in k:
#     X_a = x * P_a / (x * P_a + (1 - x) * P_b)
#     X_b = x * P_b / (x * P_a + (1 - x) * P_b)  # 气体分数比
#     # P1 = x * P_a + (1 - x) * P_b
#     # P2 = X_a * P_a + X_b * P_b
#
#     # dH = x * dH_a + (1 - x) * dH_b
#     # np.ln(101325/P1)=(dH/8.314)*(1/298-1/y)
#     def func(m):
#         return np.array([log(m[0] / P_a) * dH_a - log(m[1] / P_b) * dH_b, m[0]*x + m[1]*(1-x) - 101325])
#
#
#     # 解方程组
#     solution = fsolve(func, [1, 1])
#     P_ab = solution[0]
#     P_bb = solution[1]
#     t1 = log(P_ab/P_a)
#     t2= log(P_bb/P_b)
#     y = 1 / (1 / 298 - 8.314 / dH_a * t1)-273.15
#     y=1 / (1 / 298 - 8.314 / dH_b * t1)-273.15
#     p.append(y)
#     q.append(X_a)
# plt.plot(k,p,c='b',lw=1)
# plt.plot(q,p,c='m',lw=1)
# plt.show()
#
# ########################################
#

# x=np.linspace(0,1,100)
# x_list=x.tolist()
# y_list=[]
# T2_list=[]
# for x in x_list:
#     def fun(P_1_and_2):
#         P1, P2 = P_1_and_2
#         return np.array([(8.314 / dH_a) * np.log(np.abs(P1 / 94.6)) - (8.314 / dH_b) * np.log(np.abs(P2 / 29.1)),
#                          x * P1 + (1 - x) * P2 - 760])
#     initial_guess = [10,10]
#     solution = fsolve(fun, initial_guess)
#     P1, P2 = solution
#     T=1/(1/298.15-8.314*np.log(abs(P1/94.6))/dH_a)-273.15
#     T2_list.append(T)
#     y = x*P1 / (x*P1 + (1-x)*P2)
#     y_list.append(y)
# plt.plot(x_list, T2_list, color='r',label='Boiling point')
# plt.plot(y_list, T2_list, color='g',label='Mole fraction in vapor,x_benzene(g)')
# plt.legend()
# plt.show()

###################################


# plt.plot([0,0],[0,121.017],linestyle='--',c='k')
# plt.plot([0,0],[121.017,121.017],linestyle='--',c='k')
# plt.plot([1,1],[0,85.072],linestyle='--',c='k')
# plt.plot([0,1],[85.072,85.072],linestyle='--',c='k')
    # if solution.success:
    #     P1, T2 = solution.x
    #     T2 -= 273.15
    #     P2 = (760 - x_val * P1) / (1.0001 - x_val)
    #     y = P1 / (P1 + P2)
    #     y_list.append(y)
    #     T2_list.append(T2)
    # else:
    #     print(f"No solution found for x = {x_val}")
# x_list = x_list[:len(T2_list)]

# ##################################
P_a=94.6
P_b=29.1
dH_a=30.8*10**3
dH_b=33.2*10**3
x = np.linspace(0, 1, 100)
x_list = x.tolist()
y_list = []
T2_list = []
for x in x_list:
    def fun(P_and_T):
        P1, T = P_and_T
        # 计算两个方程的值并合并为一个数组
        return np.array([(8.314 / dH_b) * np.log(np.abs((760 - x * P1) / ((1.0001 - x) * 29.1))) - 1 / 298.15 + 1 / T,
                         (8.314 / dH_a) * np.log(np.abs(P1 / 94.6)) - 1 / 298.15 + 1 / T])
    initial_guess = [300, 110]
    solution = fsolve(fun, initial_guess)
    P1, T2 = solution
    T2 -= 273.15
    P2 = (760 - x * P1) / (1.0001 - x)
    y = P1 / (P1 + P2)
    y_list.append(y)
    T2_list.append(T2)
plt.plot(x_list, T2_list, color='r')
plt.plot(y_list, T2_list, color='g')
plt.show()
    # try:
    #     solution = fsolve(fun, initial_guess)
    #     P1, T2 = solution
    #     T2 -= 273.15
    #     P2 = (760 - x * P1) / (1.0001 - x)
    #     y = P1 / (P1 + P2)
    #     y_list.append(y)
    #     T2_list.append(T2)
    # except Exception as e:
    #     print(f"No solution found for x = {x}: {e}")
#
# # 由于我们已经确保了每次循环都成功添加了元素，所以不需要截取x_list
# plt.plot(x_list[:len(T2_list)], T2_list, color='r')

############################
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# def funn():
#     P1=0
#     T=0
#     for x in np.arange(0, 1, 0.01):
#         for P1 in np.arange(0, 760, 0.1):
#             for T in np.arange(70, 130, 0.01):
#                 if (8.314 / dH_b) * np.log(np.abs((760 - x * P1) / ((1 - x) * 29.1))) - 1 / 298.15 + 1 / T == 0 and (
#                         8.314 / dH_a) * np.log(np.abs(P1 / 94.6)) - 1 / 298.15 + 1 / T == 0:
#                     P1=P1
#                     T=T
#                     P2 = (760 - x * P1) / (1 - x + 1e-10)  # 添加1e-10避免除以零
#                     y = P1 / (P1 + P2)
#                     plt.scatter(x, T, color='r')
#                     plt.scatter(P1,T, color='g')  # 在图上标记T2的值
#                 else: continue





# initial_guess = [100, 100]
# solution = fsolve(fun, initial_guess)
# funn()

# plt.show()
