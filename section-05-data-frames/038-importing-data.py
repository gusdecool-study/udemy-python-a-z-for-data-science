import os
import pandas as pd

cwd = os.getcwd()
file = '/section-05-data-frames/00-demographic-data.csv'

csv = pd.read_csv(cwd + file)

# 2. number of rows
print(len(csv))

# 3. see columns
print(csv.columns)

# 4. number of columns
print(len(csv.columns))

# 5. top rows
print(csv.head())

# 6. bottom rows
print(csv.tail())

# 7. information on the columns
print(csv.info())

# 8. get stats of the columns
print(csv.describe())
print(csv.describe().transpose())

# -------------------------------------------------------------------------------------------------
# 041. sub-setting panda
# -------------------------------------------------------------------------------------------------

# Part 1. Rows
print(csv[21:26])

# Get some part
print(csv[['Country Name', 'Birth rate']].head())

# Combining the two
print(csv[2:8][['Country Name', 'Birth rate']])

# -------------------------------------------------------------------------------------------------
# 042. basic operation
# -------------------------------------------------------------------------------------------------

# Math
result = csv['Birth rate'] * csv['Internet users']
print(result.head())

# Add Column
csv['MyResult'] = result
print(csv.head())

# Delete column
csv.drop(columns='MyResult')
print(csv.head())

# -------------------------------------------------------------------------------------------------
# 043. Filtering data frames
# -------------------------------------------------------------------------------------------------

# normal filter
filterInternetUsers = csv['Internet users'] < 2
filterBirthRate = csv['Birth rate'] > 40
filteredCsv = csv[filterInternetUsers]

# combined filters
combinedFilter = filterInternetUsers & filterBirthRate
combinedFilteredCsv = csv[combinedFilter]

# string filter
highIncomeFilter = csv['Income Group'] == 'High income'

# Get unique values
uniqueValue = csv['Income Group'].unique()

# -------------------------------------------------------------------------------------------------
# 044. .at() & .iat()
# -------------------------------------------------------------------------------------------------

print(csv.iat[3, 4])  # Get from index at 3 and column 4
print(csv.at[3, 'Income Group'])  # Get from label at 3 and column 'Income Group'
