"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Overview: 
Same BFS Template but instead of inserting into an array each level 
Get the sum for each level 
then append the average so level_sum / level_size 

Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Time Complexity: O(N) ---> Touched every node during traversal
Space Complexity: O(N) ----> O(N) space to store items in the queue

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []

        queue = [root]
        result = []

        while queue != []:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                current_node = queue.pop(0)

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

                level_sum += current_node.val

            result.append(level_sum / level_size)

        return result
