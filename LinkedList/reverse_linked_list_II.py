"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Overview: 
So to attack this problem understand that we we want to reverse a specfic portion 
of the linked list at a certain positon 
So you will create to tracker variables a prev = null and currentNode = head
while traversing through the linked list move the prev pointer to  the head position 
and the currentNode to the head of the sublist portion 
You do this by iterating as long as left position is greater than 1 
then decrement left and right pointer until in the sublist postion
Next create a connection variable this will keep reference of the prev node we created which is at the head
and the subTail we will assign the value of the currentNode we do this because last currentNode will be on the last 
node when the sublist is reversed
now reverse the sublist portion of the linked list by iterating through portion and decrementing the right 
right will be at the postion and complete at the end position of the subarray

Now reconnect the connection next value to the reverse linked head 
if the linked list position is at the head position then reassign the value of head to the the reversed portion
and assign the subtail to the currentNode
return the head positon

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        prev = None
        currentNode = head

        while left > 1:
            prev = currentNode
            currentNode = currentNode.next
            left -= 1
            right -= 1

        connection = prev
        subTail = currentNode

        while (right > 0):
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
            right -= 1

        if connection:
            connection.next = prev
        else:
            head = prev
        subTail.next = currentNode
        return head
