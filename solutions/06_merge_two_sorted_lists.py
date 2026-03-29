"""
6. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list.

Example:
    Input: l1 = 1->2->4, l2 = 1->3->4
    Output: 1->1->2->3->4->4

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


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
    l1 = array_to_list([1, 2, 4])
    l2 = array_to_list([1, 3, 4])
    merged = merge_two_lists(l1, l2)
    print(list_to_array(merged))  # [1, 1, 2, 3, 4, 4]
