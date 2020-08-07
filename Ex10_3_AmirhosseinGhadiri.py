#Tamrin 3

#1:
from math import *
import numpy as np
import matplotlib.pyplot as plt
"""
x=np.linspace(0,10,100)

y1=np.exp(-x/10)*(np.sin((np.pi)*x))
y2=x*(np.exp(-x/3))

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['y1','y2'])
plt.show()
"""

#2:
theta1=np.linspace(0,2*(np.pi),200)
r1=0.8+np.cos(theta1)
x1=r1*(np.cos(theta1))
y1=r1*(np.sin(theta1))

theta2=np.linspace(0,2*(np.pi),200)
r2=1+np.cos(theta2)
x2=r2*(np.cos(theta2))
y2=r2*(np.sin(theta2))

theta3=np.linspace(0,2*(np.pi),200)
r3=1.2+np.cos(theta3)
x3=r3*(np.cos(theta3))
y3=r3*(np.sin(theta3))

plt.figure
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)

plt.legend(['r=0.8','r=1','r=1.2'])
plt.show()






