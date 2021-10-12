import numpy as np
h1_column=[1, 0, -1]
h2_row=[1,2,1]
x = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0], ])
## pad x to simplify the procedure
x_padding =np.pad(x,((2,2),(0,0)),'constant', constant_values=(0,0))
## x convolve with h1_column, r1[m,n] represent the current compute point.
r1 = np.zeros((9,7), dtype = np.int)
for n in range(0, 7):
 for m in range(0, 9):
  for i in range(0, 3):
    r1[m,n]= r1[m,n] + h1_column[i]*x_padding[m+i][n]
print(r1)


## r1 convolved with h2_row, r2[m,n] represent the result.
r2 = np.zeros((9,9), dtype = np.int)
## pad x to simplify the procedure
x_padding2 =np.pad(r1,((0,0),(2,2)),'constant', constant_values=(0,0))
for m in range(0, 9):
 for n in range(0, 9):
  for i in range(0, 3):
      r2[m,n]= r2[m,n] + h1_column[i]*x_padding2[m][n+i]
print(r2)


