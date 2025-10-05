### this is a simple calculator program using python function 


def add(a, b):
    z = a + b
    return z


def sub(a, b):
    z = a - b
    return z


def mul(a, b):
    z = a * b
    return z


def div(a, b):
    z = a / b
    return z


while True:
    number1 = input("enter the first number : ")
    if number1.isdigit():
        break
    else:
        continue


while True:
    number2 = input("enter the second number : ")
    if number2.isdigit():
        break
    else:
        continue

number1 = int(number1)
number2 = int(number2)

symbol = input("enter a symbol (+,-,*,/) : ")
if symbol == "+":
    print(add(number1, number2))
elif symbol == "-":
    print(sub(number1, number2))
elif symbol == "*":
    print(mul(number1, number2))
elif symbol == "/":
    print(div(number1, number2))
else:
    print("invalid symbol")
