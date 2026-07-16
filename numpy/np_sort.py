# return a sorted copy of an array
import numpy as np
a=np.random.randint (1,100,15)
print(a)
b=np.random.randint(1,100,24).reshape(6,4)
c=np.sort(a)
d=np.sort(b)
e=np.sort(b,axis=0)
print(c,d,e)

# np.append 
# the numpy.append ()append values along the mentioned axis at the end of the array
a=np.append(a,200)
b=np.append(b,np.ones((b.shape[0],1)),axis=1)
print(a,b)


