"""
Problem: Robot Return to Origin

Approach:
Track the robot's position using x and y coordinates.
Update the coordinates based on each move:
- U increases y
- D decreases y
- L decreases x
- R increases x

After processing all moves, the robot returns to the origin
if both x and y are zero.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == 'U':
                y += 1

            elif move == 'D':
                y -= 1

            elif move == 'L':
                x -= 1

            else:
                x += 1

        return x == 0 and y == 0
