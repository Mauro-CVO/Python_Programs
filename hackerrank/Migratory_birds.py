
import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    list_max = [0,]
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for x in arr:
        if x == 1:
            count_1 += 1
        elif x == 2:
            count_2 += 1
        elif x == 3:
            count_3 += 1
        elif x == 4:
            count_4 += 1
        else:
            count_5 += 1
    list_max.insert(1,count_1)
    list_max.insert(2,count_2)
    list_max.insert(3,count_3)
    list_max.insert(4,count_4)
    list_max.insert(5,count_5)
    print(list_max.index(max(list_max)))


    

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
