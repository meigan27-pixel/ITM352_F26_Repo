#ask the user to enther their birth year and then calculate their age 
# based on the current year printed out
#Name: Meigan Mituyoshi
#Date: 9/2/2026

birthYear = input("Enter your birth year: ")
currentYear = 2026
age = currentYear - int(birthYear)

print("you entered: ", birthYear)
print("your age is: " + str(age))
