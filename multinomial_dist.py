##multinomial distribution
##parameter:n(no.of trials),pvals(list of outcomes or possibility),size
from numpy import random
x=random.multinomial(n=50,pvals=[1/9,2/9,3/9,3/9])
print(x)

##multinomial will not provide single value
