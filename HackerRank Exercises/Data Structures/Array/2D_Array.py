import math
import os
import random
import re
import sys

def hourglassSummation(arr, x, y):
    
    return sum([arr[x+i][y+j] for i in range(3) for j in range(3) if (i,j) != (1,0) and (i,j) != (1,2)])

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # 0,0 0,1 0,2
    #     1,1
    # 2,0 2,1 2,2
    max_sum = hourglassSummation(arr,0,0)
    for x in range(4):
        for y in range(4):
            curr_sum = hourglassSummation(arr,x,y)
            if curr_sum > max_sum:
                max_sum = curr_sum
                
                
    return max_sum
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
