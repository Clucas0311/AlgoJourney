"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Overview: 
So inorder to get the path sum we need to the sum of a specific branch 
So We will use DFS. This will help us traverse the tree recursively giving us the sum 
If the sum is not calculate it will go back up and start traversing from the right
So first check to see if the root is none, if the root is none then return 0 ---> base case
next if the the root.val equals the sum and it has no children/leaf nodes then return true
recursive case traverse the left and right but subtract from some as you go

Time O(N) ---> Traverse each node once
Space O(N) --> Spaced used for the recursion stack


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [1,2], targetSum = 0
Output: false
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        if targetSum == root.val and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
