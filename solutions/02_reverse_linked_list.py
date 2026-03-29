"""
2. Reverse a Linked List
Given the head of a singly linked list, reverse the list and return the
reversed list.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    head = array_to_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    print(list_to_array(reversed_head))  # [5, 4, 3, 2, 1]
