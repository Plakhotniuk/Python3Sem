import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=2)

ejudge = pd.read_html('students/results_ejudge.html', index_col=0)[0]
students = pd.read_excel('students/students_info.xlsx')

plot1 = pd.DataFrame({'Mean number of solved problems':
                    [ejudge.loc[(ejudge['User'].isin(students.loc[(students['group_faculty'] == i),
                    'login']))]['Solved'].mean() for i in students['group_faculty'].unique()]},
                     index=students['group_faculty'].unique())
print(plot1)
plot1.plot.bar(ax=axes[0], fontsize=12, figsize=(10, 8),
               title='Mean number of solved problems\nby group faculty', legend=False)
plot2 = pd.DataFrame({'Mean number of solved problems':
                    [ejudge.loc[(ejudge['User'].isin(students.loc[(students['group_out'] == i),
                    'login']))]['Solved'].mean() for i in students['group_out'].unique()]},
                     index=students['group_out'].unique())

plot2.plot.bar(ax=axes[1], fontsize=12, figsize=(10, 8),
               title='Mean number of solved problems\nby group out', legend=False)

plt.savefig('Mean number of solved problems.png')
plt.show()
