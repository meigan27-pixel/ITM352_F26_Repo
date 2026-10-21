#open file and read contents

with open("names.txt", "r") as fileObject:
    while(line := fileObject.readline()):
        print(line.strip())