##if statment##
age = int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote\ncan get driving license\ncan get passport\ncan get job")
elif(age<18):
    print("You are not eligible to vote\ncan not get driving license\ncan not get passport\ncan not get job\nyou are minor")

## traffic rule##
light=input("enter colour:")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("get ready to go")
else:print("Invalid colour input")
    
print("thanx")

##mark distribution##
marks=int(input("enter marks:"))
if(marks>=90):
    print("A grade")
elif(marks<90 or marks>=80):
    print("B grade")
elif("marks<80 or marks>=70"):
    print("C grade")
else:
    print("do your best")

 ###odd or even number###

num = int((input("enter number:")))
if(num%2==0):
     print("EVEN NUMBER")
else:
    print("ODD NUMBER")

##greater of three numbers##
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))    
num3 = int(input("Enter third number: "))
if(num1>num2 and num1>num3):
    print("first number is greater")
elif(num2>num1 and num2>num3):
    print("second number is greater")
elif(num3>num1 and num3>num2):
    print("third number is greater")
else:
    print("all numbers are equal")

##divisibility by 7##
num = int(input("Enter a number: "))
if(num % 7 == 0):
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")