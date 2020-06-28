''' Problema que resolvi no site hackerrank.com '''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    tam = len(arr)
    pos = 0.000000
    neg = 0.000000
    zer = 0.000000

    for i in range(tam):
        # print("i:",i,"arr[i]:",arr[i],"pos:",pos,"neg:",neg,"zer:",zer)
        if(arr[i] < 0):
            neg += 1
        elif(arr[i] > 0):
            pos += 1
        else:
            zer += 1
    # print(tam, pos, neg, zer)
    # print(arr)
    a = format(float(pos/tam), '.6f')
    b = format(float(neg/tam), '.6f')
    c = format(float(zer/tam), '.6f')
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)