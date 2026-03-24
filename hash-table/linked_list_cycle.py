"""
Problem: Linked List Cycle

Approach:
Use Floyd’s Cycle Detection (Tortoise and Hare) algorithm.
Maintain two pointers: slow moves one step at a time and fast moves two steps.
If there is a cycle, both pointers will eventually meet.
If fast reaches the end, there is no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 

        return False
