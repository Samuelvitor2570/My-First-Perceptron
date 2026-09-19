import numpy as np


array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])





# array[start:end:step]
# in the cave above, we have the setup of
# start - which most of the time is 0, as computers tend to save 0 as the first one
# end - it's the end of search for instance i'll print in the screen every data that's between the middle ones
# step : this is the "do" of the loop
# in the next line i'm creating a loop, it starts at 0 ends at 4 and iterates from 9 to 9
#print (array[0:4:9])


#prints the last one, if i were to print -2 it would send the second to last and so on.
#print(array[-2])

# negative steps prints all lists in reverse, because it's reading every item
# one time per loop in reverse
#print(array[::-1])

# the same happens here, but 2 items per loop this time, the same would happen with bigger numbers and so on
#print(array[::-2])

# what if i wanted to print out every number from the same column

print(array[:, 0,])

