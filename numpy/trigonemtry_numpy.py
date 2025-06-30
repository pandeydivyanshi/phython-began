##trignometry function :ufunc such sin(),cos(),tan() gave value in raidian
## for value in degree sin value of pi/2
import numpy as np
x=np.sin(np.pi/2)
print(x)

##now we will find sin value of an array
import numpy as np
x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.sin(x)
print(y)

##degree into radian:by default radiun
##radians values are pi/180*degree value
import numpy as np 
x=np.array([90,180,270,360])
y=np.deg2rad(x)
print(y)

##radian into degree
import numpy as np 
x=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
y=np.rad2deg(x)
print(y)

##find angles:arcsin(),arccos(),arctan() take values in radian and produce tha corresponding sin,cos,tan

#we will now find the angle of 1.0
import numpy as np
x=np.arcsin(1.0)
print(x)

##angle of each values in array
import numpy as np
x=np.array([1,-1,.1])
y=np.arcsin(x)
print(y)

##we can also find hypotenous using the pythagoras theorem in numpy
##hypto() function that take value in radians and produce correspoinding sin,cos,tan value
##base=4,perendicular3
import numpy as np
base=3
perp=4
x=np.hypot(base,perp)
print(x)
