import numpy as np

# # Broadcasting is basically performing operations between different dimensions arrays.

# # they can only be compatible if the columns and rows are either: exactly the same amount or 1.

# array1 = np.array([[1,2,3,4]])

# array2 = np.array([[1], [2], [3], [4]])

# print(array1.shape)
# print(array1.imag)

# print(array2.shape)
# print(array2.imag)


array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])

array2 = np.array([[1], [2], [3], [4], [5], [6], [6], [8], [9], [10]])

print(array1 * array2)

