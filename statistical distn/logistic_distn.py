##logistic distn -discribe growth and imp in regression
##parameter-loc(mean(deafault value 0)),scale(s.d(default value 1)),size
##2*3 size sample with mean 1,sd 2.0,
from numpy import random 
x=random.logistic(loc=1,scale=2,size=(2,3))
print(x)

##vizualisation
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.logistic(loc=1,scale=2,size=(2,3)))
ppt.show()

##normal and logistic
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.logistic(loc=1,scale=2,size=(100)),hist=False,label="logistic")
ssb.distplot(random.normal(size=(100)),hist=False,label="normal")
ppt.show()

