##tuple##
tup=(1,2,"sita","ram",)
print(tup)
print(type(tup))
print(len(tup))                    #length of tuple


##empty tuple##
tup1={}
print(tup1) 
print(type(tup1))
              

##tuple with single element##
tup2=(1,)                              #comma is necessary to define a single element tuple,otherwise it will be considered as an integer
tup3=("sita",)                        #comma is necessary to define a single element tuple,
print(tup2)
print(type(tup2))
print(tup3)
print(type(tup3))



##trial
movie=[]
mov=input("Enter movie name: ")
movie.append(mov)
mov2=input("Enter movie name: ")
movie.append(mov2)
mov3=input("Enter movie name: ")
movie.append(mov3)
print(movie)