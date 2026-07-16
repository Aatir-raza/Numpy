# create numpy array
import numpy as np
a=np.array([1,2,3])
print(a)
# 2d and 3D
b=np.array([[2,3,4],[3,4,5]])
print(b)

c=np.array([[[2,2,4],[3,4,5],[7,6,7]]])
print(c)
# dtype
d=np.array([1,2,3],dtype=float)
print(d)
# np.arange
g=np.arange(1,11,2)
print(g)
# with reshape
t=np.arange(1,11).reshape(5,2)
print(t)
# np.ones and np.zeros
f=np.ones((4,4))
print(f)
f=np.zeros((5,5))
print(f)