import numpy as np
array1 = np.random.randn(5)
print(array1)
print(array1.sort())
print(array1)
z = np.sort(array1)[::-1]
print(z)
array2 = np.random.randn(4,5)
print(array2)
print(array2.sort(1))
print(array2)
print(array2.sort(0))
print(array2)
array3 = np.array(['aya', 'noha','aya','noha' ,'sara'])
print(array3)
x = np.unique(array3)
print(x)
