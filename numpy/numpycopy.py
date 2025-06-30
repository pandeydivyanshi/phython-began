##difference btw copy and view
#we will make a copy ,change in original array and display both
import numpy as np
x=np.array([1,2,3,4])
y=x.copy()
x[0]=576786
print(x)
print(y)

##now we will make view and change original display both
import numpy as np
x=np.array([1,2,3,4])
z=x.view()
x[0]=2345678
print(x)
print(z)
