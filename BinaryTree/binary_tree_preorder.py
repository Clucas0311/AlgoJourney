"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]


Overview: 
Recursive Case:
To understand this problem you need to know about traversing a binary tree
Preorder Traversal involves Get the current node or root and printing the value then check for left or right nodes
So the base case for this problem will be to check to see if the root is empty or None 
When the root is empty we will want to end so just return an empty array 

The recursive case so in order to create the new array we will be concating the [root.val] and the recursive calls of preorder(left) plus preorder[right]
when both cases reach none they will then create a sublist and we concat them as we proceed

Iterative Case:
Since we don't have a call stack we will be using a stack that will take in the root 
We will also be creating a results container to push root values into 
Since stacks deal with LIFO we will be pushing into the stack from the right 
and this will then allow us to pop elements from the left first then the right 
EDGE CASE: if the root is None then return an empty array

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # base case:
        if root is None:
            return []

        # recursive case:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# Iterative Solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result
