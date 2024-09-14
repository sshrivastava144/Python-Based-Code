# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to run the calculator
def calculator():
    print("Welcome to the simple calculator!")
    
    while True:
        # Taking input from the user
        num1 = input("Enter the first number (or type 'exit' to quit): ")
        if num1.lower() == 'exit':
            break
        num2 = input("Enter the second number: ")
        operation = input("Choose operation (+, -, *, /): ")

        # Convert input strings to floats
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Perform the operation based on user input
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue
        
        # Display the result
        print(f"The result is: {result}\n")

# Run the calculator
calculator()
