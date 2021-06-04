"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Overview: First Remember Elementary School Additon 
You add from the back when you reach a duplicate sum you carry the value 
The linked list is reversed so this is actually to our favor 
So to add two linked list you will need to create a new linked list we will call this 
dummyHead. As we traverse the linked list we will need to create each node 
each node will be the last digit so in order to get that we can use the modulo operator 
this will give us the remainder sum  % 10
we will also need a value called carry to store the carry number 
The carry number should always be the first number so we can get that by integer dividing the sum number
so the total sum should equal value from l1 value from l2 and carry 
we will update the carry each iteration --> sum // 10
and create a new node by getting the remainder sum % 10
Once we have our new linked list we need to take in account the carry may be left over if the carry is greater than one at the last node
so what we will do is add one to its next value 
this will give us our add two numbers linked list

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


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
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry
            carry = sum // 10
            dummyHead.next = ListNode(sum % 10)

            dummyHead = dummyHead.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            dummyHead.next = ListNode(1)
        return head.next
