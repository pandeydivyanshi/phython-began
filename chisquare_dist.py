##chi square distn use for testing of hyputhesis
#parameter :df(degree of freedom),size
##chi square with df 2 size2*3
from numpy import random
x=random.chisquare(df=2,size=(2,3))
print(x)

##visualization
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.chisquare(df=2,size=(2,3)),hist=False)
ppt.show()