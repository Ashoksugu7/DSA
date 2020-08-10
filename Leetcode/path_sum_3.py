"""
Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #check all the possibility 
        if root is None:
            return 0
        
        main = self.pathSum_r(root, sum)
        return main+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)

    def pathSum_r(self, p, sum):
        #check sum from root to leaf
        if p is None:
            return 0
        count=0
        print(p.val, sum)
        if p.val == sum:
            count+=1
        
        l=self.pathSum_r(p.left, sum-p.val)
        r=self.pathSum_r(p.right, sum-p.val)
        return count+l+r
        


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.right.right= TreeNode(11)

obj = Solution()
print(obj.pathSum(root, 8))