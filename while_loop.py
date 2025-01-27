#print first 10 numbers using while loop
i = 1
while i<10:
   print(i)
   i+=1

#take input from the user, untill he enters a number more tha 50

while i<50:
   i = int(input("Enter a number: "))
   if 0 < i < 50: 
      print("you entered an appropriate number")
   elif i > 50:
      print("You entered a number greater than 50")
   elif i == 50:
      print("You entered 50")
   else:
      print("You entered a negative number")


#nested while loop

while i<100:
    while i>50:
        print(i)
        i+=1