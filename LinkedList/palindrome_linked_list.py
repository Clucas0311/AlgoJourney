"""
Given the head of a singly linked list, return true if it is a palindrome.

Overview:
This problem involves the fast and slow pointers
So the first thing we need to do is check the edge case if there is no head return none
Then establish the fast and slow pointers -- both will start at the head position
Now, the objective with the two pointers is to move the fast pointer to the middle and then 
reverse it 
when traversing with the fast and slow technique keep in mind the fast is move two steps 
ahead of the slow pointer so when iterating we need to check for the current node the fast is on 
and the next node because if either of them are null then we can't move two spaces up
so iterate while fast and fast.next are not null 
now slow will be in the middle of the linked list and fast will be at the end 
Next step, reset fast position back to the front of the linked list 
and the slow will remain in its position but this time we will reverse that sublist 
We will then compare the fast and slow nodes until the end of slow's traversal 
if the values do not equal one another return false not a palindrome
if they complete the iteration then it is true it is a palindrome

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            prev = None
            currentNode = head
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = prev
                prev = currentNode
                currentNode = nextNode
            return prev

        slow = reverse(slow)
        fast = head

        while slow:
            if slow.val != fast.val:
                return False
            else:
                slow = slow.next
                fast = fast.next

        return True
