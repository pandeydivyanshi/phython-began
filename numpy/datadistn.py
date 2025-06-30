##data ditn is list of all possible values and how often they appear
##such list is imp when work with statistics and data science
##creating 1D array with 100 values where each value has to be 3,5,7,9
#the  prob that 3 is in set .1
#the  prob that 5 is in set .4
#the  prob that 7 is in set .3
#the  prob that 9 is in set .2
from numpy import random
x=random.choice([3,5,7,9],p=[.1,.4,.3,.2],size=(100))
print(x)

##now with 2D
from numpy import random
x=random.choice([3,5,7,9],p=[.1,.4,.3,.2],size=(3,5))
print(x)

