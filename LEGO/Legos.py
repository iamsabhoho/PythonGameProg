# library for scientific computations
import numpy as np
#library for graphs
import matplotlib.pyplot as plt

# read text file
legos = np.loadtxt('Legos.txt',delimiter=',')

# show the number of elements in legos
len(legos)

# show the dimensions of legos (# of rows, # columns)
np.shape(legos)

# show every pair of points
for x, y in legos:
    print(x,y)

# print each pair of points in a scatter plot
for x, y in legos:
    plt.scatter(x,y,color='gray')
plt.show()

