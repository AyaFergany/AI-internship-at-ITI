import numpy as np
array1 = np.random.randint(50, size = 10)
print(array1)
ind = [1,3,5,7]
z =array1[ind]
print(z)
ind2 = np.array([[1,3],[5,7]])
print(ind2)
l = array1[ind2]
print(l)
array2 = np.random.randint(100, size=(3,4))
print(array2)
ind = ((0,1,2), (3,2,3))
print(ind)
k = array2[ind]
print(k)
row = [0,1,2]
column = [3,2,3]
j = array2[row,column]
print(j)
