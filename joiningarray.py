##joining array by fnc np.concatenate()
import numpy as np
x=np.array([98787,25,2376])
y=np.array([132,33,332])
z=np.concatenate((x,y))
print(z)

##adding 2D array along with row (axis=1)
import numpy as py
x=np.array([[2342,454,873],[3323,78344,785334]])         # one row two cloumn
y=np.array([[288,4989,998],[3987,6774,988]])
z=np.concatenate((x,y),axis=1)                          #add two column in one row [[  2342    454    873    288   4989    998]
                                                                                  ##[  3323  78344 785334   3987   6774    988]]
print(z)

##joining array by fnc np.stack()
import numpy as np
x=np.array([98787,25,2376])
y=np.array([132,33,332])
z=np.stack((x,y),axis=1)                                 ##add row element and give column wise[[98787   132]
                                                                                              ##[   25    33]
                                                                                              ##[ 2376   332]]
print(z)

##stacking along with row np.hstack()
import numpy as np
x=np.array([98787,25,2376])
y=np.array([132,33,332])
z=np.hstack((x,y))               ##it add an gave one row   [98787    25  2376   132    33   332]
print(z)


##stacking along with rocolum np.vstack()
import numpy as np
x=np.array([98787,25,2376])
y=np.array([132,33,332])
z=np.vstack((x,y))               ##it add an gave one row   [[98787    25  2376]
                                                           ##[  132    33   332]]
print(z)

##stacking along with height/depth np.dstack()
import numpy as np
x=np.array([98787,25,2376])
y=np.array([132,33,332])
z=np.dstack((x,y))               ##it add an gave one row   [[[98787   132]
                                                            ##[   25    33]
                                                            ##[ 2376   332]]]
print(z)