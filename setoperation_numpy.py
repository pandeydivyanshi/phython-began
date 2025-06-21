## set collection of unique elements
##creating set use unique()  method to find unqiue elements from any array
##we will convert the array with repated element into set
import numpy as np
x=np.array([1,1,1,2,34,4,55,66,55,3,2,124,5,4])
y=np.unique(x)
print(y)


## to fine from 2 array union
import numpy as np
x=np.array([1,1,1,2,34,4,55,66,55,3,2,124,5,4])
z=np.array([11,13,165,21,342,4,255,266,755,3,2,124,5,4])
y=np.union1d(x,z)
print(y)

##intersection
import numpy as np
x=np.array([1,1,1,2,34,4,55,66,55,3,2,124,5,4])
z=np.array([11,13,165,21,342,4,255,266,755,3,2,124,5,4])
y=np.intersect1d(x,z,assume_unique=True)
print(y)

##value only in 1st array not in 2nd array
import numpy as np
x=np.array([1,1,1,2,34,4,55,66,55,3,2,124,5,4])
z=np.array([11,13,165,21,342,4,255,266,755,3,2,124,5,4])
y=np.setdiff1d(x,z,assume_unique=True)
print(y)

##value that are not in both sets use setxorld()
import numpy as np
x=np.array([1,1,1,2,34,4,55,66,55,3,2,124,5,4])
z=np.array([11,13,165,21,342,4,255,266,755,3,2,124,5,4])
y=np.setxor1d(x,z,assume_unique=True)
print(y)