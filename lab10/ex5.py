import pandas as pd
from pathlib import Path

homesDataFile = 'https://drive.google.com/file/d/1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex/'

homesDf = pd.read_csv(homesDataFile)
print(homesDf.head())

shape = homesDf.shape
print(f"the dimensions of the data frame are: {shape}")

dfBig = homesDf[homesDf["units"] >= 500]
print(dfBig.head(10))