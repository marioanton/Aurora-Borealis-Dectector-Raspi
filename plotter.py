from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for line in open("data.csv"):
    columns = line.split(',')
    if len(columns) >= 3:

	x = column[1] + Difference
	y = column[2] + Difference
	z = column[3] + Difference
	ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

plt.show()
