import pandas as pd
pd.set_option('display.max_columns', None)
data  = pd.read_csv('growth.csv')
data = pd.drop("Indicator Name",axis=1)
data = pd.drop("Indicator Code",axis=1)
print(data.head())