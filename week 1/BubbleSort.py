#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    leng = len(a)
    swaps = 0
    for i in range(leng):
        swapped = False
        for j in range(leng-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps+=1
                swapped = True
        if swapped == False:
            break
    
    print('Array is sorted in '+ str(swaps)+' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
