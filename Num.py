# basics of numpy
import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2,3],[4,1,6]],dtype='int16')
print(b)
print(a)
#seeing the dimension
print(a.ndim)
print(b.ndim)
#seeing the size..will give the number of element
print(a.size)
print(b.size)
#shape of the arrap(3*2 or something)
print(a.shape)
print(b.shape)
#data type of an array
print(a.dtype)
print(b.dtype)
#