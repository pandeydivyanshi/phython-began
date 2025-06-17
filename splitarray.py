##split array imply dividing array
##np.array_split()
import numpy as np
x=np.array([6254,87667,876,8985,678,98787])
y=np.array_split(x,3)
print(y)

##into 4 diff array
import numpy as np
x=np.array([6254,87667,876,8985,678,98787])
y=np.array_split(x,4)
print(y)

##into 5 diff array
import numpy as np
x=np.array([6254,87667,876,8985,678,98787])
y=np.array_split(x,5)
print(y)

## split into array with index
import numpy as np
x=np.array([6254,87667,876,8985,678,98787])
y=np.array_split(x,3)
print(y[0])                                             #[ 6254 87667]                   
print(y[1])                                             #[ 876 8985]
print(y[2])                                             #[  678 98787]

## split of 2 D array
import numpy as np
x=np.array([[11,22],[33,44],[55,66],[77,88],[99,1010],[1111,1212]])
y=np.array_split(x,3)
print(y)
##output[array([[11, 22],
       #[33, 44]]), array([[55, 66],
       #[77, 88]]), array([[  99, 1010],
       #[1111, 1212]])]

#split 2D int three 2D
import numpy as np
x=np.array([[1,1,22],[3,3,44],[5,5,66],[7,7,88],[9,9,1010],[111,1,1212]])
y=np.array_split(x,3)
print(y)
##output
#[array([[ 1,  1, 22],
       #[ 3,  3, 44]]), array([[ 5,  5, 66],
       #[ 7,  7, 88]]), array([[   9,    9, 1010],
       #[ 111,    1, 1212]])]

##split 2 D into three 2D along with row
import numpy as np
x=np.array([[1,1,22],[3,3,44],[5,5,66],[7,7,88],[9,9,1010],[111,1,1212]])
y=np.array_split(x,3,axis=1)
print(y)
#output
# [array([[  1],
#        [  3],
#        [  5],
#        [  7],
#        [  9],
#        [111]]), array([[1],
#        [3],
#        [5],
#        [7],
#        [9],
#        [1]]), array([[  22],
#        [  44],
#        [  66],
#        [  88],
#        [1010],
#        [1212]])]

##split by h split
import numpy as np
x=np.array([[1,1,22],[3,3,44],[5,5,66],[7,7,88],[9,9,1010],[111,1,1212]])
y=np.hsplit(x,3,)
print(y)
##output
# [array([[  1],
#        [  3],
#        [  5],
#        [  7],
#        [  9],
#        [111]]), array([[1],
#        [3],
#        [5],
#        [7],
#        [9],
#        [1]]), array([[  22],
#        [  44],
#        [  66],
#        [  88],
#        [1010],
#        [1212]])]