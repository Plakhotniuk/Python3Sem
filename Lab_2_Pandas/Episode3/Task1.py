import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=2)

ejudge = pd.read_html('students/results_ejudge.html', index_col=0)[0]
students = pd.read_excel('students/students_info.xlsx')

newdata = students.merge(ejudge, how='inner', left_on='login', right_on='User')

newdata[['group_faculty', 'Solved']].groupby('group_faculty').\
    mean().plot(kind='bar', rot=0, ax=axes[0],
                title='Mean number of solved\nproblems by group faculty', fontsize=8, legend=False)
newdata[['group_out', 'Solved']].groupby('group_out').\
    mean().plot(kind='bar', rot=0, ax=axes[1],
                title='Mean number of solved\nproblems by group out', legend=False)

plt.savefig('Mean number of solved problems.png')
plt.show()
