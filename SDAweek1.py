import csv as C
import numpy as N
import pandas as P
from IPython.display import display

N.nan
N.inf

data = P.read_csv('allbp.data',
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
columns = len(df.axes[1])-1  
 
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
print(data.isnull().sum().sum())

#2.1 The number of yes values divided by the number of observations
data_t = (data== "t").sum()
data_f = (data== "f").sum()

print("Number of yes values divided by the number of observations")
print(data_t / rows)

#2.2 The sum of the squared values divided by the number of non-NA values

variables = data[['TSH','T3','TT4','T4U','FTI','TBG']]
df2 = P.DataFrame(variables)
notnull = variables.notnull().sum().sum()
df2['Sum of the squared values T3/non-NA'] = ((df['TSH']**2).sum())/notnull
df2['Sum of the squared values TT4/non-NA'] = ((df['TT4']**2).sum())/notnull
df2['Sum of the squared values T4U/non-NA'] = ((df['T4U']**2).sum())/notnull
df2['Sum of the squared values FTI/non-NA'] = ((df['FTI']**2).sum())/notnull
df2['Sum of the squared values TBG/non-NA'] = ((df['TBG']**2).sum())/notnull
print("The sum of the squared values divided by the number of non-NA values")
print(df2)

#2.3 The mean ratio between T3 and TT4
ratios = variables[['T3','TT4']]
df3 = P.DataFrame(ratios)
df3['Ratio between T3 and TT4'] = (df['T3']/df['TT4'])
print(df3)

print("The mean ratio between T3 and TT4:" ,(df3['Ratio between T3 and TT4'].sum())/len(df3.axes[0]))
