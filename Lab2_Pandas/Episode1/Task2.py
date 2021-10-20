import pandas as pd
data = pd.read_csv('transactions.csv.webarchive', index_col=0)
data.reset_index()
print(data.loc[(data['CONTRACTOR'] == 'Umbrella, Inc') & (data['STATUS'] == 'OK'), 'SUM'].sum())
