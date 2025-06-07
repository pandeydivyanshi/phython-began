##list##
marks=[19,30,39,75,32,24,23,79,97,65,30,11,35,68,67]
print(marks)
print(len(marks))
print(type(marks))
print(marks[0])                                        ##indexing in list
print(marks[1:5])                                      ##slicing in list
print(marks[1:])                                       ##slicing in list
print(marks[-6:-1])                                    ##negative indexing in list
biodata=["divyanshi",19,"MSc","statistics",30000000.543]          ##list can have different data types
print(biodata)
print(biodata[0])                                     ##indexing in list
print(len(biodata))                                   
print(type(biodata))          
print(biodata[1:3])                                   ##slicing in list    
print(biodata[-5:-2])                               ##negative indexing in list                    
name=["divyanshi","shubham","ujjwal","gaurav","rajani"]
print(name)
name[1]="guru dutt"                                  ##updating value in list allow in list
print(name)

##list functions##
num = [100,12,3,14,5,19,7,88,9]
num.append(11)                                  ##append function adds value at the end of list
print(num)
num.sort()                                    ##sort function sorts the list in ascending order
print(num)

num = [100,12,3,14,5,19,7,88,9]
num.reverse()                                 ##reverse function reverses the list
print(num)
num.remove(100)                               ##remove function removes the value from the list
print(num)
num.pop(5)                                  ##pop function removes the value at the given index
print(num)
