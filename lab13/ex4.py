import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
results_df = pd.DataFrame.from_records(results)

vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print("public vehicles and fuel sources: ")

vehicles.info()

vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)