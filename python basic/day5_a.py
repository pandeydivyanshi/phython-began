##function##
def sum(a,b):                        #creating function
    sum =a+b
    print(sum)
    return sum
sum(5,6)                               #recalling function
sum(14,14)
##other way ##
def cal(a,b):                         ## a ,b are parameter
    return a+b
add=cal(77773,436748746)
print(add)
##fnc with no parameter##
def hlw():
    print("hello divyanshi how are you is everything right")         ## return no value
hlw()
hlw()
hlw()
output = hlw()
print(output)
##avg of 3 number##
def avg(a,b,c):
    sum = a+b+c
    avg=sum/3
    print(avg)

avg(99,99,88)
##builtin function##
print("divyanshi")
print("pandey")                          #print is built in fnc ,code gave output as next line
print("divyanshi",end="")
print("pandey")                          ## output in same line
print("divyanshi",end="$")
print("pandey") 
##len(),type(),range() are other in built fnc##
##default argument ##
def product(a,b=5):                                    # value assign in fnc already called default
    product=a*b
    print(product)
product(2)
def product(a=5,b=5):                                    ## first value in fnc assign should be non default
    product=a*b
    print(product)
product()
##trial 1##
yy = ["me","you","we",]
def print_len(lst):
    print(print_len(lst))
print_len(yy)