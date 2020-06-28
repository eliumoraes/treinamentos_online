''' Problema que resolvi no site hackerrank.com '''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces = ' ' * (n-1)
    step = '#'
    for i in range(n):
        print(spaces + step)
        spaces = spaces[:-1]
        step = step + '#'


if __name__ == '__main__':
    n = int(input())

    staircase(n)