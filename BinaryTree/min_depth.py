"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Overview: Same BFS Template but check to see if the current node has any children
if not add to the depth and return it. 


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = [root]
        min_depth = 0

        while queue != []:
            level_size = len(queue)

            for _ in range(level_size):
                current_node = queue.pop(0)

                if current_node.left is None and current_node.right is None:
                    min_depth += 1
                    return min_depth

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

            min_depth += 1
