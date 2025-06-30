#arthimatic operatorsAdd commentMore actions
a=5
b=8
print(a+b)  #addition
print(a-b)  #substraction
print(a*b)   #multiplication
print(a/b)   #division
print(a%b)   #modulus use for finding remainder
print(a**b)  #exponentiation ,a^b
print(a//b) #floor division it return the largest integer less than or equal to division reault

##relational operators
# it return boolean value True or False
print(a==b)  #equal to
print(a!=b)  #not equal to
print(a>b)  
print(a>=b)  
print(a<b)  
print(a<=b)  

#assignment operators
num=10
num+=5                                                  #is equal to num = num + 5,+=is assignment operator
print("add is",num)
num-=3                                                                #-= is assignment operator , equal to num = num-3
print("sub is",num)
num*=2                                                                              # *= is assignment operator
print("multi is",num)
num/=2                                                                #/= is assignment operator
print("div is",num)
num%=3                                                                      # for remainder
print("mod is",num)
num**=6                                                                            #power
print("power is",num)
num//=2                                                                          # floar division
print("floor dividion is",num)
 
 ## logical operators
 #it work on boolean values
a=True
print(not a)                                                                             #not operator
a = 5
b = 15
print(not(a>b))                                                                  #not operator
print(a==b and  b>10)                                                                # and
print(a==b or b>10)  