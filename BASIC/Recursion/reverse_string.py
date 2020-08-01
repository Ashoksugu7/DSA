#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:03:57 2020

@author: ashok
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        j=len(s)-1
        for i in range(len(s)//2):
            s[i],s[j] = s[j],s[i]
            j-=1
            
        return s

obj = Solution()
print(obj.reverseString([1,2,4,5,6]))


def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        p=head
        while p.next is not None:            
            p.val, p.next.val = p.next.val, p.val
            if p.next.next is not None:
                p=p.next.next
            else:
                p=p.next
        return head
        