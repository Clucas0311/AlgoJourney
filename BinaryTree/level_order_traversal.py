"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Overview: 
When you think of level order traversal you think of a queue FIFO (First in First Out)
Edge Cases: if the the root is none then return an empty array 
So the first thing you will need to is put the root in the queue the root 
Now while the queue is not empty iterate 
now we will need to check the currentNode to see if it has any children  but first create 
the levels array each level needs to be in an array so assign levels to an empty array 
now we are going to use the size of the queue to help add its children to the queue
now iterate as long as the level_size is greater than 0 if the size is greater than 0 get the currentNodes children
the currentNode is going to be the root node in the queue remove that node and check to for its left and right children 
now that the level is in the queue remove push the currentNode.val to the levels array 
Do these steps until all the children removed from the queue and into levels 
push each level into the results container 
return result

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

            result.append(level)

        return result
