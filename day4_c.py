## for loop##
list=(1,2,3,4,5,7,8,9,3,32,6,)
for var in list:
    print(var)
tup=("divyanshipandey")
for che in tup:
    if(che=="p"):
        print("p found")
        break
    print(che)
else:
    print("END")

    ##trial1##
list1=[1,4,9,16,25,36,49,64,81,100]
for val in list1:
    print(val)
    x=49
for value in list1:
    if(value == x):
        print("x found")
        break
    print(value)

    ## range ##
for el in range(5):                            ##ending value (but in range ending value doesnot include)
    print(el)
for pin in range(1,5):                           ##statring value,ending value
    print(pin)
for inn in range(1,5,2):                          ##starting value,ending value, step size
    print(inn)
## even number ##
for nm in range(0,50,2):
    print(nm)

#trial1#
for mm in range(1,100):
    print(mm)

##trail2##
for nn in range(100,1,-1):
    print(nn)

##trail3#
n=int(input("enter number"))
for tt in range (1,11):
    print(tt*n)

    ##pass##
for pp in range(6):
    pass
print("we use pass statment to make loop empty")

## sum of n number##
n = 22
sum = 0
for yy in range (1,n+1):
    sum+=yy

print("total sum",sum)

p=0
add = 0
while p<=22:
    add +=p
    p+=1

print("total ",add)

##factorial##

fac = 1
for xx in range(1,6):
    fac*=xx

print("factorial ",fac)