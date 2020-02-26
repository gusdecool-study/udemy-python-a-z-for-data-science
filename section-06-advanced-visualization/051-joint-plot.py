import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

cwd = os.getcwd()
file = '/section-06-advanced-visualization/00-movie-ratings.csv'

movies = pd.read_csv(cwd + file)
movies.head()
movies.info()
movies.describe()

# Objective is to change columns "year" to categorical variable.
movies['Film'] = movies['Film'].astype('category')
movies['Genre'] = movies['Genre'].astype('category')
movies['Year of release'] = movies['Year of release'].astype('category')

j = sns.jointplot(data=movies, x='Rotten Tomatoes Ratings %', y='Audience Ratings %', kind='hex')
plt.show()
