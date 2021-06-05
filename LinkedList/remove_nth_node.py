"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Overview: 
The approach to this problem we need to create two pointers as well as create a dummyHead
So the dummyHead will be inserted in the front of the current head
The left pointer will be positon at the start of the linked list so 0
The right pointer will be positioned at the former head of the linked list
Now shift the right pointer n steps so the distance between the left and right will be 
nth spaces, decrement n each iteration
now iterate as long as the right isn't none
This will move the left position one node away from the node we want to remove
so now change the next pointer of the left positon change it to equal the node after its current next
return the dummyHead.next this will omit the dummyHead value created. 

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummyHead = ListNode(0, head)
        left = dummyHead
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummyHead.next
