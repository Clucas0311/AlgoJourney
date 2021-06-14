"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

Overview: 
Same template as every BFS but instead of creating a container to put each level into, 
Push into the results container the right side branch nodes, this includes right side nodes on the left side as well
Do this by getting the length of the queue and subtracting that by 1 so becasically all its last elements 

Time O(N) traversal touches each node
Space --> O(N) as the number of nodes grow the queue will grow
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = [root]
        result = []

        while queue != []:
            level_size = len(queue)

            for i in range(0, level_size):
                currentNode = queue.pop(0)

                if i == level_size - 1:
                    result.append(currentNode.val)

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

        return result
