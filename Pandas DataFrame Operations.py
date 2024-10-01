'''
Pandas DataFrame Operations

Write a program to perform the following operations on the dataframe.

         a) Retrieve a particular column from the DataFrame
         b) Summarize the data frame and observe the statistics of the DataFrame created
         c) Observe the mean and standard deviation of the data frame and print the values.
Dataframe:
data = { 'Name': ['John', 'Alice', 'Bob', 'Eva', 'Charlie'],
                 'Age': [25, 28, 22, 30, 35],
                 'Salary': [50000, 60000, 45000, 70000, 80000],
                 'Rating': [4.5, 3.8, 4.2, 4.9, 3.5],
                 'Experience': [2, 4, 1, 6, 5] }

Input Format:
 Users will be prompted to enter the column name for retrieval.

Output Format:
a) Retrieved Column: The values of the retrieved column are printed.
b) Summary Statistics of DataFrame - Descriptive statistics (count, mean, std, min, 25%, 50%, 75%, max) are printed.
c) Mean and Standard Deviation of DataFrame -Mean and standard deviation values for each column are printed.

Sample Input and Output:
Enter the column name for retrieval:
Age
 Retrieved Column ('Age'):
0    25
1    28
2    22
3    30
4    35
Name: Age, dtype: int64

 Summary Statistics of DataFrame:
             Age        Salary    Rating  Experience
count   5.000000      5.000000  5.000000    5.000000
mean   28.000000  61000.000000  4.180000    3.600000
std     4.949747  14317.821063  0.554076    2.073644
min    22.000000  45000.000000  3.500000    1.000000
25%    25.000000  50000.000000  3.800000    2.000000
50%    28.000000  60000.000000  4.200000    4.000000
75%    30.000000  70000.000000  4.500000    5.000000
max    35.000000  80000.000000  4.900000    6.000000

 Mean of the DataFrame:
Age              28.00
Salary        61000.00
Rating            4.18
Experience        3.60
dtype: float64

Standard Deviation of the DataFrame:
Age               4.949747
Salary        14317.821063
Rating            0.554076
Experience        2.073644
dtype: float64'''
import pandas as pd 
import numpy as np 
df = { 'Name': ['John', 'Alice', 'Bob', 'Eva', 'Charlie'],
                 'Age': [25, 28, 22, 30, 35],
                 'Salary': [50000, 60000, 45000, 70000, 80000],
                 'Rating': [4.5, 3.8, 4.2, 4.9, 3.5],
                 'Experience': [2, 4, 1, 6, 5] }
data=pd.DataFrame(df)
retrival_col=input("Enter the column name for retrieval:")
col=data[retrival_col]
print("  Retrieved Column ('Age'):")
print(col)
print(" Summary Statistics of DataFrame:")
summary=data.describe()
print(summary)
mean_dat=data.mean()
print(" Mean of the DataFrame:")
print(mean_dat)
sta_dev=data.std()
print("Standard Deviation of the DataFrame:")
print(sta_dev)