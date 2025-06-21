##by using ufunc additional argument
##addition
import numpy as np
x=np.array([1,2234,324,321])
y=np.array([232,354,232,1332])
z=np.add(x,y)
print(z)

#substraction
import numpy as np
x=np.array([1,2234,324,321])
y=np.array([232,354,232,1332])
z=np.subtract(x,y)
print(z)

##multiplication
import numpy as np
x=np.array([1,2234,324,321])
y=np.array([232,354,232,1332])
z=np.multiply(x,y)
print(z)

##division
import numpy as np
x=np.array([1,2234,324,321])
y=np.array([232,354,232,1332])
z=np.divide(x,y)
print(z)

#power() fundtion value from 1st array to power of value of 2nd array to return new array
import numpy as np
x=np.array([1,2,3,4])
y=np.array([3,4,5,8])
z=np.power(x,y)
print(z)

#reminder - mod()     reminder()    return reminder of 1 st array corrosponding to 2nd array and result in new array
import numpy as np
x=np.array([100,20,3989,4090])
y=np.array([3,4,5,8])
z=np.mod(x,y)
print(z)  
##reminder
import numpy as np
x=np.array([100,20,3989,4090])
y=np.array([3,4,5,8])
z=np.remainder(x,y)
print(z)

##quotient and mod(reminder)
#divmod() return both quotient and mod(reminder)
import numpy as np
x=np.array([100,20,3989,4090])
y=np.array([3,4,5,8])
z=np.remainder(x,y)
print(z)

##absolute() and abs() - do same operation but here we should use absolute() to avoid confusion with python in bulit function
##math.abs()
import numpy as np
x=np.array([-100,-20,-3989,-4090])
z=np.absolute(x)
print(z)

