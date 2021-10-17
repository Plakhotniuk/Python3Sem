import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 155, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots(nrows = 3, ncols = 2)
ax1[0][0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f',
        shadow=True, startangle=90)
ax1[0][0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1[0][0].set(title='sosi')
plt.show()