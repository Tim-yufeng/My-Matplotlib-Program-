import numpy as np
from scipy.optimize import fsolve
def func(x):
    return x**2 +2*x-3
solutions=fsolve(func,-1.001)
print(solutions)