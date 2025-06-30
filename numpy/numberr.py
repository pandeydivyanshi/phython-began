import numpy as np
print("version:", np.__version__)
##now we will create a numpy ndarray object
##the array object in numpy is called ndarray
#array()
x=np.array([1,2,3,4,5])
print("x:", x)
print("type of x:", type(x))
## we can also pass a list of list,tuple or an array loke onject with array() and it will create a ndarray
import numpy as np
a=np.array((1,2,3,4,5),)
print("a:", a)
print("type of a:", type(a))

##dimension in array
##dimension in array is one level of array depth(also called nested array)
##0d array is a scalar
#e.g
b=np.array(5)
print("b:", b)
#1D array is a vector 
#e.g
c=np.array([1,2,3,4,5])
print("c:", c)
##creating a 2D array
import numpy as np
d=np.array([[1,2,3],[4,5,6]])
print("d:", d)
print("type of d:", type(d))
##creating a 3D array frome 2D array
import numpy as np
n=np.array([[[1,2,3],[6,7,88]],[[88,22,11],[33,44,55]]])
print("n:", n)
print("type of n:", type(n))

##check how many dimensions an array has by attribute ndim
import numpy as np
b=np.array(5)
c=np.array([1,2,3,4,5])
d=np.array([[1,2,3],[4,5,6]])
n=np.array([[[1,2,3],[6,7,88]],[[88,22,11],[33,44,55]]])
print("b.ndim:", b.ndim)
print("c.ndim:", c.ndim)
print("d.ndim:", d.ndim)
print("n.ndim:", n.ndim)
##create an 5D array to check the ndim attribute
import numpy as np
e=np.array([1,23,4,5,6],ndmin=5)
print("e:", e)
print("e.ndim:", e.ndim)

##check the shape of an array by attribute shape
import numpy as np
b=np.array(5)
c=np.array([1,2,3,4,5])
d=np.array([[1,2,3],[4,5,6]])
n=np.array([[[1,2,3],[6,7,88]],[[88,22,11],[33,44,55]]])
e=np.array([1,23,4,5,6],ndmin=5)
print("b.shape:", b.shape)
print("c.shape:", c.shape)
print("d.shape:", d.shape)
print("n.shape:", n.shape)
print("e.shape:", e.shape)