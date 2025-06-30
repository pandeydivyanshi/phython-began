##set##
set1={1,2,3,44,55,32,2,11,"world",'hello','hi','hi',23.99,(1,2,3,5,)}
print(set1)                                         #set ignore dublicate value, unordered,mutable,but element of set are immutable
print(len(set1))                                     #it doesn't include list , dictinory
print(type(set1))

##empty set ###
nul = set()                         ## correct syntax
print(nul)
print(type(nul))
set1.add("divyanshi")               ## add an element
print(set1)
set1.remove(44)                  ## remove an element
print(set1)
set2={1,2,456,885443,5365,532}
set2.clear()                           ## cleare all set
print(set2)
print(set1.pop())                         ##  random element pop out
###union ##
print(set2.union(set1))
print(set1.intersection(set2))

##trial##
word = {
    "table":("a pice of furniture","alist or facts"),
    "cat" : "animal",
}
print(word)

classroom = { "python","python","python","java","java","java","c","c","c","c++","c++","c++","javascript"}
print(classroom)
print(len(classroom))

marks={}
x=int(input("ener py:"))
marks.update({"phy":x})
y=int(input("ener ch:"))
marks.update({"chm":y})
z=int(input("ener math:"))
marks.update({"math":z})
print(marks)

values = {9,9.0}
print(values)
values = {"9",9.0}
print(values)
values = {9,"9.0"}
print(values)
values={ ("int",9),("float",9.0)}
print(values)




