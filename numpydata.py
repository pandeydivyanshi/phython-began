##checking data type
#i for integer
#b for boolean
#u for unsign integer
#c for complex float
#f for float
#m for time delta
#M for datetime
#O for object
#S for string
#U for unicode string
# V memory
import numpy as np
x=np.array([1,2,3,4,5])
print(x.dtype)                                       ##it also give bites value

#for string
import numpy as np
a=np.array(["divya","div","arti","syama","dev"])
print(a.dtype)      

#CREATING array eith defined datatypye
import numpy as np
x=np.array([1,2,3,4,5],'S')
print(x)
print(x.dtype)                                       ##it also give bites value

#creating array with 4 byte
import numpy as np
x=np.array([1,2,3,4,5],dtype='i4')
print(x)
print(x.dtype)                                       ##it also give bites value

##if a type in which the element cannot be casted then numpy raise error 
# import numpy as np
# x=np.array([1,'a','b'],'i')            # this raise error
# print(x)
# print(x.dtype)      

#converting data type into existing array astpe() create copy of array
import numpy as np
x=np.array([1.44,2.66,3.75,4.24,5.444])
y=x.astype('i')                                              ##this copy and make it into integer         
print(y)
print(x)
print(x.dtype)                                       ##it also give bites value
print(y.dtype)
