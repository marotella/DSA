#!/bin/python3
### THIS CODE IS NOT OPTIMIZED TO PASS ALL TESTS. NEED TO ACCOUNT FOR LONGER LISTS
import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    # sort array
    arr.sort()
    #create an unfairness variable
    unfairness = float('inf')
    #iterate through the array to build the subarray
    for i in range(len(arr)- (k-1)):
        subarr = arr[i:k+i]
    #find the min and max
        difference = max(subarr)-min(subarr)
    #subtract
    #compare to unfairness
        if difference < unfairness:
            unfairness = difference
    #store
    #return
    return unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
