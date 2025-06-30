##filtering miply getting some elements out and creating new array
##a boolean index list is list of boolean corresponding to index in array
import numpy as np
x=np.array([1,232,45,654,32])
y=np.array([True,False,True,False,True])
z=x[y]
print(z)                                        #[ 1 45 32]

##by filtering
##printing number higher than 5
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array=[]
for i in x:
    if i>5:
        array.append(True)
    else:
        array.append(False)
z=x[array]
print(z)
print(array)

##creating filter array of even elements
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array=[]
for i in x:
    if i%2==0:
        array.append(True)
    else:
        array.append(False)
z=x[array]
print(z)

##filter array direct by orignal array
import numpy as np
x=np.array([1,232,45,654,32,55,323,66,33,])
y=x>100                                         ##direct assinginf condition rather than true false
z=x[y]
print(y)
print(z)

##even numnber
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x%2==0                 ##direct assinginf condition rather than true false
z=x[y]
print(y)
print(z)
