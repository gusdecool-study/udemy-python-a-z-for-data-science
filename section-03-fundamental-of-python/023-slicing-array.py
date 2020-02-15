import numpy as np

a = np.array([23456, 27, 546, 444, 555])
b = a[0:2]  # this is a reference in numpy
b[:] = 111

# examine "a" first two values is changed to "111"
