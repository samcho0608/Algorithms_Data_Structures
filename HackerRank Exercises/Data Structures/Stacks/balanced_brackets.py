#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for i in range(1,len(s)+1):
        bracket = s[-i]
        if bracket in [']','}',')']:
            stack.append(bracket)
        else:
            if not stack:
                return 'NO'
            r = stack.pop()
            if bracket + r not in ['()', '{}', '[]']:
                return 'NO'
    return 'YES' if not stack else 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
