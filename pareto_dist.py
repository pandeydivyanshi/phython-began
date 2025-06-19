##pareto distn:80:20(20% factor cause 80% outcome)
##parameter:a(shape parameter),size
from numpy import random
x=random.pareto(a=6,size=(2,3))
print(x)

##visualization
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.pareto(a=6,size=(2,3)))
ppt.show()