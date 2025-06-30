##summation is adding all element of array , add is adding two array
import numpy as np 
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.add(x,y)
print(z)

import numpy as np 
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.sum([x,y])                            ##gave single number 1+2+3+4+5+6=21
print(z)

#summation over axis : if you specify axis = 1,numpy will sum number in each array
import numpy as np 
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.sum([x,y],axis=1)                            
print(z)

##cumulative  sum : means partially adding the element in array
# example :[1,2,3,4] would be [1,1+2,1+2+3,1+2+3+4] =[1,3,6,10]
##represented by cumsum()
x=np.array([1,2,3,4])
z=np.cumsum(x)
print(z) 