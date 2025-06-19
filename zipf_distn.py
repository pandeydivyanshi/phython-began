##zipf distn:provide how commonly a words use
#parameter :a(distribution parameter),size
##sample of 2*3,a=3
from numpy import random
x=random.zipf(a=3,size=(2,3))
print(x)


##vizualistaion
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
x=random.zipf(a=3,size=(100))
ssb.distplot(x,kde=False)
ppt.show()