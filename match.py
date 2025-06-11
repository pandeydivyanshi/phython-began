n = int(input("Enter the number: "))
match n:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case _ :                           ##deafult case
        print("You entered a number other than one, two, or three.")
   