#user enters a decimal number, calculate the square of the number and print it
#round the value to two decimal places
#Name: Meigan Mituyoshi
#Date: 9/2/2026

inputValue = input("Enter a floating point number: ")
floatValue = float(inputValue)
squareValue = floatValue ** 2
roundedValue = round(squareValue, 2)

print("you entered: ", floatValue)
print("the square of your number is: ", roundedValue)