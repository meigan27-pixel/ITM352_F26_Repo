# Write code that will iterate through numbers from 1 to 10 and print 
# the number if it is not equal to 5 (using continue) and stop the 
# loop entirely and print a message when it reaches 8 (using break).

for x in range(10):
    if x == 8:
            print("done!")
            break
    if x != 5:
        print(x)
        continue
#order of if statements needed to be switched
#all numbers except 5 would be printed since it continues through 
#the whole list before moveing onto the next if statement
