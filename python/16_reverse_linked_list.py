"""
Q16. Reverse Linked List (Category: Linked List)

Problem: Reverse a singly linked list iteratively.

Approach: Maintain prev and curr pointers. Re-link each node to point backward,
          then advance both pointers.

Time Complexity : O(n)
Space Complexity: O(1)
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def list_to_str(head: Optional[ListNode]) -> str:
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    return " -> ".join(parts)


if __name__ == "__main__":
    # Build 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(list_to_str(reverse_list(head)))  # 5 -> 4 -> 3 -> 2 -> 1
