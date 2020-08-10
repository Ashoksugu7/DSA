"""
Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute=0
        freshs = []
        rottens= []
        #direction of the infections
        directions = [[0,1],[1,0], [0,-1],[-1,0]]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                #identity rotten and fresh orangle position
                if grid[i][j]==2:
                    rottens.append([i, j])
                
                if grid[i][j]==1:
                    freshs.append([i, j])


        print(freshs)
        print(rottens)
        
        while (len(freshs) > 0):
            infected=[]
            for rotten in rottens:
                x = rotten[0]
                y = rotten[1]
                for direction in directions:
                    i = x + direction[0]
                    j = y + direction[1]
                    if [i, j] in freshs:
                        
                        freshs.remove([i, j])
                        infected.append([i, j])
                        print(freshs, rottens, i,j, infected, sep="==")
                        print("")
                    i=x
                    j=y
            
            
            if len(infected) == 0:
                return -1

            rottens=infected
            minute+=1            
        
        
        
        
        return minute

    

        




obj = Solution()
grid=[[2,1,1],[0,1,1],[1,0,1]]
print(obj.orangesRotting(grid))