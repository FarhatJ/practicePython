"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Example:
arr = [1,1,0,-1,-1]
There are n = 5 elements in the array arr, two positive, two negetive and one zero.
Their ratios are 2/5 = 0.400000, 2/5=0.400000 and 1/5=0.200000
the output should be:
0.400000
0.400000
0.200000

"""

import math
import os
import random
import re
import sys


def plusMinus(arr):
    size = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in range(size):
        if arr[i] > 0:
            pos+=1
        elif arr[i] < 0:
            neg+=1
        else:
            zero+=1
    print(format(pos/size, '.6f') + "\n" + format(neg/size, '.6f') + "\n" + format(zero/size, '.6f'))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
