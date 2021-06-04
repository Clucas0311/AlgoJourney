"""
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Overview:
How to attack this problem first we need to take an account the edge cases 
If one the linked list is null return the other one

To Do this problem we need to create a dummyNode, we will be essentially creating a 
new linked list and attach to it the node that is least then move the pointer as we progress
and the position of the dummyNode. 
Now when the iteration is complete We need to take in account when one of the list has reach null or the end
when we reach the end we will attach the next value of the remaining linked list 
to the linked list that still has nodes

REMEMBER whenever we create a dummyhead always keep access to the the head by creatng a head variable assigned the the dummyHead

return head.next

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        head = dummyHead
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                dummyHead.next = l1
                l1 = l1.next
            else:
                dummyHead.next = l2
                l2 = l2.next
            dummyHead = dummyHead.next

            if l1 != None:
                dummyHead.next = l1
            else:
                dummyHead.next = l2
        return head.next
