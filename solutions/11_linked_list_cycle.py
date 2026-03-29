"""
11. Linked List Cycle Detection
Given the head of a linked list, determine if the linked list has a cycle.
Use Floyd's Cycle Detection Algorithm (two pointers).

Example:
    Input: 3 -> 2 -> 0 -> -4 -> (back to 2)
    Output: True

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    # Build: 3 -> 2 -> 0 -> -4 -> (back to node with val=2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle
    print(has_cycle(node1))  # True

    # No cycle
    head = ListNode(1, ListNode(2))
    print(has_cycle(head))   # False
