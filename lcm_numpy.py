##LCM : lowest common difference
##lcm of 2 numbers
import numpy as np
x=6
y=4
z=np.lcm(x,y)
print(z)

##lcm of array
import numpy as np
x=np.array([4,9,5,8])
y=np.lcm.reduce(x)        #reduce() ufunc ,lcm() fnc on each element and it will reduce by 1D
print(y)

##lcm of all of an array where the array contain all integer from 1 to 10
import numpy as np
x=np.arange(1,11)
y=np.lcm.reduce(x)
print(y) 