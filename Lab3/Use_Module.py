# Use the reusable math functions from the HandyMath module.
import handyMath


# Get two numbers from the user so every calculation uses the same inputs.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the requested results using f-strings for clear formatting.
print(f"The midpoint is {handyMath.midpoint(num1, num2)}.")
print(f"The square root of the square of {num1} is {handyMath.squareroot(num1 ** 2)}.")
print(f"{num1} raised to the exponent {num2} is {handyMath.exponent(num1, num2)}.")
print(f"The maximum is {handyMath.max(num1, num2)}.")
print(f"The minimum is {handyMath.min(num1, num2)}.")
