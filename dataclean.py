# DONT RUN THIS FILE
# This file is used to clean the data and save it to a CSV file
# The original data is too large to upload to GitHub and process individually so its precleaned and saved to a CSV file
# This code is provided for reference only and to show how the data was cleaned/show work

import pandas as pd

df = pd.read_csv('DS0001/27521-0001-Data.tsv', sep='\t')
print(df.head())

cleaned = df.loc[:, ["NODR30A", "RK5ALWK", "GRSKD4_5", "ALCTRY", "ALCREC", "ALCYRTOT", "IRALCFY", "TOTDRINK",
                     "TXEVER", "ALCPHCTD", "ALCEMCTD", "ALCFMCTD", "TXYRINAD", "TXILALEV", "GENDER_R", "AGE_YRS", "ALLARRST"]]
print(cleaned.head())

# Save cleaned dataframe to a CSV file
cleaned.to_csv('cleaned_data.csv', index=False)
