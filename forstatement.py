#for first 100 interger, print all even numbers

for a in range(100):
  if a % 2 == 0:  
    break
  else:
    print(a)


# print next 100 numbers after a.

a = int(input("Enter a number: "))

for a in range(a, a + 100):
    print(a)


# print all numbers from 0 to 100 in steps of 5
for k in range(0, 119, 5):
  print(k)    
  if k == 100:
    break


#print the fruits in the list

fruits = ["apple", "banana", "orange"]   #the fruits names are saved as a list

for i in fruits:
    print(i)
    for fruit in i:
        print(fruit)
        