import numpy as np
def oneD_convolution(numpyObject1, numpyObject2):
 if (type(numpyObject1) is np.ndarray) & (type(numpyObject2) is np.ndarray):
   numpyObject2 = numpyObject2[::-1]
   out=np.zeros((len(numpyObject1)+len(numpyObject2)-1,), dtype = np.int)
 for i in range(0, len(out)):
   start = (i - len(numpyObject2) + 1) if (i - len(numpyObject2) + 1)>0 else 0

 for j in range(start, i+1):
  if j < len(numpyObject1):
    k = len(numpyObject2) - (i + 1 - start) + (j - start)
    out[i] = out[i] + numpyObject1[j]*numpyObject2[k]
    return out
  else:
     print("not type of numpy")
 return 0

x = np.array([1, 1, 3, 5, 3, 1, 1])
h1 = np.array([1, -1])
h2 = np.array([-2, -1])
y1 = oneD_convolution(x, h1) + oneD_convolution(x, h2)
print(y1)
y2 = oneD_convolution(oneD_convolution(x, h1), h2)
print(y2)
