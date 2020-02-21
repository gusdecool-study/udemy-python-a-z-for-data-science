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

