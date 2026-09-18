import numpy as np

"""
The next logical step is to set up a series of dimensional arrays.

In the following code i wrote a 2d array a 3x3 columns and rows array.

"""
 
array = np.array([['A','B','C'],
                  ['D','E','F'],
                  ['G','H','I']
])

print(array.ndim, "Dimensions")


print(array[0][0])
print(array[0,0])

"""
now lets try a 3d one

"""


array2 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   
                  [['1','2','3'],['4','5','6'],['7','8','9']],

                  [['!','@','#'],['$','%','^'],['&','*','=']]])

print(array2.ndim, "Dimensions")
print(array2.shape, "Shape")

"""
Chain indexing, does the same but slower

"""
print(array2[0][0])


"""

Multidimensional indexing, does the same but faster, which i will be using for this project

"""
print(array2[0,0,0])


"""
my objetive now is to print

3 * 3 = 9 

"""

word = array2[1,0,2] + ' ' + array2[2,2,1] + ' ' + array2[1,0,2] + ' ' + array2[2,2,2] + ' ' + array2[1,2,2]
print(word)

