"""
Given a string s, find the length of the longest 
substring without repeating characters.

Approach: This problem deals with the sliding window technique 
We will create two pointers one that will extend if there are no duplicates 
The other will remain put if there is a duplicate it will then increment removing that element
creating a new substring
So, we are going to first create a set --> a set is useful because it only contains unique values
if the set doesn't have  the value we are going to add the value to the set and then update out max value to get 
the size of the set if we run into a duplicate value we are going to remove the pointer in the front and create 
a new substring you do this until iteration is over - updating the max to a new max on the way.

Time Complexity O(n) iterate the length of the string 
Space Complexity O(min(m,n)) n is the size of the characters in the alphabet
and o(k) is the size of the set
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a 
subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set = set()
        right = 0
        left = 0
        longest = 0
        while right < len(s):
            if s[right] not in new_set:
                new_set.add(s[right])
                longest = max(longest, len(new_set))
                right += 1
            else:
                new_set.remove(s[left])
                left += 1
        return longest
