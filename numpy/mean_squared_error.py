import numpy as np
actual=np.random.randint(1)
predicted=np.random.randint(1,50,25)
print(actual-predicted)
 
def mse(actual,predicted):
  return np.mean((actual-predicted)**2)
mse(actual,predicted)
 