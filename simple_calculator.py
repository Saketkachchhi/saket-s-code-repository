a = int(input("enter a number:"))
b = int(input("enter a number:"))

z = input("Enter an operator(+,-,*,/):")

if z == "+":
    print("the sum is:", a+b)
elif z == "-":
    print("the difference is:", a-b)
elif z == "*":
    print("the product is:", a*b)
elif z == "/":
    if b == 0:
        print("undefined")
    else:
        print("the quotient is:", a/b)
else:
    print("invalid operator")