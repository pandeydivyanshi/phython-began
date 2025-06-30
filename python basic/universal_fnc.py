##unfnc stands for universal function of numpy that operate on nparray
##ufunc also take additional argument like where,dtype,out
##vectorization - converting the iterative statment into vector based statment
##example without ufunc ,here we will use python inbuilt zip()
x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i,j in zip(x,y):             #adding both list
    z.append(i+j)
print(z)

##with ufunc we will use add() function
import numpy as np
x=[1,2,3,4]
y=[4,5,6,7]
z=np.add(x,y)
print(z)