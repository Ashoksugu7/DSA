#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sumXor function below.
def sumXor(n):
    # x=0
    # count=0
    # while x < n:
    #     if x+n == x^n:
    #         count+=1
    #     x+=1
    # return count
    if n==0:
        return 1
    power=Counter(bin(n))
    return 2**(power['0']-1)


print(sumXor(5))
