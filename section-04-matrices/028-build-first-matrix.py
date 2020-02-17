import numpy as np

mydata = np.arange(0, 20)
reshape_a = np.reshape(mydata, (5, 4))
reshape_b = np.reshape(mydata, (5, 4), order='C')
reshape_c = np.reshape(mydata, (5, 4), order='F')

# Exercise to get number 10
print(reshape_a[2, 2])

# Numpy Array
r1 = ['I', 'am', 'happy']
r2 = ['What', 'a', 'day']
r3 = [1, 2, 3]

foo1 = [r1, r2, r3]
foo2 = np.array([r1, r2, r3])
