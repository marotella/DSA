
# PrepareInterview Preparation Kits1 Month Preparation KitWeek 1Subarray Division 1
# Exit Full Screen View
# Problem	Submissions	Leaderboard	Discussions	Editorial
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.
# Example 
 
 

# Lily wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .
# Function Description
# Complete the birthday function in the editor below.
# birthday has the following parameter(s):
# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month
# Returns
# int: the number of ways the bar can be divided
# Input Format
# The first line contains an integer , the number of squares in the chocolate bar. 
# The second line contains  space-separated integers , the numbers on the chocolate squares where . 
# The third line contains two space-separated integers, and , Ron's birth day and his birth month.
# Constraints

# , where ()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    #make a counter
    counter = 0
    #iterate over the length of the string
    for i in range(len(s)-m+1): # -m + 1 to make sure the section is the right length
        sum = 0
        for j in range(i, i+m):
            sum += s[j]
        if sum == d:
            counter += 1
    return counter
            
    #sum the indexes in that range
    # check if it is equal to the day
    # if it is increate the counter
    # iterate
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()