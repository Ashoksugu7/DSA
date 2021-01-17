"""
Valid Mountain Array
Easy

570

81

Add to List

Share
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n < 3:
            return False
        
        def strict_decrease(start):
            for i in range(start, n):
                if arr[i-1] <= arr[i]:
                    return False
            
            return True
        
        def strict_increase():
            for i in range(2, n):
                print(arr[i-2], arr[i-1], arr[i])
                if arr[i-1] == arr[i] or arr[i-2] > arr[i-1] :
                    return False
                
                if arr[i-2] < arr[i-1] and  arr[i-1] > arr[i]:
                    return strict_decrease(i+1)
            
            return False
        
        
        return strict_increase()
        