def calculator():
    """
    A simple command-line calculator that performs basic arithmetic operations.
    """
    print("Simple Calculator")
    print("-----------------")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            break
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        else:
            result = num1 / num2
    else:
        # This case should ideally not be reached due to the earlier validation
        print("An unexpected error occurred.")
        return

    print(f"The result is: {result}")
calculator()
