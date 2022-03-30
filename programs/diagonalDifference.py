"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
Example:
The square matrix array arr is as shown below:

  11 2  3
  4  5  6
  7  8 -9

the sum of left-to-right diagonal 11+5-9=7, and that of right-to-left diagonal 3+5+7= 15. There absolute difference is |7-15|= 8

"""


import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    size = len(arr)
    sumLeftDig = 0
    sumRightDig = 0
    for i in range(size):
        sumLeftDig+=arr[i][i]
        sumRightDig+=arr[i][size-i-1]
    return abs(sumLeftDig - sumRightDig)
    

result = diagonalDifference([[11,2,3],[4,5,6],[7,8,-9]])
print(result)
