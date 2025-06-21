##hyperbolic function :ufunc such sinh(),cosh(),tanh() gave value in raidian
## for value in degree sinh value of pi/2
import numpy as np
x=np.sinh(np.pi/2)
print(x)

##now we will find sin value of an array
import numpy as np
x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.cosh(x)
print(y)

##find angles:arcsinh(),arccosh(),arctanh() take values in radian and produce tha corresponding sinh,cosh,tanh

#we will now find the angle of 1.0
import numpy as np
x=np.arcsinh(1.0)
print(x)

##angle of each values in array
import numpy as np
x=np.array([1,-1,.1])
y=np.arcsinh(x)
print(y)
