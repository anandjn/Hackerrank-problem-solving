#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #sorting keyboard array is decending order
    keyboards.sort(reverse = True)
    #sorting drives array in ascending order
    drives.sort()
    #check for base case and return -1
    if (b < (keyboards[-1] + drives[0])):
        return -1
    else:
        #making suitable combination whose sum is <= b and returning the max
        maxPrice = 0
        #variable to keep record of iterated drives
        i = 0
        for keyboard in keyboards:
            for j in range(i, len(drives)):
                #noting down for which indexed drive it break
                i = j
                value = keyboard + drives[j]
                if maxPrice < value and value <=b:
                    #modify maxPrice
                    maxPrice = value
                    #if we reached the top case early we exit to prevent further processing
                    if value == b:
                        return value
                if value > b:
                    break              
                
                
        return maxPrice

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

