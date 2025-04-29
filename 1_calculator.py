def addition(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print("Please input two numbers: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("""
Please select operation you want to perform:
      1. Addition
      2. Substraction
      3. Multiplication
      4. Division
""")
select = int(input("Select the operation(1,2,3,4): "))


if select == 1:
    print("Addition of two number:",addition(a,b))
elif select == 2:
    print("Substraction of two number:",substract(a,b))
elif select == 3:
    print("Multiplication of two number:",multiply(a,b))
elif select == 4:
    print("Divisionof two number:",divide(a,b))
else: 
    print("Please enter valid input: ")