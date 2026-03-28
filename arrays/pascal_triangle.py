"""
Problem: Pascal's Triangle

Approach:
Build the triangle row by row. Each row starts and ends with 1.
For the middle elements, use the values from the previous row:
triangle[i-1][j-1] + triangle[i-1][j].

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle
