a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

z = input("Choose an operator (+, -, *, /): ")

if z == '+':
    c = a + b
    print("The sum is:", c)

elif z == '-':
    d = a - b
    print("The difference is:", d)

elif z == '*':
    e = a * b
    print("The product is:", e)

elif z == '/':
    if b != 0:
        f = a / b
        print("The quotient is:", f)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator! Please choose one of (+, -, *, /).")
