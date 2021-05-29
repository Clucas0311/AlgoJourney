"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Template:
First check to see if the lengths of the two strings given are the same length 
Because anagram means SAME characters and SAME length 
Now create a hash_map this hash_map is going to keep track of the occurences of each 
character in the first string 
Now after creating a hash_map check to see if the second strings characters are located 
inside that string, if they are then decrement that value 
Otherwise return False
Now if the string's are anagrams of one another the hash_map's values should all be 0
if the hash_map is all zero's then we have an anagram, otherwise the algorithim is not an anagram

Time O(N) because creating the hash_map is O(N) the length of the string 
Space O(1) Because the hash_map's size will remain the same no matter how large the string is

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
            else:
                return False

        for val in hash_map.values():
            if val != 0:
                return False
        return True
