"""
Thousand Separator
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31
"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        beg=str(n)
        for i in range(len(beg)-3,0, -3):
            print(i)
            beg=beg[:i]+"."+beg[i:]
            print(beg)
        return beg
        

obj = Solution()
print(obj.thousandSeparator(1234567))