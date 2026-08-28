def calculator():
    """
    A simple calculator program that performs basic math operations.
    Supports: addition, subtraction, multiplication, and division.
    """
    
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    
    try:
        # Get two numbers from the user
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Display operation options
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("\nEnter your choice (1/2/3/4): ").strip()
        
        # Perform the selected operation
        if operation == '1':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        
        elif operation == '2':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        
        elif operation == '3':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
        
        elif operation == '4':
            # Error handling for division by zero
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")
        
        else:
            print("\nError: Invalid operation choice. Please enter 1, 2, 3, or 4.")
    
    except ValueError:
        print("\nError: Please enter valid numbers.")
    
    print("\n" + "=" * 40)


if __name__ == "__main__":
    calculator()
