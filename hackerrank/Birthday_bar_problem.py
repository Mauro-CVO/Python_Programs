import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    combination = len(s) - m + 1
    for i in range(combination):
        arr = s[i : i + m]
        num = 0
        for j in arr:
            num += j
        if num == d:
            count += 1
        else:
            continue
    print(count)


    return sum([])
if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

