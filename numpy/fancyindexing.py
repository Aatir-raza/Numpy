import numpy as np
a =np.arange(24).reshape(6,4)
print(a)

# for row 
b=a[[0,2,3]]
print(b)
# for column 
c=a[:,[0,2,3]]
print(c)
