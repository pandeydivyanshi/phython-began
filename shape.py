##shape of array - it is no. of elements in each dimension of array
import numpy as np
x=np.array([[1,22,3,33,12],[1223,34,45,3,22]])
print(x.shape)
###output (2,5) imply dimension is 2 and each dimension has 5 element

#5D array using ndim
import numpy as np
x=np.array([233333,2321,348765,234567],ndmin=5)
print(x)
print(x.shape)
##output (1,1,1,1,4)   fith dimen has 1 element ,fourth has 1 element and so on and last one D has 4elements

