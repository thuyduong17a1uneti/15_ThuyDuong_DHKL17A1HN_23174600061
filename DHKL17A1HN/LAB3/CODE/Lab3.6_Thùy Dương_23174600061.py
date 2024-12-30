import pandas as pd

stocks1 = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB2\DATA\stocks1.csv')
stocks2 = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB3\DATA\stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')
volume_total = stocks.groupby('symbol')['volume'].sum()
pivot_table['volume'] = pivot_table.columns.map(volume_total)
pivot_table_sorted = pivot_table.sort_values(by='volume', ascending=False)
print(pivot_table_sorted.head())