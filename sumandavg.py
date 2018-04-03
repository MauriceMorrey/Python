
#import numpy as np
a = [1, 2, 5, 10, 255, 3]
print sum(a)#prints sum of a
#print np.mean(a)#mean gives the average

print sum(a,0.0) / len(a)#gives more exact float result for the average

# Print odd numbers from 1 to 1000
# Iterate from 1 to 1000 with skip value of 2 and print the current value
for i in range (1, 1000, 2):
    print i


# Print all the multiples of 5 from 5 to 1,000,000
# Iterate from 5 to 1000001 with a skip value of 5 and print the current value
for i in range (5, 1000001, 5):
    print i

