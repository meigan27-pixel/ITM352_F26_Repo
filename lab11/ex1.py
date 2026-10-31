import pandas as pd
import ssl 

csvFile = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

ssl._create_default_https_context = ssl._create_unverified_context

try:
    df = pd.read_csv(csvFile, engine='python', on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print("error reading the csv file:", e)
