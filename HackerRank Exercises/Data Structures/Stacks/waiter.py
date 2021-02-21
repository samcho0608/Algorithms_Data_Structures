#!/bin/python3

import os
import sys

#
# Complete the waiter function below.
#
def waiter(number, q):
    answers = []
    b = []
    primes = []
    num = 2
    while len(primes) != q:
        if all(num % i != 0 for i in range(2,num)):
            primes.append(num)
        num += 1
            
    for p in primes:
        a = []
        while number:
            num = number.pop()
            
            if num % p == 0:
                b.append(num)
            else:
                a.append(num)
            
        while b:
            answers.append(b.pop())
            
        number = a
        
    while number:
        answers.append(number.pop())
        
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
