##poission dist-estimate how many time an event occurs
##parameter;lam(no of occurance or rate),size
#generate a random 1*10 of occurance 2
from numpy import random
x=random.poisson(lam=2,size=10)
print(x)

##vizualisation
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.displot(random.poisson(lam=2,size=10),kde=False)                   #only give histogram
ppt.show()

#visualing normal and poisson on same graph
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.poisson(lam=2,size=10),hist=False,label="poisson")
ssb.distplot(random.normal(loc=2,scale=5,size=(100)),hist=False,label="normal")
ppt.show()



##n*p(in binomial) ==lam(in poisson)