##uniform distn - it is for prob
##parameter-a(lowerbound 0.0),b(upper bound 1.0),size
from numpy import random
x=random.uniform(size=(2,3))            ##2D array with 2 row and each have 3 element
print(x)


##for visualisation
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.uniform(size=(2,3)))
ppt.show()

#3visualization unform and normal
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.uniform(size=(2,3)),hist=False,label="unform")
ssb.distplot(random.normal(loc=1,scale=1,size=(100)),hist=False,label="normal")
ppt.show()