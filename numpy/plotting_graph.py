# graph of x=y
import numpy as np
import matplotlib .pyplot as plt
x=np.linspace(-10,10,100)
y=x
plt.plot(x,y)
plt.show()

# graph of y=xsquare
import numpy as np
import matplotlib .pyplot as plt
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()

# y=sin(x)
import numpy as np
import matplotlib .pyplot as plt
x=np.linspace(-10,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()

# y=xlog(x)
import numpy as np
import matplotlib .pyplot as plt
x=np.linspace(-10,10,100)
y=x*np.log(x)
plt.plot(x,y)
plt.show()

# sigmoid
import numpy as np
import matplotlib .pyplot as plt
x=np.linspace(-10,10,100)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()












