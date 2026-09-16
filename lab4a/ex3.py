#manipulate a list in various tricky ways
#Name: Meigan Mitsuyoshi
#Sept. 16, 2026

responseValues = [5, 7, 3, 8]
responseValues.append(0)

print("response values with 0 appended:", responseValues)

#responseValues.insert(2, 6)
#print("response values with 6 inserted at index 2:", responseValues)

responseValues = responseValues[:2] + [6] + responseValues[2:]
print("response values with 6 inserted at index 2:", responseValues)