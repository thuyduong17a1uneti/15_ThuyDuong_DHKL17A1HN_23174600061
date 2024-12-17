import pandas as pd

stocks1 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks1.csv')

print(stocks1.head())
print(stocks1.dtypes)
print(stocks1.info())