# a = int(input("enter your age: "))
# print("your age is: ", a)

# if a >= 18:
#     print("you are eligible to Drive")
# else:
#     print("you are not eligible to Drive")


# a = int(input("enter a number:"))

# if a < 0:
#     print("negative number")
# elif a > 0:
#     if a > 10:
#         print("positive number greater than 10")
#     elif a < 10:
#         print("positive number less than 10")
# else:
#     print("zero")



#TELL GOODMORNING GOODNIGHT GOOD AFTERNOON DEPENDING ON THE TIME

import datetime                 #import the datetime module
now = datetime.datetime.now()   #get the current time, date and year 

if now.hour < 12:
    print("Good Morning")
elif now.hour < 18:
    print("Good Afternoon")
else:
    print("Good Night")