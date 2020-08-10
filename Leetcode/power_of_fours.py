"""
Power of Four

Solution
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false

Example 3:

Input: 256
Output: true
Follow up: Could you solve it without loops/recursion?

"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0:
            bin_str=bin(num)[::-1]
            if bin_str.count('1') > 1:
                return False
            else:
                return bin_str.index('1')%2==0
            
        else:
            return False
        

obj = Solution()
print(obj.isPowerOfFour(4))
print(obj.isPowerOfFour(256))
print(obj.isPowerOfFour(5))