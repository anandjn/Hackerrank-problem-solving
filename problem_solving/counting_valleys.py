#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    currentPosition = 0
    lastDirection = ""
    for direction in s:
        #tracks current position
        if direction == 'U':
            currentPosition = currentPosition + 1
            lastDirection = 'U'
        else:
            currentPosition = currentPosition - 1
            lastDirection = 'D'
        
        #if current postion is 0 it must have come from a valley/mountain
        if currentPosition == 0:
            if lastDirection == 'U':
                valleyCount = valleyCount + 1
    return valleyCount
          


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
