#create pandas data frame from individual lists

import pandas as pd

# List of individuals
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

rawData = zip(ages, gender)

df = pd.DataFrame(data=rawData, index=names, columns=["ages", "gender"])

summary = df.describe()
print(summary)

aveAge_by_gender = df.groupby("gender")["ages"].mean()
print(f"average age by gender: ")
print(aveAge_by_gender)
