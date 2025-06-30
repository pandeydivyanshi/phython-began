##rabndom imply something cant predict logically
##generating random integer
from numpy import random
x=random.randint(100)                     ##genertae any random number from 1 to 100
print(x)

##genertae any float via rand()
from numpy import random
x=random.rand()                       #3 genertae any random float from 0 to 1
print(x)

#creating random array of 6 integer element from0 to 100
from numpy import random
x=random.randint(100,size=(6))
print(x)

##creating random 2D array with 3rows and each have 6 element
from numpy import random
x=random.randint(100,size=(3,6))
print(x)

##creating 1D 6 element in float
from numpy import random
x=random.rand(6)
print(x) 

##creating random 2D array with 3rows and each have 6 float element
from numpy import random
x=random.rand(3,6)
print(x)

##genertaing random number from array with help of choice()
from numpy import random
x=random.choice([12,2,433,435,14,1435,3223])                     ##gave number in btw array
print(x)

##genertaing random number of 2D array with help of choice
from numpy import random
x=random.choice([12,2,433,435,14,1435,3223],size=(3,6))                       ##2D array with 3 row and each has 6 random element but they belong to that array element
print(x) 