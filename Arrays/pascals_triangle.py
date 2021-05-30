"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Time Complexty and Space O(N^2)

Overview:
First create an array of all 1's that will grow i + 1 number of rows for the amount of rows needed 
Iterate through the rows 
Iterate again but start at 1 since Pacals Triangle the first and last element must be filled with one's before
Each row is created by adding the previous element and the current element from the previous row
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result
