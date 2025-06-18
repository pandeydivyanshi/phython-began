##numpy random module provide two method 1.suffel()   2.permutation()
#now we shuffel element of array
##shuffel() make change in orignal array
from numpy import random
import numpy as np
x=np.array([132,435,6547,21,34,456,98,23])
random.shuffle(x)
print(x)

##now by permutation
##permutatin() leave orignal value unchanged
from numpy import random
import numpy as np
x=np.array([132,435,6547,21,34,456,98,23])
print(random.permutation(x))
