"""
Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

"""
class Solution:
    def upper_only(self, word):
        for ch in word:
            if ord(ch) > 96:
                return False
        return True

    def lower_only(self, word):
        for ch in word:
            if ord(ch) < 96:
                return False
        return True       


    def detectCapitalUse(self, word: str) -> bool:
        #one character is alway true
        if len(word) <= 1:
            return True

        #checking first two character
        if ( int(ord(word[0])) < 96 and int(ord(word[1]) < 96)):
            #all letter are upper
            return self.upper_only(word[2:])
        elif (int(ord(word[0]) < 96 and int(ord(word[1])) > 96 )):
            #first letter upper and remain lower
            return self.lower_only(word[2:])
        else:
            #all letter are lower
            return self.lower_only(word)
            




obj = Solution()
print(obj.detectCapitalUse("  "))