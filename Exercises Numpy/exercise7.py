import numpy as np

# Comparison operators

score = np.array([87, 12, 45, 100, 59, 80])

#print(score >= 60)

print(score < 60)

# now i'll change the grades below 60 to zero

score[score < 60] = 0
print(score)


