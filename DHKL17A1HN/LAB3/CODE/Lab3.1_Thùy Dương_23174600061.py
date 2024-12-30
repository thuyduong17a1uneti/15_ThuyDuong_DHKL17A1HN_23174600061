import pandas as pd

stocks1 = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB2\DATA\stocks1.csv')

print(stocks1.head())
print(stocks1.dtypes)
print(stocks1.info())