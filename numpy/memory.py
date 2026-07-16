a=[i for i in range (10000000)]
import sys
sys.getsizeof(a)
print (a)


import numpy as np
a= np.arange(10000000)
sys.getsizeof(a)
print(a)
