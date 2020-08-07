import numpy as np
import matplotlib as plt

#Tamrin 2

vec1=np.array([-1., 4., -9.])
mat1=np.array([[1., 3., 5.], [7., -9., 2.], [4., 6., 8.]])

#1:
vec2=(np.pi/4) * vec1
print(vec2)
#vec2=array([-0.78539816,  3.14159265, -7.06858347])

#2:
vec2=np.cos(vec2)
print(vec2)
#vec2=array([[ 0.70710678, -1.         , 0.70710678]])

#3:
vec3=vec1 + 2*vec2
print(vec3)
#vec2=array([[ 0.41421356,  2.         ,-7.58578644]])

#4:Skip

"""#5:
vec4=np.multiplication(mat1,vec3)
"""
#6:
print(np.transpose(mat1))
"""[[ 1.  7.  4.]
   [ 3. -9.  6.]
   [ 5.  2.  8.]]"""

#7:
print(np.linalg.det(mat1))
#result:161.99999999999994

#8:
print(np.trace(mat1))
#result:0.0

#9:
print(np.min(vec1))
#result:-9.0

#10:
print(np.argmin(vec1))
#result:2

#11:
print(np.min(mat1))
#result:-9.0

#12:
A=np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])

A1=np.sum(A[:,0])
A2=np.sum(A[:,1])
A3=np.sum(A[:,2])
A4=np.sum(A[:,3])
A5=np.sum(A[:,4])
SUM1=np.array([A1,A2,A3,A4,A5])

a1=np.sum(A[0,:])
a2=np.sum(A[1,:])
a3=np.sum(A[2,:])
a4=np.sum(A[3,:])
a5=np.sum(A[4,:])
sum1=np.array([[a1],[a2],[a3],[a4],[a5]])

print(np.min(SUM1))#result=65
print(np.max(SUM1))#result=65

print(np.min(sum1))#result=65
print(np.max(sum1))#result=65

print(np.sum(np.diag(A)))#result=65
print(np.sum(np.fliplr(A)))#result=325 WHY???????
#So matrix A is magic square.

#13:
M=np.random.rand(10,10)
print(M)

#14:#I don't understand the question.




























