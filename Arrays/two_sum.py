"""
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Objective:
So this is two sum unsorted the technique involved is you first create an dictionary 
this dictionary will be used as a look-up as we iterate through the array we are going 
to check to see if the key which is the target - current_elm has been seen in the dictionary
if it has return the an array with the needed_value and the i, otherwise the dictionary 
will store the current_elm as a key and the i as its value for look-up

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        hash_map = {}
        for i in range(len(nums)):
            current_elm = nums[i]
            needed_val = target - current_elm
            if needed_val in hash_map:
                return [hash_map.get(needed_val), i]
            else:
                hash_map[current_elm] = i