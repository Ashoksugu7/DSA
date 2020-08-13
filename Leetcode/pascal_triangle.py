"""
Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
1
11
121
1331
14641


Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        temp=[1,1]
        #reusing previous list to identifying the current list
        while(rowIndex > 1):
            res=[1]
            for i in range(len(temp)-1):
                res.append(temp[i]+temp[i+1])
            res.append(1)
            temp=res

            rowIndex-=1
        return temp

    



obj = Solution()
print(obj.getRow(6))