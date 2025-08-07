def calculate():
    """Performs a calculation and handles potential errors gracefully."""
    try:
        operator = input("Enter an operator (+, -, *, /): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2  # The ZeroDivisionError will be caught below
        else:
            print("Error: Invalid operator.")
            return  # Stop if the operator is not valid

        print(f"The result is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    calculate()
