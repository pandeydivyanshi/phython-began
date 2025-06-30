##create your ufunc , you have to define a function ,like you do in normal function in python ,then you add it to numpy with frompyfunc() method.
## arguments of formfunc ():function,inputs,outputs
##create your own ufunc for addition
import numpy as np
def myadd(x,y):
    return x+y

myadd= np.frompyfunc(myadd,2,1)           ##2 imply 2D array input and 1 imply 1D array output
print(myadd([1,2,3,4],[5,6,7,8]))

#checking this function is ufunc or not
import numpy as np
print(type(np.add))

##concatenate
import numpy as np
print(type(np.concatenate))

##what if ufunc does not exist
# import numpy as np
# print(type(np.divyanshi))               ## get error

##checking ufunc by if statment
import numpy as np
if type(np.add) == np.ufunc:
    print("fnc is ufunc")
else:
    print("func is not ufunc")
