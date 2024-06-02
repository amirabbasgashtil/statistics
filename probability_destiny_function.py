# Probability Density Function (PDF) for 0 < x < 2
from sympy import integrate, Symbol

def PDF(x):
    return (x/2)

'''
calculating the probability of X which
X is continous with PDF
we have to integrate the PDF and solve the problem
'''
# for calculating probability of 1 < x < 2:
x = Symbol('x') 
res = integrate(PDF(x), (x, 1, 2))
print(res)

"""
    checking the neccessary conditions
"""

# 1. for every x f(x) > 0:
# 2. f(x) should be piecewise continuous.
# 3. 0∫2 f(x)dx=1: