import numpy as np
import matplotlib
matplotlib.use('TkAgg') #for OSX
import matplotlib.pyplot as plt
import seaborn as sns
import copy

msize = 5  # mesh size, square mesh, one side

coeffs = (1.0,-2.0,1.0)
dx = 1.0/float(msize)

def getn(i, j):
    return i * msize + j
    pass


ssize = msize * msize  # stiffness matrix size
# gen. stiffness matrix.
stiffness = [[0.0 for x in range(ssize)] for y in range(ssize)]
source = [0.0 for x in range(ssize)]


# Set Source Vector
# row = 1, colum = 1:msize = 100C
for j in range(0, msize):
    n = getn(0, j)
    source[n] = 100.0
    pass

# print source

# Set Stiffness Matrix
# Outer Boundaries = 1


for i in range(0, 1):
    for j in range(0, msize):
        stiffness[getn(i, j)][j] = 1.0
        pass

for i in range(1, msize):
    for j in range(0, 1):
        n = getn(i, j)
        stiffness[n][n] = 1.0
        pass

for i in range(1, msize):
    for j in range(msize - 1, msize):
        n = getn(i, j)
        stiffness[n][n] = 1.0
        pass

for i in range(msize-1,msize):
    for j in range(0,msize):
        n = getn(i,j)
        stiffness[n][n] = 1.0
        pass


# Inside # for Derivative 2 Accuracy 2

for i in range (1,msize-1):     # select all-
    for j in range(1,msize-1):  # inner nodes

        nr = getn(i,j) # current row of the stiffness  matrix
        #print i,j,n

        for coin in range(-1,2):
            nc = getn(i+coin, j)
            stiffness[nr][nc] += coeffs[coin+1] / pow(dx,2) # += is important :)

        for coin in range(-1,2):
            nc = getn(i, j+coin)
            stiffness[nr][nc] += coeffs[coin+1] / pow(dx,2)

        pass

visual = copy.deepcopy(stiffness) #copy
for i in range(ssize):
    for j in range(ssize):
        if visual[i][j] == 1:
            visual[i][j] = 80.0 #dummy for visualization

#visual of the stiffness matrix
sns.set()
sns.heatmap(visual)
plt.show()
