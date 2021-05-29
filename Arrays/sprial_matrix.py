"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Overview: 
For this algorithim we are going to use pointers and matrix boundaries to traverse through the list
First thing we need to do is create a container that will hold all the elements in after traversing
Next create boundaries for matrix positions
You will need to create a pointer start at the startCol, startRow both of which will be 0
the endRow will be the last element in the matrix and the endCol will be the last element for the first array at its index 
while traversing you are going to be changing one position row/col at a time 
so if you want only elements in the first col you will start at the startCol and at the endCol inclusive so add 1
Next to get the rows you will move the position downward startRow + 1 and get the elements in the endCol between the that position
and the endRow
Next get the elements in the endRow but in reversed order 
After that the last col
Then move the pointers inward after all iterations are met 
if the startRow === endRow then break so test the conditions for both row and col to remove duplicates

Time Complexity: O(N) for the total number of the elements in the matrix 
Space Complexity O(N) storing all N values in the array 

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        container = []
        startCol = 0
        startRow = 0
        endRow = len(matrix) - 1
        endCol = len(matrix[0]) - 1
        while startRow <= endRow and startCol <= endCol:
            for col in range(startCol, endCol + 1):
                container.append(matrix[startRow][col])
            for row in range(startRow + 1, endRow + 1):
                container.append(matrix[row][endCol])
            for col in reversed(range(startCol, endCol)):
                if startRow == endRow:
                    break
                container.append(matrix[endRow][col])
            for row in reversed(range(startRow + 1, endRow)):
                if startCol == endCol:
                    break
                container.append(matrix[row][startCol])
            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
        return container
