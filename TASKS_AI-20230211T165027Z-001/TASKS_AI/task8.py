import numpy as np
array1 = np.random.randn(4,5)
print(array1)
print(array1.mean())
print(array1.min())
print(array1.max())
print(array1.std())
print(array1.cumsum())
array2 = np.array([77,46,85,22,28,89,63,43,4,76])
print(array2)
print(array2.min())
print(array2.argmin())
print(array2.argmax())
print(array1)
z = array1.sum(axis = 0)
print(z)
x = array1.sum(axis = 1)
print(x)
array3 = np.array([True, False, False,False,True,True])
print(array3.sum())
print(array3.any())
print(array3.all())
array4 = np.array([True, True, True, True])
print(array4.all())