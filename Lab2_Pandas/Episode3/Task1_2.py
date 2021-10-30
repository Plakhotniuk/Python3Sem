import matplotlib.pyplot as plt
import pandas as pd

fig1, axes = plt.subplots(nrows=1, ncols=2)

ejudge = pd.read_html('students/results_ejudge.html', index_col=0)[0]
students = pd.read_excel('students/students_info.xlsx')
good_results = ejudge.loc[(ejudge['H'] > 10) | (ejudge['H'] > 10)]
plot1 = pd.DataFrame({"number of students": students.loc[students['login'].
                   isin(good_results['User'])]['group_faculty'].value_counts().values},
                     index=students.loc[students['login'].isin(good_results['User'])]['group_faculty'].
                   value_counts().index)
plot1.plot.bar(ax=axes[0], fontsize=12, figsize=(10, 8),
               title='Number of people \nfrom group faculty', legend=False)
plot2 = pd.DataFrame({"number of students": students.loc[students['login'].
                   isin(good_results['User'])]['group_out'].value_counts().values},
                     index=students.loc[students['login'].isin(good_results['User'])]['group_out'].
                   value_counts().index)
plot2.plot.bar(ax=axes[1], fontsize=12, figsize=(10, 8),
               title='Number of people \nfrom group out', legend=False)
plt.savefig('Number of students how passed tests in last problems.png')
plt.show()
