"""
Maximum Repeating Substring
User Accepted:4
User Tried:20
Total Accepted:4
Total Submissions:20
Difficulty:Easy
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
 

Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
"""
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count =0
        s_len = len(sequence)
        w_len = len(word)
    
        
        if w_len > s_len:
            return count
        
        if word == sequence:
            return 1
        
#         for i in range(s_len-w_len+1):
#             print(i, sequence[i:i+w_len], word)
#             if sequence[i:i+w_len] == word:
#                 count+=1
#             else:
#                 count=0
                
#         return count

        count=0
        while True:
            
            print(word*count,sequence)
            if word*count in sequence:
                count+=1
            else:
                if count > 0:
                    return count-1
                else:
                    return 0
        