
num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))
op = input("Enter The Arithmetic Operator: ")
def add():
    num3=num1 + num2
    print(num3)

def subtract():
    num3=num1 - num2
    print(num3)

def multiply():
    num3=num1 * num2
    print(num3)

def divide():
    num3=num1 / num2
    print(num3)

def pow():
    num3=num1 ** num2
    print(num3)

if op == "+":
    add()

if op == "-":
    subtract()

if op == "*":
    multiply()

if op == "/":
    divide()

if op == "^":
    pow()