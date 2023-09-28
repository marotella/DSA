#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Calculate turns if starting from the beginning
    turns_from_start = p // 2

    # Calculate turns if starting from the end
    turns_from_end = (n // 2) - (p // 2)

    # Return the minimum of the two possibilities
    return min(turns_from_start, turns_from_end)

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()