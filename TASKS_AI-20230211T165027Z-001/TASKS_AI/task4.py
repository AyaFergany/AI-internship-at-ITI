import numpy as np
array2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
z = array2d[0:2,:]
print(z)
x = array2d[:,1]
print(x)
y = array2d[2,1]
print(y)
v = array2d[1:3,1:4]
print(v)