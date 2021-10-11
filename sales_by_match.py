#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sum:int = 0
    checked:list[int] = []
    for i in range(n):
        if(not (ar[i] in checked)):
            count:int = 1
            for j in range(n - (i+1)):
                if(ar[i] == ar[j + (i+1)]):
                    count = count + 1
            sum = sum + math.floor(count/2)    
        checked.append(ar[i])
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
