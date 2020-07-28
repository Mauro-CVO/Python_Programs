import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
from math import gcd

def getTotalX(a, b):
    count = 0
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i/ gcd(lcm, i)
    for j in b:
        if j % lcm == 0:
            count += 1
        else:
            continue
    print(count)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)