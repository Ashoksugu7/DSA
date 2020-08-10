"""
ind All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
import math
class Solution:
    def findDuplicates(self, nums):
        result=[]
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if (nums[index] < 0):
                result.append(index+1)
            #visited index changed to the negative value
            nums[index]=-nums[index]
            #print(nums, i, index)
        return result
obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))