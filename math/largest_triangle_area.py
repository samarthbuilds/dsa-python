"""
Problem: Largest Triangle Area

Approach:
Try every possible combination of three points.
For each triplet, calculate the triangle's area using
the Shoelace Formula. Keep track of the maximum area found.

Time Complexity: O(n^3)
Space Complexity: O(1)
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2

                    max_area = max(max_area, area)

        return max_area
