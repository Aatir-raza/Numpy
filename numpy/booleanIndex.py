import numpy as np
a= np.random.randint(1,100,24).reshape(6,4)
print(a)
 # find numbers greater than 50

b=a%2
print(b)
# find out even number
c=a%2==0
print(c)

# find all number greater than 50 and are given
a=[(a>50)] & (a%2==0)
print(a)

# find all number not divisible by 7 
d=a[~(a%7==0)]
print(d)

