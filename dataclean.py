# DONT RUN THIS FILE
# This file is used to clean the data and save it to a CSV file
# The original data is too large to upload to GitHub and process individually so its precleaned and saved to a CSV file
# This code is provided for reference only and to show how the data was cleaned/show work

import pandas as pd

df = pd.read_csv('DS0001/27521-0001-Data.tsv', sep='\t')
print(df.head())

cleaned = df.loc[:, ["NODR30A", 'ALCTRY', 'ALCREC', 'IRALCFY',
                     'ALCYDAYS', 'TOTDRINK', "IRSEX", "AGE_YRS", "BOOKED"]]
print('BEFORE CLEANING')
print(cleaned.head())
print(cleaned.shape)  # (55602, 9)

# remove rows with values like 975, 985, 991, 993, 994, 997, 998
cleaned = cleaned[cleaned["NODR30A"] < 900]
cleaned = cleaned[cleaned["ALCTRY"] < 900]
cleaned = cleaned[cleaned["TOTDRINK"] < 900]
cleaned = cleaned[cleaned["BOOKED"] < 90]

# change values of 3 to 1 from BOOKED
cleaned["BOOKED"] = cleaned["BOOKED"].replace(3, 1)


print('AFTER CLEANING')
print(cleaned.head())
print(cleaned.shape)  # (22853, 9)

# save cleaned data to csv
cleaned.to_csv('DS0001/cs105_dataset.csv', index=False)
