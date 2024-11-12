# Basic Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to perform the calculator operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            # Get user input for operation
            choice = input("Enter choice (1/2/3/4): ")

            # Ensure valid operation
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input, please choose 1, 2, 3, or 4.")
                continue

            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the operation based on user choice
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            # Ask if the user wants to continue
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Exiting the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()