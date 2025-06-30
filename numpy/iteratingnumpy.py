##iterating imply going to each element one by one
##1 D array
import numpy as np
x=np.array([123,545,678,234567])
for i in x:
    print(i)

#for 2 D array
import numpy as np
x=np.array([[123,545,678,234567],[2343,49897,8676,353]])
for i in x:
    print(i)
## iterating each scaler in 2D array
import numpy as np
x=np.array([[123,545,678,234567],[2343,49897,8676,353]])
for i in x:
    for a in i:             ##use nested for loop
        print(a)

## iterated each scaler of 3D
import numpy as np
x=np.array([[[133,567,4356,12345],[2345,34565,234,234],[32,345,234,23],[23,34,34,234]]])
for i in x:
    for a in i:
        for b in a:
            print(b)


## iteration by np.nditer()
import numpy as np
x=np.array([[[133,567,4356,12345],[2345,34565,234,234],[32,345,234,23],[23,34,34,234]]])
for i in np.nditer(x):
    print(i)

##iterate with different stepsize (slicing)
import numpy as np
x=np.array([[123,545,678,234567],[2343,49897,8676,353]])
for i in np.nditer(x[:, ::2]):
    print(i)