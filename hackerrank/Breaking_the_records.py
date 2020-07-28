import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    count_best = 0
    count_worst = 0
    for i in scores[1:]:
        if best < i:
            best = i
            count_best += 1
        elif worst > i:
            worst = i
            count_worst += 1
    print(f"{count_best} {count_worst}")




if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

