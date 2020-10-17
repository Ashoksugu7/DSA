"""
Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""
class Solution:

    def list2nums(self, digits):
        res=0
        for i in range(len(digits)):
            res=(res*10)+digits[i]
        return res


    def sequentialDigits(self, low: int, high: int):
        res=[]
        
        digits=[ i for i in range(1,10) ]
        len_digits= len(digits)
        # print(digits)
        s_low=len(str(low))
        s_high=len(str(high))

        cur=s_low
        while (cur <= s_high):
            for i in range(len_digits):
                if i+cur <= len_digits:
                    temp =self.list2nums(digits[i:i+cur])
                    if low <= temp and temp <= high:
                        res.append(temp)
            cur+=1
        
        return res
            

obj = Solution()
print(obj.sequentialDigits(1000, 1000000000))
