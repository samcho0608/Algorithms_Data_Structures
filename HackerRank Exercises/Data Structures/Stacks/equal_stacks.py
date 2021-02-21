#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    if not all([h1,h2,h3]):
        return len(h1) + len(h2) + len(h3)
    
    for i in (h1, h2, h3):
        i.reverse()
        
    heights = [sum(h1), sum(h2), sum(h3)]
    while len(set(heights)) != 1:
        tallest_index = heights.index(max(heights))
        tallest = [h1,h2,h3][tallest_index]
        heights[tallest_index] -= tallest.pop()
    
    return heights[0]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
