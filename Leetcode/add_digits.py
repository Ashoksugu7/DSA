#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:37:17 2020

@author: ashok

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
             
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        else:
            t = sum([ int(i) for i in str(num) ])
            return self.addDigits(t)
        
    def quick_solution(self, num):
        if num == 0:
            return num
        elif num%9==0:
            return 9
        else:
            return num%9
        
        
        
obj = Solution();
print(obj.addDigits(9875))
print(obj.quick_solution(9875))

