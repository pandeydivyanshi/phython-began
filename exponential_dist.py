##exponential distn - used to describe time till next event that is like failure or suecces
##parameter:scale(inverse of rate),size
##exponential of scale = 2.0,size=2*3
from numpy import random
x=random.exponential(scale=2,size=(2,3))
print(x)

##visualization
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.exponential(scale=2,size=(100)),hist=False)
ppt.show()