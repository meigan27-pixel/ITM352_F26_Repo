#open file and read contents
#append a new name at end of file

with open("names.txt", "r") as fileObject:
    contentsList = fileObject.readlines()
    print(contentsList)

with open("names.txt", "a") as fileObject:
    print(f"appending new name to file....")
    fileObject.write("Doe, Jane\n")