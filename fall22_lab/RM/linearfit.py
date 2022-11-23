import numpy as np
import matplotlib.pyplot as plt
import csv


def LineFit(x, y):
    '''Returns slope and y-intercept of linear fit to (x,y) data set'''
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    yint = y.mean()-slope*xavg
    return slope, yint
                
# generate training data
# replace this part with your (velocity^2 , position) data set
with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

x = [x[0] for x in data]
y = [x[1]**2 for x in data]

# compute coefficients for simple linear regression
# using predefined LineFit() function
slope, yint = LineFit(x, y)

# plot
x2 = np.array([0, 10])
y2 = slope * x2 + yint

plt.figure(1, figsize = (10,8))
plt.scatter(x, y, color='b', s=20)
plt.plot(x2, y2, color='r', linewidth=3)

plt.axis([0,10,-5,30])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression\n')

plt.savefig("simple_lin_regression.png")
plt.show()

