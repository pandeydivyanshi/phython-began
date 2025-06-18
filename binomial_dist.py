# ##binomial distn -binary output
# ##parameter;n(total trial),p(prob),size(shape returend array)
from numpy import random
x=random.binomial(n=10,p=.5,size=10)
print(x)

 ##vizualization of data
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.binomial(n=10,p=.5,size=100),kde=False,hist=True)                 ##kde=false imply histogram width is less
ppt.show()

#diff btw normal and binomial visuals
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.displot
ssb.distplot(random.binomial(n=100,p=.5,size=1000),hist=False,label="BINOMIAL")
ssb.distplot(random.normal(loc=2,scale=1,size=1000),hist=False,label="NORMAL")
ppt.show() 