import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    ar.sort()
    i = 0
    j = 1
    print(ar)
    while i < len(ar) - 1:
        print(f"{ar[i]} + {ar[j]} % k = {(ar[i] + ar[j]) % k}")
        if (ar[i] + ar[j]) % k == 0:
            count += 1
            print(f"counts = {count}")
        j += 1
        print(f"i = {i}")
        print(f"j = {j}")
        if j == len(ar): #- 1:
            i += 1
            j = i + 1
        # elif j == len(ar):
        #     break
        
    print(count)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)