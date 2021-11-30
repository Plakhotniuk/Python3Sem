import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=2)

ejudge = pd.read_html('students/results_ejudge.html', index_col=0)[0]
students = pd.read_excel('students/students_info.xlsx')
newdata = students.merge(ejudge, how='inner', left_on='login', right_on='User')
good_results = newdata.loc[(newdata['H'] > 10) | (newdata['G'] > 10)]
good_results[['group_out', 'group_faculty']].groupby('group_out').count().\
    plot(kind='bar', rot=0, ax=axes[0],
    title='Number of people \nfrom group faculty', fontsize=8, legend=False)

good_results[['group_out', 'group_faculty']].groupby('group_faculty').count().\
    plot(kind='bar', rot=0, ax=axes[1],
    title='Number of people \nfrom group out', fontsize=8, legend=False)

plt.show()
