##reccursion##
def shw(n):
    if n == -1:                           ## base case (stopping condition)
      return
    print(n)
    shw(n-1)

shw(5)

# n to 1 reverse order #
def cunt(a):
    if a == 0:
     return
    print(a)
    cunt(a-1)
   
cunt(10)

def fact(b):
    if(b==1 or b==0):
       return 1
    else:
       return fact(b-1) * b
   
print(fact(5))
