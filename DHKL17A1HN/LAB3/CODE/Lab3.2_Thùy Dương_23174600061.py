import pandas as pd

stocks1 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks1.csv')

print(stocks1.isnull().sum())
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)
print(stocks1.isnull().sum())