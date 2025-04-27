import math
from scipy.optimize import fsolve
import numpy as np

x=float(input('x坐标：'))
y=float(input('y坐标：'))
z=float(input('z坐标：'))
H=100
h1=26
h2=67
def equation_1(x_1):
    return (y-h1-h2*np.cos(x_1))/(math.sqrt(x**2+(z+H)**2)+h2*np.sin(x_1))-np.tan(x_1)
def equation_2(x_2):
    return (abs(y-h1)+h2*np.cos(x_2))/(math.sqrt(x**2+(z+H)**2)-h2*np.sin(x_2))-np.tan(x_2)
# 初始猜测值
initial_guess = 0
def equation_3(y_1):
    return np.tan(y_1)-x/(z+H)
# 求解方程
if y>(h1+h2):
    x_1 = fsolve(equation_1, initial_guess)
else:
    x_1= -fsolve(equation_2, initial_guess)
# x_1 = fsolve(equation_1, initial_guess)

x_2 = fsolve(equation_3, initial_guess)
# print(solution)
print(math.degrees(x_1[0]),math.degrees(x_2[0]))





