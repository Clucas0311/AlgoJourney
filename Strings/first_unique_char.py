"""
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

Overview: 
Looking for first unique character so you will need to create a character map
Once you create the character map to track occurances 
Iterate through the string to get is index
check the character map to see when the value first equals one then immediately return that index
Otherwise when the loop ends return -1 

Time O(N) Going through the string twice to create the hashMap and to check for index
Space O(1)  Characters in the alphabet 26
 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        index = 0
        while index < len(s):
            if hash_map.get(s[index]) == 1:
                return index
            index += 1
        return -1
