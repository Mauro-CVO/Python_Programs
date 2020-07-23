import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_house = 0
    oranges_house = 0

    for x in apples:
        if x + a >= s and x + a <= t:
            apples_house += 1
        else:
            continue
    print(apples_house)

    for y in oranges:
        if y + a >= s and y + a <= t:
            oranges_house += 1
        else:
            continue
    print(oranges_house)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)