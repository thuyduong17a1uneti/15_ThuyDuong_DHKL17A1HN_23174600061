import pandas as pd

stocks1 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks1.csv')
stocks2 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

stocks_avg = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
print(stocks_avg.head())