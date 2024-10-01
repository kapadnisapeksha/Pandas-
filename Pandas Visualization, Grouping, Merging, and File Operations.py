'''
Pandas Visualization, Grouping, Merging, and File Operations

Write a program which use pandas inbuilt visualization.

Pandas Inbuilt Visualization (a):

Bar Plots: Creates a bar plot for the 'Category' column against 'Values1' and 'Values2'. Save filename as “Barplot”.
Histograms: Generates a histogram for the 'Values1' column. Save filename as “Histogram”.
Line Plots: Creates a line plot for 'Category' against 'Values1' and 'Values2'. Save filename as “Line plot”.
Scatter Plots: Produces a scatter plot for 'Values1' against 'Values2'. Save filename as “Scatter plot”.
Demonstrate use of groupby() method (b):

Creates a new DataFrame (df_groupby) and demonstrates the use of the groupby() method to group data by the 'Category' column and calculate the mean of 'Values' for each category.
Pandas Merging, Joining, and Concatenating (c):

Merging: Combines two DataFrames (df1 and df2) based on the 'ID' column using an outer join and prints the result.
Concatenating: Concatenates two DataFrames (df1 and df2) along the rows and prints the result.
Note:

plt.savefig("filename") saves the generated plots as image files with the specified filename.
Sample input & output:'''
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E', 'E', 'E', 'E', 'E'],
    'Values1': [8, 8, 2, 2, 4, 4, 4, 6, 6, 7, 7, 7, 7, 1],
    'Values2': [7, 7, 4, 4, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
# Bar Plots
df.groupby('Category').plot(kind='bar', figsize=(8, 6))
plt.title('Histogram')
plt.ylabel('Frequency')
plt.savefig("Barplot")

# Histograms
df['Values1'].hist(bins=5)
plt.title('Histogram')
plt.xlabel('Values1')
plt.ylabel('Frequency')
plt.savefig("Histogram")

# Line Plots
df.plot(x='Category', y=['Values1', 'Values2'], kind='line', figsize=(8, 6))
plt.title('Line plot')
plt.xlabel('Category')
plt.ylabel('Values') 
plt.savefig("Line plot")

# Scatter Plots
df.plot.scatter(x='Values1', y='Values2', figsize=(8, 6))
plt.title('Scatter plot')
plt.xlabel('Values1')
plt.ylabel('Values2')
plt.savefig("Scatter plot")

df_groupby = df.groupby('Category').mean()
print(df_groupby)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print(merged_df)

concatenated_df = pd.concat([df1, df2], axis=0)
print(concatenated_df)   
