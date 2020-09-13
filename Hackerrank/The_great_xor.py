import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.
"""
5 -> 101 => 010 -> 2


"""
def theGreatXor(x):
    return (1 << x.bit_length())-1-x


print(theGreatXor(5))
print(theGreatXor(100))