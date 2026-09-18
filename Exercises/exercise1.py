import numpy as np

""" 

i am choosing numpy because it's faster than raw python, for instance:

The following code demonstrates how numpy actually doubles the info inside the variable
and how pure python simply adds a copy of the numbers after it.

"""

array = np.array([1,2,3,4])
array *= 2
print(array)
print(len(array))

arrayp = [1,2,3,4,]

arrayp *= 2
print(arrayp)
print(len(arrayp))
