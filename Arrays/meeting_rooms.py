"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 
Overview: So first thing we need to do is sort the array in ascending order 
We need to make sure that each start time start from least to greatest 
Once we have that we will then traverse the array grabbing two elements 
initialize the last_end to be -1
start, end 
if there is a situation where last_end <= start then keep traversing 
but if last_end > start return ---> return false
update last_end to equal end and compare during each traversal

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last_end = -1
        for start, end in intervals:
            if last_end <= start:
                last_end = end
            else:
                return False
        return True
