import numpy as np 
from statistics import mean
from statistics import median

#1
list1 = [5, 8, 7, 6, 8, 4]
list2 = [1.3, 2.1, 1.8, 1.2, 1.4, 2.3]
list3 = ['y', 'y', 'n', 'y', 'n', 'n']

A = np.array(list1)
B = np.array(list2)
C = np.array(list3)

matrix = np.column_stack((A, B, C))

print(f"Matrix: \n {matrix}")

print(f"Element (3,2): {matrix[2][1]}")
print(f"4th row: {matrix[3]}")

sub1 = matrix[np.ix_([1,2,3,4],[1,2])]
sub = matrix[1:5, -2:]

print(f"Submatrix of 2 last columns and rows 2-5: \n {sub}")

matrix_t = np.transpose(matrix)

print(f"Transpose of data matrix: \n {matrix_t}")


#3&4
from matplotlib import pyplot
import seaborn as sns

# Generate some data for this demonstration.
data1 = [170, 192, 184, 168, 176, 181, 163]
data2 = [170, 170, 170, 170, 192, 192, 192, 192, 184, 184, 184, 184, 168, 168, 168, 168, 176, 176, 176, 176, 181, 181, 181, 181, 163, 163, 163, 163]

bins = (160,170,180,190,200)

pyplot.hist(data1, bins,  label='data1')
pyplot.hist(data2, bins, alpha = 0.2, label='data2')
pyplot.legend(loc='upper right')
pyplot.ylim(0, 9)

pyplot.show()

sns.distplot(np.array(data1), hist=False, label = 'data1')
sns.distplot(np.array(data2), hist=False, label = 'data2')
pyplot.legend(loc='upper right')

pyplot.show()

#1: It's not possible to conclude that the distribution is not normal.
#2: There's statistical evidence that the distribution is not normal.

#5

import csv
import pandas as P

with open('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/Statistical Data Analysis/graph.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.strip().split('\n')

# Extract the relevant lines with actual data
data_lines = [line.split() for line in lines[5:]]


# Convert the data to CSV format
csv_data = "\n".join(",".join(line) for line in data_lines)

# Write the CSV data to a file
with open('temperature_data.csv', 'w') as file:
    file.write("Year,No_Smoothing,Lowess(5)\n")
    file.write(csv_data)

print("CSV file 'temperature_data.csv' created successfully.")


data = P.read_csv('temperature_data.csv',
           # field separator character
           sep=",",
           # missing value characters
           #Find invalid values in the data and replace them either with a correct value (if possible) or with NaN.
           na_values=['?'],
           # no row names
           index_col=False,
           # no column names
        
           # quote character
           quotechar='"')

print(data)

# Extract the temperatures (No_Smoothing column)
temperatures = [float(line[1]) for line in data_lines]

# Calculate the mean
mean_temperature = mean(temperatures)

# Calculate the median
median_temperature = median(temperatures)

print(f"Mean temperature: {mean_temperature:.2f}")
print(f"Median temperature: {median_temperature:.2f}")

from scipy import stats

# Perform Shapiro-Wilk test
statistic, p_value = stats.shapiro(temperatures)

# Define a significance level (e.g., 0.05)
alpha = 0.05

# Print the result
if  p_value > alpha:
    print("The distribution can be normal. ")
else:
    print("There's statistical evidence that the distribution is not normal")

years = [int(line[0]) for line in data_lines]
start_year = 2000
filtered_temperatures = [temp for year, temp in zip(years, temperatures) if year >= start_year]

# Perform Shapiro-Wilk test
statistic, p_value = stats.shapiro(filtered_temperatures)

# Define a significance level (e.g., 0.05)
alpha = 0.05

# Print the result
if  p_value > alpha:
    print("The distribution can be normal. ")
else:
    print("There's statistical evidence that the distribution is not normal")
