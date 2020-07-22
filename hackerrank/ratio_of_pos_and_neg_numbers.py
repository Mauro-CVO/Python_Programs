import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    ratio = (len(arr))
    for i in arr:
        if i == 0:
            zero += 1
        elif i < 0:
            neg += 1
        else:
            pos += 1
    print(pos/ratio)
    print(neg/ratio) 
    print(zero/ratio)

if __name__ == '__main__':
    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))
    arr = [1, -1, 0]

    plusMinus(arr)
