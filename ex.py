data = ("hello", "10", "goodbye", 3, "goodnight", 5)

value = input("Enter a value to append: ")

try:
    data.append(value)
except Exception:
    data = (*data, value)

print("Updated tuple:", data)