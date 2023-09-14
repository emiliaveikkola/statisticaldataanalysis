import csv as C
import os 
import numpy as N
import pandas as P
from IPython.display import display
print(os.getcwd())
N.nan
N.inf

data = P.read_csv('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/Statistical Data Analysis/Data files-20230907-2/13-data.csv',
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

df.loc[df.retention_time < 0, 'retention_time'] = N.NaN

#Use median imputation to fill in all missing values of the retention_time variable.
df['retention_time'] = df['retention_time'].fillna(df['retention_time'].median())

#Find invalid values in the data and replace them either with a correct value (if possible) or with NaN.
for index, row in df.iterrows():
    if row['location'] == '33100':
        row['location'] = 'Tampere'
    if row['location'] == '20100':
        row['location'] = 'Turku'
    if row['sex'] == 'nale':
        row['sex'] == 'male'   

display(df.to_string())



#4
df1 = P.read_csv('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/Statistical Data Analysis/Data files-20230907-2/14-espoo.csv', index_col=0)

df2 = P.read_csv('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/Statistical Data Analysis/Data files-20230907-2/14-helsinki.csv', index_col=0)

#merge the data into a single data frame.
df = P.merge(df1, df2, left_index=True, right_index=True, how='outer')

print(df)

#For how many days were observations made in total?
print(f"Total number of days observed: {len(df.index)}")

#How many observation days were there for each street?
print("Observation days for each street: ")
print((~df.isna()).sum(axis=0), end="\n\n")

#On how many days were all streets observed simultaneously?
print(f"Days all streets were observed simultaneously: {df.notna().all(axis=1).sum()}")

#Which street was the busiest in terms of the total number of cyclists?
print("The number of cyclits the busiest street had: ")
print(df.sum(axis=0).sort_values(ascending=False), end="\n\n")

#Filter out the dates which have one or more missing values.
print("And now the busiest street had :")
print(df.dropna().sum(axis=0).sort_values(ascending=False), end="\n\n")
