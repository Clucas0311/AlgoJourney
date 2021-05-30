''' Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Overview:
This problem deals with two pointers that are on the same side. so you will have one pointer 
Which will be the anchor and the other will be the explorer 
The anchor will move during each iteration 
If the current element doesn't equal zero we will swap the zero with the non matching one 
Thus placing all the zeros the end of the list

Time Complexity O(N) the length of the list
Space O(1) Nothing is stored and in place
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        explorer = 0
        while explorer < len(nums):
            if nums[explorer] != 0:
                temp = nums[anchor]
                nums[anchor] = nums[explorer]
                nums[explorer] = temp
                anchor += 1
            explorer += 1
