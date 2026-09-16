#Define a list of survey response values [5, 7, 3, and 8] and store them in a variable
#Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053)
#and add to list
#Name: Meigan Mitsuyoshi
#Sept. 16, 2026

responseValues = [5, 7, 3, 8]
responseValues.sort()
responseIDs = (1012, 1035, 1021, 1053)
responseValues.append(responseIDs)

print("combined response values and IDs:", responseValues)

responseValuesNew = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
print("combined response values and IDs using a list of tuples:", responseValuesNew)