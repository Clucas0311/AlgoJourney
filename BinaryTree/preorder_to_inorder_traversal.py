"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.
 Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Overview:
For this problem, we will be doing it recursively. 
We need to understand 2 things whatever is the first element in the preorder is going to be our root.
For the inorder travel list wherever the first element in preorder is in the inorder traversal the left side of it is going to be the 
left subtree and the right is going to be the right subtree
So we are going to search each array based on these specifications. So when trying to build the left subtree
We know that we need the next element in preorder so that'll be starting at index 1 and end at that index and for inorder start at beginning and end at the mid 
For right start at all the elements that are on the right of the mid for both inorder and preorder
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
