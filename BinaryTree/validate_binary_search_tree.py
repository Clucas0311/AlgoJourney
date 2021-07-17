"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Overview: 
This can be solved using DFS. So what we are going to do is create a helper method called valid 
this method is going to take the current node, the left boundary, and the right boundary
We know that a binary search tree left side is that its right boundarys  always be less than the root 
and its left boundary can be less than -infinity,  and for the right side it always has to be greater than the parent root so that will be the smallest it can be 
and it can grow towards positive infinity
So the base case will be if the node is None return true b/c BST can be none and still be BST
not if the node.val is not less than the parent node on the left and not greater than the parent node on the right then it isn't a BST

Traverse through every node in the binary tree when we reach to a leafnode/ node with no children we are going to return true, make the binary search tree valid
If we are not at a leaf node we need to recursivly look through each subtree and see if the root is less than the right node and greater than the left 
So validate the left and right subtree recursively
Keep track of the min and max values of the tree 
Recursive CASE:
call valid if valid is on the left create the boundaries same for the right

lastly invoke the valid function with float('inf')

Time Complexity O(N) ---> Traverses Through Every Node
Space Complexity O(N) ---> Depending on the call stack frame 

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if node is None:
                return True

            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))
