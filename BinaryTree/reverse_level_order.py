"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Overview: 
The same pattern for level order traversal but with a twist, instead of appending level to the result
add the array elements to the front as opposed to the back 

Time Complexity --> O(N) N is the every node in the tree
Space Complexity --> O(N) where is n is the size of the queue

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        result = []

        while queue != []:
            level = []
            level_size = len(queue)

            while level_size > 0:
                currentNode = queue.pop(0)

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

                level.append(currentNode.val)
                level_size -= 1

            result.insert(0, level)

        return result
