import pandas as pd
data = pd.read_csv('transactions.csv.webarchive', index_col=0)
data.reset_index()
[print(i) for i in data.loc[data['STATUS'] == 'OK'].sort_values(by=['SUM'], ascending=False)['SUM'].iloc[0:3].values]
