##reshaping-means changing shape of array like adding or remving the elements
#1D to 2D
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(4,3)
print(y)

#1D to 3D
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(2,3,2)
print(y)

##checking reshaping is copy or view
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
print(x.reshape(2,4).base)                              ##it gave orignal array imply reshape is veiw array

##unkown dimension-only allow one unkwon dimension for reshaping
##let pass -1
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=x.reshape(2,2, -1)
print(y)

#flattering the array by converting multidimensional array to 1D
import numpy as np
x=np.array([[1,2,3,4],[5,6,7,8]])
y=x.reshape(-1)                                    #by default it gave 1D array
print(y)

## other fnc for changing shape,flatten,ravel and also rearranging element rot90,flip,flipir,flipud