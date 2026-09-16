first = input("enter your first name: " )
middleInitial = input("enter your middle initial: ")
last = input("enter your last name: ")

fullName = first + " " + middleInitial + ". " + last

print("Your full name is: " + fullName)
#using an f string
print(f"your full name using f string is: {first} {middleInitial}. {last}")
#using %
print("your full name using percent is %s %s. %s" % (first, middleInitial, last))
#using format()
print("your full name using format() is {} {}. {}".format(first, middleInitial, last))
#using join()
print("your full name using join() is " + " ".join([first, middleInitial + ".", last]))
#using format() but unpacking the list as the argument
print("your full name using format() but unpacking the list is {} {}. {}".format(*[first, middleInitial + ".", last]))