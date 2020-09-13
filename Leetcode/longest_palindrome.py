"""
Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = [0]*52
        for char in s:
            ascii = ord(char)
            if ascii > 64 and ascii < 91:
                count[ascii-65]+=1
            else:
                count[(ascii-97)+25]+=1
        print(sum(count))
        temp_old = [0]
        even_res = 0
        even_only=True
        for i in count:
            if i%2 ==0:
                even_res+=i
            else:
                even_only = False
                even_res+=i-1

        if even_only:
            return even_res
        else:
            return even_res+1



obj = Solution()
print(obj.longestPalindrome("bb"))