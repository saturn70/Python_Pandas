# pip install pandas
# Import Libraries
import numpy as np
import pandas as pd
# Load Data
df=pd.read_csv('https://raw.githubusercontent.com/saturn70/Python_Pandas/main/tips.csv')
print(df)
# Print first five rows
print(df.head())
# Print last five rows
print(df.tail())
