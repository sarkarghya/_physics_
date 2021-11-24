import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.optimize import fsolve
import numpy as np
from math import sqrt

cr = 0.02
nsw = 0.95
cdap = 0.04

eta = 0.5


x_data = []
y_data = []
fig, ax = plt.subplots()
line, = ax.plot(0, 0)

def animation_frame(i):
    x = i
    def f(vars):
        z = vars
        eq = 1/(1+(1/((2*eta/(z + sqrt(z**2 + x/nsw)))-1))) -  cr -(z**2/x)*cdap 
        return eq
    t = fsolve(f, 1)

    x_data.append(i)
    y_data.append(1/(1-t[0]))


    plt.xlim(0, 0.4)
    plt.ylim(0, 4)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line, 


animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 4, 0.1), interval=0.4)
