"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Overview: 
This is graph problem so the first thing we are going to do is check to see if grid is None and the length is not 0
if is return 0 
So each islands deals with 1 to the left right above we are going to count each item 
To do so, we are going to create a number_of_islands tracker set to 0 
Next traverse the matrix to find when a island is in the matrix 
an Island equals "1" we are going to increment the number_of_islands tracker 
in order to do so we are going to create a helper method that will recursively call 
the base case will be when the matrix is out of bounds 
and the recursive cases will be called four times checking left, right up and down
return 1 each time is encounters a 1
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] is "1":
                    number_of_islands += self.get_island_count(grid, i, j)

        return number_of_islands

    def get_island_count(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        grid[i][j] = "0"
        self.get_island_count(grid, i + 1, j)
        self.get_island_count(grid, i - 1, j)
        self.get_island_count(grid, i, j + 1)
        self.get_island_count(grid, i, j - 1)
        return 1
