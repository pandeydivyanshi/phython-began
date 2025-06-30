##rayleigh ditn-used in signal processing
#parameter:scale(S.D,how flat the ditsn is/default value 1),size
#Rl with scale 2,size 2*3
from numpy import random
x=random.rayleigh(scale=2,size=(2,3))
print(x)

##vizualisation
from numpy import random
import matplotlib.pyplot as ppt
import seaborn as ssb
ssb.distplot(random.rayleigh(scale=2,size=(2,3)),hist=False)
ppt.show()
