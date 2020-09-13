#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    """
    You will be given an array of integers. All of the integers except one occur twice. That one is unique in the array.

    Given an array of integers, find and print the unique element.
    """
    res=0
    for i in range(len(a)):
        res^=a[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()