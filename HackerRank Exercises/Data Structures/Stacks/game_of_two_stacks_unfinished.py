#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#

def twoStacks(x, a, b):
    la, lb = [a[0]],[b[0]]
    del a[0]
    del b[0]
    
    while a or b:
        if a:
            la.append(a[0] + la[-1])
            del a[0]
        if b:
            lb.append(b[0] + lb[-1])
            del b[0]
       
    max_count = 0
    while la and lb:
        if la[-1] > x:
            la.pop()
        if lb[-1] > x:
            lb.pop()
            
        if not la or not lb or la[-1] <= x and lb[-1] <= x:
            max_count = max(len(la), len(lb))
            break
    
    if bool(la) ^ bool(lb):
        return max(len(la), len(lb))
    
    while la and lb:
        la.pop() if la[-1] > lb[-1] else lb.pop()
        if len(la) + len(lb) <= max_count:
            return max_count
        if la[-1] + lb[-1] <= x:
            return max(len(la) + len(lb), max_count)
        
            
            
            
    

if __name__ == '__main__':
    inputfile = open('input.txt', 'r')
    g = int(inputfile.readline())

    for g_itr in range(g):
        nmx = inputfile.readline().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, inputfile.readline().rstrip().split()))

        b = list(map(int, inputfile.readline().rstrip().split()))

        result = twoStacks(x, a, b)

        print(result)

    inputfile.close()
