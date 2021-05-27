"""
Write a function to find the longest common prefix string 
amongst an array of strings.
If there is no common prefix, return an empty string "".

To Approach this problem we will be doing the vertical scanning apporoach
Where we will be taking the first element getting each individual character
then check to see if each character matches the character in the first string 
if the string doesn't match return the prefix created otherwise add to the prefix 

Only add to prefix if each character matches the first character  of each element

Time Complexity O(S) ---> Where S is the sum of all the characters
O(S * m) for even lengths
Space O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # intialize a variable to add the prefix to if they match
        prefix = ""
        # if the str length is empty then return prefix
        if len(strs) == 0:
            return prefix
        # iterate through the first element to get each individual character
        for i in range(len(strs[0])):
            characters = strs[0][i]
            # iterate through the whole strs array omitting the first element
            for j in range(1, len(strs)):
                #if the first element character is the same size as the element or the characters 
                # don't match return the prefix
                if i == len(strs[j]) or strs[j][i] != characters:
                    return prefix
            #otherwise update and concat the character to the prefix total
            prefix = prefix + characters
        # if all values are true return prefix
        return prefix