"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).


Overview: 
Same BFS Template but this time we need to create a boolean to check to see if the direction is 
left_to_right or right_to_left
Based on those insertions we will append the current_node.val into the levels array

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []


Time Complexity: Traverse the Tree touching every Node O(N)
Space Complexity: O(N) the space needed to store nodes in the queue
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result = []

        # create a boolean to change the order
        left_to_right = True
        while queue != []:
            level = []
            level_size = len(queue)

            while level_size > 0:
                current_node = queue.pop(0)

                # if the direction is left to right
                if left_to_right:
                    # then append the value original direction
                    level.append(current_node.val)
                else:
                    # append the value from the front
                    level.insert(0, current_node.val)

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

                level_size -= 1

            result.append(level)
            # update direction
            left_to_right = not left_to_right

        return result
