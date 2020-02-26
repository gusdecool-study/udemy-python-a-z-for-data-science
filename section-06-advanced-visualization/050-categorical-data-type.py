import os
import pandas as pd

cwd = os.getcwd()
file = '/section-06-advanced-visualization/00-movie-ratings.csv'

csv = pd.read_csv(cwd + file)
csv.head()
csv.info()
csv.describe()

# Objective is to change columns "year" to categorical variable.
csv['Film'] = csv['Film'].astype('category')
csv['Genre'] = csv['Genre'].astype('category')
csv['Year of release'] = csv['Year of release'].astype('category')

csv['Genre'].cat.categories
