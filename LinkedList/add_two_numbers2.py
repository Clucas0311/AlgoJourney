"""
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers 
and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Overview:
Same Approach As Add Two Numbers One, but use an Array/stack 
And Pop off back element 
After The linked List is created, reverse it back to its orginal position 

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        head = dummyHead
        p1 = []
        p2 = []
        carry = 0

        while l1:
            p1.append(l1.val)
            l1 = l1.next

        while l2:
            p2.append(l2.val)
            l2 = l2.next

        while len(p1) != 0 or len(p2) != 0:
            x = p1.pop() if len(p1) != 0 else 0
            y = p2.pop() if len(p2) != 0 else 0
            sum = x + y + carry

            carry = sum // 10
            dummyHead.next = ListNode(sum % 10)
            dummyHead = dummyHead.next

        if carry > 0:
            dummyHead.next = ListNode(1)

        def reverse(head):
            prev = None
            currentNode = head
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = prev
                prev = currentNode
                currentNode = nextNode
            return prev
        return reverse(head.next)
