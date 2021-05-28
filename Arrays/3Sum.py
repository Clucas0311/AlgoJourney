'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Setup:
First always ask if the list is sorted, if the list is not then sort it 
Create a container to hold the triplets that equal the value 
iterate through the array but keep room for the two pointer to do two sum 
So in all you will have three pointers one pointer that will stay fixed on a value 
In the case of checking for duplicates we first need to check the fixed pointer
CONDITION 
if i == 0 or when i > 0 and the current element doesn't equal the previous element then iterate
the two pointers needed are the next pointer from the current pointer so i + 1 and the the right will be the last element
The next two pointers will move like two sum when we have a match both two pointers will move at the same time 
if there is no match if the current_sum is too large decrease the right pointer
if the sum it too little increase the left pointer
when the values match the target add the items to the list and then check the two pointers for duplicates 
so if the current element and the next element match skip over them 
for right you decrement for left you increment
then increment and decrement both
lastly return the container of triplets

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Time Complexity O(N^2) Iterates once but again with the while loop with two sum
Space Complexity O(N) triplets stored make a O(N) space 
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        container = []
        for i in range(len(nums) - 2):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[left] + nums[right]
                    if current_sum == 0:
                        container.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum > 0:
                        right -= 1
                    else:
                        left += 1
        return container
