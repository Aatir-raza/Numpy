#numpy.concentenate ()function concentenate a sequence of array along an existing axis 
import numpy as np
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)
print(a,b)
c=np.concatenate((a,b),axis=1)
print (c)

# np.unique 
# with the help of np .unique()method we can get the unique values from an array given as parameter in np,unique() method 
d=np.array([1,1,2,2,3,3,4,5,5,6,6,7,7])
e=np.unique(d)
print(e)