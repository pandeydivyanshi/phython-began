##normal(gaussian) ditribution
##random.normal() Parameter :loc(MEAN),scale(STANDARD DEVIATION),size

#generating normal distn of size 2*3
from numpy import random
x=random.normal(size=(2,3))
print(x)

#generating normal distn of size 2*3,with loc =1,scale=2
from numpy import random
x=random.normal(size=(2,3),loc=1,scale=2)
print(x)

##vizualisation of normal distn
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.normal(size=100),hist=(False))
ppt.show()
#bormal curve are bell shape