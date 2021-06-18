"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Overview:
Do the iterative approach for Inorder Traversal, creating a stack as the call stack
Create a n pointer that will increment every time a node is popped off of the stack 
if n == k then return the value

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        curr = root
        stack = []

        while curr is not None or stack != []:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
