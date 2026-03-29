"""
Q17. Detect Cycle in Linked List (Category: Linked List)

Problem: Detect if a linked list has a cycle.

Approach: Floyd's slow-fast pointer algorithm.
          If slow and fast ever meet, a cycle exists.

Time Complexity : O(n)
Space Complexity: O(1)
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    # Cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    n3, n2, n0, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n3.next = n2; n2.next = n0; n0.next = n4
    n4.next = n2  # cycle
    print(has_cycle(n3))  # True

    # No cycle: 1 -> 2
    nc = ListNode(1, ListNode(2))
    print(has_cycle(nc))  # False
