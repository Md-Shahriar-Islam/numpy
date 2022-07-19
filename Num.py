import numpy as np
#task1
a=np.ones((5,5))
a[1:4:1,1:4:1]=0
a[2,2]=9
b=np.identity(3)
c=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
d=c[2:4,0:2].copy()
#printing random number using numpy
e=[x for x in range(0,101,2)]
print(e)

print(d)