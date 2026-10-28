#read json file of taxi trip data and create dataframe and simple stats
import pandas as pd

resultsDf = pd.read_json("Taxi_Trips.json")

print(resultsDf.head(6))

print(resultsDf.describe())

median = resultsDf["fare"].median()
print(f"the median fare value is: {median}")