##array indexing is used to access elements of an array start from 0
#1 D array indexing
import numpy as np
n=np.array([11,54,56,78,90])
print(n[0])                             #accessing first element of array
print(n[1])                                            #accessing second element of array
##we can add/subtract/multiply/divide elements of an array
print(n[3]+n[4])                      #adding 4th and 5th element of array

#2 D array indexing
#considering 2D array as a matrix
n2=np.array([[11,54,56,78,90],[12,45,67,89,100]])
print("first element of first row",n2[0,0])                        #accessing first element of first row
print("third element of first row",n2[1,2])                        #accessing third element of second row

#3 D array indexing
import numpy as np
d=np.array([[[11,54,56],[78,90,12]],[[45,67,89],[100,101,102]]])
print("first element of first row of first 2D array",d[0,0,0])        #accessing first element of first row of first 2D array
print("second element of second row of first 2D array",d[0,1,1])      #accessing second element of second row of first 2D array
