import csv as C
import numpy as N
import pandas as P
from IPython.display import display

N.nan
N.inf

data = P.read_csv('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/Statistical Data Analysis/thyroid+disease/allbp.data',
           # field separator character
           sep=",",
           # missing value characters
           na_values=["?"],
           # no row names
           index_col=False,
           # no column names
           header=None,
           # quote character
           quotechar="'")

data.columns = ['age','sex','on thyroxine','query on thyroxine','on antithyroid medication','sick','pregnant','thyroid surgery','I131 treatment','query hypothyroid','query hyperthyroid','lithium','goitre','tumor','hypopituitary','psych','TSH measured','TSH','T3 measured','T3','TT4 measured','TT4','T4U measured','T4U','FTI measured','FTI','TBG measured','TBG','referral source','']
# 1.1 How many observations and variables
df = P.DataFrame(data)
rows =  len(df.axes[0])
columns = len(df.axes[1])  
 
display(data)

print("How many observations: ",  rows ,"and variables: ", columns)

#1.2 Which variables have missing values
nan_cols = []
for i in data.columns:
    if data[i].isnull().any():
        nan_cols.append(i)
print("Which variables have missing values")
print(nan_cols)

# How many
print("How many?")
print(df.isna().sum(), end="\n\n")
print(data.isnull().sum().sum())

#2.1 The number of yes values divided by the number of observations
data_t = (data== "t").sum()
data_f = (data== "f").sum()

print("Number of yes values divided by the number of observations")
print(data_t / rows)

#2.2 The sum of the squared values divided by the number of non-NA values

quantitative_idx = [17, 19, 21, 23, 25, 27]

subset = df.iloc[:, quantitative_idx]
result = (subset**2).sum(axis=0) / subset.notna().sum(axis=0)
print(result, end="\n\n")


#2.3 The mean ratio between T3 and TT4

print("The mean ratio between T3 and TT4:" ,((df['T3'] / df['TT4']).mean()))

