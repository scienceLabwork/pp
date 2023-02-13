# #LAB PP Q2
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,2,0.1)

def mean(x):
    return sum(x)/len(x)

def std(x):
    m = mean(x)
    return (sum([(i-m)**2 for i in x])/len(x))**0.5

mu = x.mean()
sigma = x.std()

y = []
for i in range(len(x)):
    fofx = 1.0/(2.0*math.pi*sigma**2)**0.5*math.exp(-0.5*(x[i]-mu)**2/sigma**2)
    y.append(fofx)
    print(fofx)

plt.scatter(x, y)
plt.show()