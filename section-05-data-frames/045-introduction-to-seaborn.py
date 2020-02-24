# -------------------------------------------------------------------------------------------------
# 045. Introduction to Seaborn
# -------------------------------------------------------------------------------------------------

import os
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

cwd = os.getcwd()
file = '/section-05-data-frames/00-demographic-data.csv'

csv = pd.read_csv(cwd + file)

plt.rcParams['figure.figsize'] = 8,4

# distplot
visual1 = sns.distplot(csv['Internet users'], bins=30)
plt.show()

# boxplot
visual2 = sns.boxplot(data=csv, x='Income Group', y='Birth rate')
plt.show()

# Linear model plot
visual3 = sns.lmplot(data=csv, x='Internet users', y='Birth rate')
plt.show()
