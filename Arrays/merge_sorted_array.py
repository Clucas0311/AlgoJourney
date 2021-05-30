"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Overview:
The goal is we will create two pointers, one will access the first array the other the second 
REMEMBER Arrays are 0 based so subtract one from them 
We will traverse from the last element right to left in the nums1 array 
so access the index of nums1 which will be m + n - 1
iterate as long as the index is greater than or equal to 0 
In the case if one of the arrays reach to the end before the other as the array with 
values still in it to the nums1[index] 
Next check to see if either element is greater than the other if it is then add it to the longest array
decrement each pointer during each iteration

Time Complexity O(m + n) ---> iterate through both arrays at different lengths
Space Complexity O(1) --> Size doesn't change 

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        index = m + n - 1

        while index >= 0:
            if first < 0:
                nums1[index] = nums2[second]
                second -= 1
            elif second < 0:
                nums1[index] = nums1[first]
                first -= 1
            else:
                if nums1[first] > nums2[second]:
                    nums1[index] = nums1[first]
                    first -= 1
                else:
                    nums1[index] = nums2[second]
                    second -= 1
            index -= 1
