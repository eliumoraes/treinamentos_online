''' Problema que resolvi no site hackerrank.com '''
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = s[8:]
    if(t=='PM'):
        h = str(int(s[:2]) + 12)
        h = h if (h != '24') else '12'

    else:
        h = str(int(s[:2])).zfill(2)
        h = h if (h != '12') else '00'

    m = str(int(s[3:5])).zfill(2)
    s = str(int(s[6:8])).zfill(2)

    return(h+':'+m+':'+s)

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'saida.txt'
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()