

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    suma_a = 0
    suma_b = 0
    k = len(arr) - 1
    for i in range(len(arr)):
        suma_a += arr[i][i]
    for j in range(len(arr)):
        suma_b += arr[j][k]
        k -= 1
    return abs(suma_a - suma_b)
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("n:").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("arr:").rstrip().split())))
    
    print(arr)

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()