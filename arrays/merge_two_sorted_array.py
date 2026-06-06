"""
Problem: Merge Two Sorted Lists

Approach:
Use a dummy node to build the merged linked list.
Compare the current nodes of both lists and attach the smaller one
to the result. Move the corresponding pointer forward.
After one list is exhausted, attach the remaining nodes of the other list.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
