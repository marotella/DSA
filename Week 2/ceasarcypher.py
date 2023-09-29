#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = ""
    for letter in s:
        if letter in alpha_lower:
            index = alpha_lower.index(letter)
            new_index = (index + k) %26
            encoded += alpha_lower[new_index]
        elif letter in alpha_upper:
           index = alpha_upper.index(letter)
           new_index = (index + k) % 26
           encoded += alpha_upper[new_index]
        else:
            encoded += letter
    return encoded
     
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()