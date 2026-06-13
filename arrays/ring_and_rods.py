"""
Problem: Rings and Rods

Approach:
Use a hashmap where each rod stores a set of colors present on it.
Iterate through the input string in pairs (color, rod) and add the
color to the corresponding rod's set. Finally, count how many rods
contain all three colors: Red, Green, and Blue.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]

            if rod not in rods:
                rods[rod] = set()

            rods[rod].add(color)

        count = 0

        for colors in rods.values():
            if len(colors) == 3:
                count += 1

        return count
