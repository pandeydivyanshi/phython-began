##break and continue ##
num = (1,44,76,24,46,7898,75,753,9997,42,66,3,5,67,99)
x=5
i=0
while(i<=len(num)):
    if(num[i] == x):
        print("x found at",i)
        break
    else:
        print("not found")
    i+=1


print("end of")

##continue##


a = 0
while a <= 5:
    if a == 3:
        a += 1
        continue
    print(a)
    a += 1


a = 0
while a <= 10:
    if a % 2 == 0:
        a += 1
        continue
    print(a)
    a += 1

a = 0
while a <= 10:
    if a % 2 != 0:
        a += 1
        continue
    print(a)
    a += 1
