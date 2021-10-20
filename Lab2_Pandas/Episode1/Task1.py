import pandas as pd
data = pd.read_csv('transactions.csv.webarchive', index_col=0)
data.reset_index()
[print(data.loc[data['STATUS'] == 'OK'].sort_values(by=['SUM'], ascending=False)['SUM'].iloc[i]) for i in range(3)]