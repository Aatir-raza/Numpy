#with numpy array
import numpy as np
a =np.arange(10000000)
b=np.arange(10000000,20000000)
import time
start= time.time()
c=a+b
print(time.time()-start)
# with python list 

a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]

c=[]
import time
for i in range(len(a)):
  c.append(a[i]+b[i])
print(time.time()-start)

print(2.2889182567596436/0.02443861961364746)