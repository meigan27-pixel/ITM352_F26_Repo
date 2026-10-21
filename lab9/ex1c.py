#open file and read contents

with open("names.txt", "r") as fileObject:
    contents = fileObject.read()
    print(contents)
    contentsList = contents.split("\n")
    print(f"number of names: {len(contentsList)}")
    for name in contentsList:
        print(name)