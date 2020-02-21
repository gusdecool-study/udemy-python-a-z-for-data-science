import os
import pandas as pd

cwd = os.getcwd()
file = '/section-05-data-frames/00-demographic-data.csv'

csv = pd.read_csv(cwd + file)
