##searching array imply search for certain value and return the index that give the match
##using fnc where()
import numpy as np
x=np.array([11,323,11,323465,4332,11,2345,11,345,445,11])
y=np.where(x ==11)                            ## return index where 11 is present
print(y)

##index on which even number present
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=np.where(x%2==0)
print(y)

##index on which odd number present
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=np.where(x%2==1)
print(y)

##searchsorted()  ,perform binary search in array
#we will find the index where value 7 will be inserted
import numpy as np
x=np.array([1,7,3,4,5,6,9,8,9,10,12])
y=np.searchsorted(x,7,side='left')
print(y)

##search from right
import numpy as np
x=np.array([1,7,3,4,5,6,8,9,10,12])
y=np.searchsorted(x,7,side='right')
print(y)