import numpy as np
import matplotlib.pyplot as plt

#TAMRIN 1

#1:
x=8

#2:
pow(x,2)

#3:
theta=(np.pi)/3

#4:
y1=np.sin(theta)
y2=np.cos(theta)
print(y1)
print(y2)
#According to the result, radian is being used.

#5:
meshpoints=np.linspace(-1,1,500)
print(meshpoints)

#6:
print(meshpoints[53])
#The result will be -0.7875751503006012.

#7:
plt.plot(meshpoints,np.sin(2*(np.pi)*meshpoints))
plt.show()





