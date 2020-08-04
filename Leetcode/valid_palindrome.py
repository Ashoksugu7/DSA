"""
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            while (i < j and not s[i].isalnum()):
                #skipping left side non-alpha numerical character
                i+=1
            
            while (i < j and not s[j].isalnum()):
                #skipping right side non-alpha numerical character
                j-=1
            
            if (i < j and s[i].lower() != s[j].lower()):
                #comparing the both side character                
                return False
            i+=1
            j-=1
            
        return True

obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))