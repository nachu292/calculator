# this is a  calculator program

def add(x, y):
    z = x + y
    return z


def sub(x, y):
    z = x - y
    return z


def mul(x, y):
    z = x * y
    return z


def div(x, y):
    z = x / y
    return z


def mod(x, y):
    z = x % y
    return z


while True:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    symbol = input("Enter operator (+, -, *, /, %): ")
    if num1.isdigit() and num2.isdigit():
        if symbol == "+":
            num1 = int(num1)
            num2 = int(num2)
            print(f"result: {add(num1, num2)}")
            ask = input("Do you want to continue? (yes/no): ")
            if ask.lower() != "yes":
                break
        elif symbol == "-":
            num1 = int(num1)
            num2 = int(num2)
            print(f"result: {sub(num1, num2)}")
            ask = input("Do you want to continue? (yes/no): ")
            if ask.lower() != "yes":
                break
        elif symbol == "*":
            num1 = int(num1)
            num2 = int(num2)
            print(f"result: {mul(num1, num2)}")
            ask = input("Do you want to continue? (yes/no): ")
            if ask.lower() != "yes":
                break
        elif symbol == "/":
            num1 = int(num1)
            num2 = int(num2)
            print(f"result: {div(num1, num2)}")
            ask = input("Do you want to continue? (yes/no): ")
            if ask.lower() != "yes":
                break
        elif symbol == "%":
            num3 = float(num1)
            num4 = float(num2)
            print(f"result: {mod(num3, num4)}")
            ask = input("Do you want to continue? (yes/no): ")
            if ask.lower() != "yes":
                continue
            elif ask.lower() == "no":
                break
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid operator. Please try again.")
            continue
    else:
        print("Invalid input. Please enter numeric values.")
