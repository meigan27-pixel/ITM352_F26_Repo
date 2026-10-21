#open a file and print its type

fileObject = open("names.txt", "r")
print(type(fileObject))
fileObject.close()
