a = int(input("ENter a number: "))

match a:

    case 1:
     print("You entered one")
    case 2:
     print("You entered two")
    case _ if  2 < a <= 10:
     print("You entered a number less than or equal too 10 but greater than 2")
    case _ if a > 10:
     print("You entered a number greater than 10")
    case _ if a < 0:
     print("You entered a negative number")
    case _ if a == 0:
     print("You entered zero")
