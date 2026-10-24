import csv

fileName = "taxi_1000.csv"

with open(fileName, "r") as file:
    csvReader = csv.reader(file)

    totalFare = 0
    maxDistance = 0
    aveFare = 0
    numRow = 0

    for row in csvReader:
        if numRow == 0:
            fareIndex = row.index('Fare')
            distanceIndex = row.index('Trip Miles')
            numRow += 1
            continue

        if numRow > 0:
            fare = float(row[fareIndex])
            distance = float(row[distanceIndex])

            if fare > 10:
                totalFare += fare

                if distance > maxDistance:
                    maxDistance = distance
            
            numRow += 1

if numRow > 1:
    aveFare = totalFare / (numRow - 1)  # Subtract 1 for the header row

print(f"Total Fare: ${totalFare:.2f}")
print(f"Average Fare: ${aveFare:.2f}")
print(f"Maximum Trip Distance: {maxDistance:.2f} miles")