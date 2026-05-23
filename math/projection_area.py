"""
Problem: Projection Area of 3D Shapes

Approach:
Calculate the projection areas from three different views:
1. Top view: count all non-zero cells
2. Front view: find the maximum value in each row
3. Side view: find the maximum value in each column

Add all three projection areas to get the final answer.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        top = 0
        front = 0
        side = 0

        for i in range(n):
            row_max = 0
            col_max = 0

            for j in range(n):
                if grid[i][j] > 0:
                    top += 1

                row_max = max(row_max, grid[i][j])
                col_max = max(col_max, grid[j][i])

            front += row_max
            side += col_max

        return top + front + side
