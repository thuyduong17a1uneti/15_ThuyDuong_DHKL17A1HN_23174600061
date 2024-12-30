import pandas as pd

stocks1 = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB3\DATA\stocks1.csv')
stocks2 = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB3\DATA\stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

companies = pd.read_csv(r'D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB3\DATA\companies.csv')
print(companies.head())
stocks_companies = pd.merge(stocks, companies, left_on='symbol', right_on='name', how='inner')
company_avg_close = stocks_companies.groupby('name')['close'].mean()
print(company_avg_close.head())