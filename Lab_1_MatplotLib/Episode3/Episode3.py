import pandas as pd
import matplotlib.pyplot as plt

fig1, axes = plt.subplots(nrows = 4, ncols = 2)

data = pd.read_csv('students.csv', sep='[;,|_]', engine='python')

data.columns = ['Preps', 'Groups', 'Marks']

j, k = 0, 0
for i in data['Preps'].unique():
    new_data = data.loc[data.Preps.isin([i])]['Marks'].value_counts().sort_index().to_frame()
    print(new_data)
    new_data.plot.pie(y='Marks', figsize=(8, 8), ax=axes[j, k], autopct='%1.0f%%', shadow=True,
                      startangle=90, legend=False, fontsize=8, title=i)
    axes[j, k].title.set_size(10)
    if not k:
        k+=1
    else:
        j +=1
        k = 0

fig1.delaxes(axes[3][1])
fig1.tight_layout(pad=1.0)
plt.savefig('Marks_per_prep.png')
plt.show()
