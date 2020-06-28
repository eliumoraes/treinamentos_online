''' Problema que resolvi no site hackerrank.com '''
#!/bin/python3

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
    tam = len(arr)
    dp = 0
    ds = 0
    a = 0
    b = tam - 1
    for i in range(tam):
        dp = arr[i][a] + dp
        ds = arr[i][b] + ds
        a += 1
        b -= 1
    return abs(dp - ds)


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'saida.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
