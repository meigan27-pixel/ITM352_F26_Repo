# Read housing data, keep large properties, and clean the selected data.
import pandas as pd
from pathlib import Path


homes_data_file = Path(__file__).resolve().with_name("homes_data.csv")
homes_df = pd.read_csv(homes_data_file)
print(homes_df.head())


# Print the dimensions of the DataFrame.
shape = homes_df.shape
print("The dimensions of the dataframe are:", shape)


# Keep properties with more than 500 units and drop the easement column.
df_big = homes_df.loc[homes_df["units"] > 500].drop(columns=["easement"]).copy()
print(df_big.head(10))


# Look at the data types.
df_big.info()


# Coerce land_sqft, gross_sqft, and sale_price to numeric.
for column in ["land_sqft", "gross_sqft", "sale_price"]:
    df_big[column] = pd.to_numeric(df_big[column], errors="coerce")


# Drop rows with missing values and duplicate rows.
df_big = df_big.dropna().drop_duplicates()


# Look at the data types and print the cleaned data.
print("After cleaning....")
df_big.info()
print(df_big.head(10))