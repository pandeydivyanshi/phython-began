##slicing array means extracting a portion of the array
##syntax: array[start:stop:step],[start:end]
#example of slicing array from1 to 5
import numpy as np
n=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(n[1:5])                                       ## Output: [2 3 4 5]
print(n[0:9:2])                                     ## Output: [1 3 5 7 9]
print(n[1:])                                        ## Output: [ 2  3  4  5  6  7  8  9 10]
print(n[:5])                                        ## Output: [1 2 3 4 5]

##negative slicing
import numpy as np
n=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(n[-5:-1])                                     ## Output: [6 7 8 9]
print(n[-5:])                                       ## Output: [ 6  7  8  9 10]

##now print every other element
import numpy as np
n=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(n[::2])                                       ## Output: [1 3 5 7 9]

##2D array slicing
import numpy as np
n = np.array([[1, 2, 3,645,665,678], [4, 5, 6,567,989,6799]])
print(n[0, 1:4])                                    ## Output: [2 3 645]
print(n[1, 2:])                                     ## Output: [6 567 989 6799]
##a value from both rows/index
print(n[0:2,4])                                  ## Output: [665 989]
print(n[0:2, 1:4])                                  ## Output: [[2 3 645]
                                                     ##          [5 6 567]]

##3D array slicing                                                     
import numpy as np
a= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[0, 1, 2])                                    ## Output: 6
print(a[1, 0, 1])                                    ## Output: 8
print(a[0, :, 1])                                    ## Output: [2 5]
print(a[:, 1, :])                                    ## Output: [[ 4  5  6]
                                                     ##          [10 11 12]]