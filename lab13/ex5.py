#get json file from city of chicago data portal and analyze driver types
import pandas as pd
import requests

url = 'https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type'
response = requests.get(url)

response_json = response.json()

print("driver types and counts:")

response_df = pd.DataFrame.from_records(response_json)
response_df.columns = ['driver_type', 'count_license']
response_df = response_df.set_index("driver_type")

print(response_df)