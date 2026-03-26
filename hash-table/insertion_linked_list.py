"""
Problem: Intersection of Two Linked Lists

Approach:
Use two pointers for both linked lists. Traverse both lists,
and when a pointer reaches the end, redirect it to the head of
the other list. This way both pointers will traverse equal lengths.
If there is an intersection, they will meet at the intersection node.
Otherwise, both will reach None.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA
