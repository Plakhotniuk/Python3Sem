import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=3)

data = pd.read_csv('flights.csv', index_col=0)
data.reset_index()

newdata = data.groupby('CARGO').sum()
newdata['COUNTS'] = data.groupby('CARGO').count()['PRICE'].values
print(newdata)

for i in newdata.columns:
    newdata[i].plot.bar(ax=axes[list(newdata.columns).index(i)],
                        fontsize=12, figsize=(10, 8), title=i, color=['r', 'g', 'b'])
    axes[list(newdata.columns).index(i)].title.set_size(15)

fig1.tight_layout(pad=1.0)
plt.savefig('flight_companies_report.png')
plt.show()
