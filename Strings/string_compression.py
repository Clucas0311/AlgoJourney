"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
 Time Complexity O(N) Iterate the length of the string once
 Space O(1) we didn't store it into anything so its inplace 
 Overview: 
 You will need to create two pointers i and j
 First create a index variable this variable will help us know where we need to place the number and the letter 
 in our character array
 now the two pointers the i pointer is going to stay in place until the the j pointer reaches a character that doesn't match
 when the charater doesn't match 
 we will update the chars[index] to equal the character at the current i position 
 then increment the index up one giving it a position for us to place the number characters in the array 
 now to get the number characters we need to get the distance beteen i and j 
 do j - i if that value is greater than one that means we we are going to compress that number
 then convert that number character into a string and place that into a characters array 
 do this by iterating through the loop 
 increment index each time there is a new character 
 move i to the same positon j is and start over 
 and return the index which will be the newly compressed string 


Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
Example 4:

Input: chars = ["a","a","a","b","b","a","a"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.

"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                count = str(j - i)
                for letter in count:
                    chars[index] = letter
                    index += 1
            i = j

        return index
