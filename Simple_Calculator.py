
# This calculator supports basic arithmetic operations like addition, subtraction, multiplication, and division.

def sum_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")

def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")

def get_valid_number(prompt):
    """Prompt the user for a valid number, continue until a valid input is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_valid_operator():
    """Prompt the user for a valid operator, continue until a valid operator is entered."""
    while True:
        operator = input("Please enter an operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            return operator
        else:
            print("Invalid operator! Please enter one of the following: +, -, *, /")

def simple_calculator():
    """Simple calculator that continues asking for valid input until correct values are provided."""
    while True:
        a = get_valid_number("Please enter the first number: ")
        b = get_valid_number("Please enter the second number: ")
        operator = get_valid_operator()

        if operator == "+":
            sum_numbers(a, b)
        elif operator == "-":
            subtract(a, b)
        elif operator == "*":
            multiply(a, b)
        elif operator == "/":
            divide(a, b)

        # Ask the user if they want to perform another calculation
        another_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calc != 'yes':
            break

if __name__ == "__main__":
    simple_calculator()
