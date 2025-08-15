# p6b_compare.py
"""
Script to compare the random splitter and middle splitter for computing the 
median in Project 6 Part B
"""
import matplotlib.pyplot as plt
import numpy as np
import time
from p6b import select_r, select_m

# Generate test data:  a set of vectors of varying lengths
#   (a vector is a 1D array)
powers= np.array(range(2,6))
lengths= 10**powers + 1  # The different vector lengths to use
                         #   Use odd lengths for simplicity
num_powers= len(powers)  # How many different lengths
num_vectors= 100         # How many vectors of each length to use
# There will be num_powers * num_vectors random vectors of varying lengths
data= []
for b in range(num_powers):
    innerlis= []
    for c in range(num_vectors):
        innerlis.append(np.random.random_sample(lengths[b]))
    data.append(innerlis)
    # data is a nested list of vectors
    # data[b][c] is a random vector of length lengths[b]
###############################################################
# TODO: Modify the ABOVE block of code such that four vector
#       lengths are used in this script, as stated in the 
#       project description.
# Hint: You need to change only one line of code.
###############################################################
    
# Run both algorithms using the same test data
time_r= np.zeros(num_powers)  # computation time using random splitter
time_m= np.zeros(num_powers)  # computation time using middle splitter

for b in range(num_powers):
    kth_index= int(lengths[b]/2) # Index for 50th percentile value (median)
                                 # The 2nd arg to the select_r, select_m calls
    # Time the random splitter approach
    tstart= time.time()  # current time in seconds
    for vec in data[b]:
        med_r= select_r(vec, kth_index)
    tstop= time.time()
    time_r[b]= tstop - tstart
    
    # Time the middle splitter approach
    tstart= time.time()
    for vec in data[b]:
        med_m= select_m(vec, kth_index)
    tstop= time.time()
    time_m[b]= tstop - tstart
    
# Plot time vs length of vector for both approaches on one set of axes
# (i.e., plot two curves within the same set of axes)
plt.plot(lengths, time_r/num_vectors, 'b-o',  
         lengths, time_m/num_vectors, 'm-d') 
plt.title('Average time to compute the median value') 
plt.xlabel('Size of data') 
plt.ylabel('Time in seconds') 
plt.legend(['Random splitter', 'Middle splitter'])
plt.show()

###############################################################
# TODO: Add a comment below to answer the two questions asked
#       on the last page of the project description. 
###############################################################
# Q1: 
# I think the middle splitter is better because it takes it consistently takes less time as the size of the data increases. 
#In addition, it's more predictable because it always splits the list into roughly equal halves unlike the random splitter that creates unbalanced partitions and therefore lead to slower performace on avg.

# Q2: 
#I think plt.log is best especially for larger data because it compresses larger values. 
#Therefore, it makes it easier to compare the growth for large data.

