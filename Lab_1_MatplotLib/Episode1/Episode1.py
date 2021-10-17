import matplotlib.pyplot as plt
for i in range(1, 6):
    with open('00' + str(i) + '.dat', 'r') as line:
        b = [float(i) for i in line.read().split()]
        x = b[1:2 * int(b[0]):2]
        y = b[2:2 * int(b[0]) + 1:2]
        if len(x) > 100:
            print(x)
            plot = plt.scatter(x, y, marker='.', s=3)
        else:
            plot = plt.scatter(x, y, marker='.', s=10)
        plt.title('Number of points:' + str(len(x)))
        plt.axis('scaled')
        plt.savefig('00' + str(i) + '.png')
        plt.cla()
