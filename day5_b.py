yy = ["me", "you", "we"]
                                                              #trail 1
def print_len(lst):
    print(len(lst))  # 
    return len(lst)

print_len(yy)

def print_lst(lst):                                      ##trial 2
    for item in lst:
        print(item, end=' ')

print_lst(yy)

n=5
def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact(n)

def convt(usd):
    inr=usd*83
    print(usd,"USD",inr,"INR")
convt(100)

def input(n):

    if n%2 ==0:
        print("even")
    else:
        print("odd")
input(6)



