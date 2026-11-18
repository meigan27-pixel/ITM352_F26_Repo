#grab 1 month interest rate data from the treasury website
import ssl, lxml
import pandas as pd
import urllib.request

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603'
print("retrieving", url)

webpage = urllib.request.urlopen(url)
df = pd.read_html(webpage)

print("columns:", df[0].columns)

int_rate_table = df[0]

#print table of 1 month interest rates
print("1 month interest rates:")

for index, row in int_rate_table.iterrows():
    print(f"date: {row['Date']}, 1 month rate: {row['1 Mo']}")