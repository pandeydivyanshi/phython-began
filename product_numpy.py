##product use prod()
## it gave product od each element in array
import numpy as np
x=np.array([1,2,3,4,5])                  #1*2*3*4*5
y=np.prod(x)
print(y)

##product of two array
import numpy as np
x=np.array([1,2,3,4,5]) 
z=np.array([6,7,8,9,10]) 
y=np.prod([x,z])                     ##1*2*3*4*5*6*7*8*9*10
print(y)



##product over axis
import numpy as np
x=np.array([1,2,3,4,5]) 
z=np.array([6,7,8,9,10]) 
y=np.prod([x,z],axis=1)                     
print(y)

##cumulative product 
##partial product
import numpy as np
x=np.array([1,2,3,4,5])
y=np.cumulative_prod(x)
print(y)