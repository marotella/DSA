#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    #determine the size of the matrix
    n = len(matrix)
    sub_matrix = n // 2 
    #half the matrix
    sum = 0
    for i in range(sub_matrix):
        for j in range(sub_matrix):
            max_num = max(matrix[i][j], matrix[i][n-1-j], matrix[n-1-i][j], matrix[n-1-i][n-1-j])
            sum += max_num
            
    return sum
    
