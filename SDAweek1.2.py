import csv as C
import os 
import numpy as N
import pandas as P
from IPython.display import display
print(os.getcwd())
N.nan
N.inf

data = P.read_csv('13-data.csv',
           # field separator character
           sep=",",
           # missing value characters
           #Find invalid values in the data and replace them either with a correct value (if possible) or with NaN.
           na_values=['NA'],
           # no row names
           index_col=False,
           # no column names
        
           # quote character
           quotechar='"')


df = P.DataFrame(data)


#Replace all missing values of the purchases variable with zero.
df['purchases'] = df['purchases'].fillna(0.0)

#Use median imputation to fill in all missing values of the retention_time variable.
df['retention_time'] = df['retention_time'].fillna(df['retention_time'].median())

#Find invalid values in the data and replace them either with a correct value (if possible) or with NaN.
for index, row in df.iterrows():
    if row['location'] == '33100':
        row['location'] = 'Tampere'
    if row['location'] == '20100':
        row['location'] = 'Turku'

display(df.to_string())




#4
df1 = P.read_csv('14-espoo.csv',
           # field separator character
           sep=",",
           # missing value characters
           na_values=['NA'],
           # no row names
           index_col=False,
           # no column names
        
           # quote character
           #quotechar='"'
           )

df2 = P.read_csv('14-helsinki.csv',
           # field separator character
           sep=",",
           # missing value characters
           na_values=['NA'],
           # no row names
           index_col=False,
           # no column names
        
           # quote character
           #quotechar='"'
           )

#merge the data into a single data frame.
df = P.merge(df1, df2, on="date", how="outer")

print(df)

#For how many days were observations made in total?
print(f"Total number of days observed: {len(df.index)}")

#How many observation days were there for each street?
print(f"Observation days for each street: {df.count()}")

#On how many days were all streets observed simultaneously?
print(f"Days all streets were observed simultaneously: {df.notna().all(axis=1).sum()}")

#Which street was the busiest in terms of the total number of cyclists?
df_sum= df.loc[:, df.columns != "date"]
print(df_sum.sum())
df_sum = df_sum.sum()
print(f"The busiest street had:{df_sum.max()}")

#Filter out the dates which have one or more missing values. Does this affect your conclusion about the busiest street? Why or why not?
df_all = df.dropna()

df_sum= df_all.loc[:, df_all.columns != "date"]
print(df_sum.sum())
df_sum = df_sum.sum()
print(f"And no the busiest street had:{df_sum.max()}")
