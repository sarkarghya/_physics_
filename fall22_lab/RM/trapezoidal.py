import numpy as np
import matplotlib.pyplot as plt

# METHOD1: define trapezoidal function by yourself
def trapezoidal1(f, a, b, n):
    '''return integral result using trapezoidal rule''' 
    '''integral from a to b of a function f(x)'''
    '''the interval (b-a) is broken into n segments'''
    h = float(b-a)/n
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return h*s
    
def f(x):
    return x**2

s1 = trapezoidal1(f, 5, 10, 100)    
print('The integral of y=x^2 using trapezoidal rule is:', s1)

# METHOD2: use numpy.trapz() under numpy modeule

# generate training data
# replace x, y data sets with your (force, position) measurements 
x = np.arange(5, 10, 0.05)
y = x**2
'''numpy.trapz(y, x=None, dx=1.0, axis=-1)'''
'''integrate along the given axis using the composite trapezoidal rule'''
'''integrate y(x) along given axis'''
s2 = np.trapz(y,x)
print('The integral of y=x^2 using trapezoidal rule is:', s2)

