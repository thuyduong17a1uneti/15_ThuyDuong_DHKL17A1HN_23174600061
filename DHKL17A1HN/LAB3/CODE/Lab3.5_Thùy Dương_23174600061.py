import pandas as pd

stocks1 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks1.csv')
stocks2 = pd.read_csv(r'D:\DHKL17A1HN\LAB3\DATA\stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

stocks.set_index(['date', 'symbol'], inplace=True)
stocks_grouped = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close', 'volume']].mean()
stocks_grouped.sort_index(inplace=True)
print(stocks_grouped.head())
