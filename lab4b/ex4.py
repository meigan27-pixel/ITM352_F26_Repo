#parse through portions of email address and print out domain name and username
#name: Meigan Mitsuyoshi
#Sept. 18, 2026

email = input("Enter an email address: ")

parts = email.split("@")
username = parts[0]
domain = parts[1]

print("Username is:", username)
print("Domain name is:", domain)

#method 2: using index() and slicing()
atIndex = email.index("@")
username2 = email[:atIndex]
domain2 = email[atIndex + 1:]
print("Username (method 2):", username2)
print("Domain name (method 2):", domain2)
