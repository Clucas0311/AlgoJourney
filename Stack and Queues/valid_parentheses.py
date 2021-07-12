"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Overview:
So a valid parentheses is if it has an open an closed bracket, It will not be valid if the string starts with an close
and if a close comes before it open counter part
Create a hashMap to track keys are closes and values are opens 
Use a stack
Iterate through the string if the stack is not empty and the matching opening value is found in the dictionary 
then pop pair from stack 
otherwise it will be false

Time O(N)
Space O(N) 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {']': '[', '}': '{', ')': '('}

        for char in s:
            if char in close_to_open:
                if stack != [] and stack[-1] is close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
