##rounding decimal- 5 ways in numpy :truncation,fix,rounding,floor,ceil
##truncation:trunc() and fix()
##these command remove decimal and return integer closest to zero
import numpy as np
x=np.array([12.32,23.44,3.24,3.34,.34,24.99,-32.3])
z=np.trunc(x)
print(x)
print(z)
y=np.fix(x)
print(y)

##rounding rounoff use around()
x=np.array([12.32,23.44,3.24,3.34,.34,24.99,-32.3])
z=np.around(x)
print(x)
print(z)

#floor() round off decimal to lower integer
x=np.array([12.32,23.44,3.24,3.34,.34,24.99,-32.3])
z=np.floor(x)
print(x)
print(z)  

##ceil() round off decimal to greater interger
x=np.array([12.32,23.44,3.24,3.34,.34,24.99,-32.3])
z=np.ceil(x)
print(x)
print(z) 