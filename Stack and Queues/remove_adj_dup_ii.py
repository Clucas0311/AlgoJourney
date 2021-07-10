"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Overview: 
Similar to Remove Adj I with the use of the stack, ---> remember that strings are immutable so I stack will be helpful to keep track
Now the stack's will have array of elements the first element of the first array will be the char and the second will be the number count or freq
Everytime the char is a duplicate you are adding to the freq element
If the stack's last element equals to k then pop/remove that last element from the stack 
Then after that concat the remaining elements in the stack to a string 
 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ''
        stack = []
        for char in s:
            if stack != [] and stack[-1][0] is char:
                stack[-1][1] += 1
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ''
        for arr in stack:
            result += (arr[0] * arr[1])

        return result
