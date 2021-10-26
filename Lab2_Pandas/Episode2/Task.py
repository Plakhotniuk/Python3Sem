import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=3)

data = pd.read_csv('flights.csv', index_col=0)
data.reset_index()
print(data)
newdata = pd.DataFrame({'Total flights': [len(data.apply(lambda x: True if x[0] == i else False, axis=1)
                                              [data.apply(lambda x: True if x[0] == i else False, axis=1)
                                               == True].index) for i in data['CARGO'].unique()],
                        'Total cost': [data.loc[(data['CARGO'] == i), 'PRICE'].sum() for i in data['CARGO'].unique()],
                        'Total weight': [data.loc[(data['CARGO'] == i), 'WEIGHT'].sum() for i in data['CARGO'].unique()]},
                       index=data['CARGO'].unique())
print(newdata)
for i in newdata.columns:
    newdata[i].plot.bar(ax=axes[list(newdata.columns).index(i)],
                        fontsize=12, figsize=(10, 8), title=i, color=['r', 'g', 'b'])
    axes[list(newdata.columns).index(i)].title.set_size(15)

fig1.tight_layout(pad=1.0)
plt.savefig('flight_companies_report.png')
plt.show()
