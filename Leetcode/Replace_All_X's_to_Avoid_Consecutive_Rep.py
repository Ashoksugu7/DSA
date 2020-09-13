"""
Replace All ?'s to Avoid Consecutive Repeating Characters
User Accepted:603
User Tried:816
Total Accepted:603
Total Submissions:919
Difficulty:Easy
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"
 

Constraints:

1 <= s.length <= 100

s contains only lower case English letters and '?'.
"""

class Solution:
    def modifyString(self, s: str) -> str:
        res=list(s)
        n=len(res)
        for i in range(len(res)):
            if res[i]=='?':
                print(i)
            
                
                k=97
                while  ( i+1 < n and (ord(res[i-1])==k or k==ord(res[i+1]) ))  :
                    k+=1
                else:
                    res[i]=chr(k)
                    if(i==n-1 and res[i-1]=='a'):
                        res[i]='b' 
                print(res)
        

                

            
        return ''.join(res)


obj=Solution()
print(obj.modifyString("?a?ub???w?b"))