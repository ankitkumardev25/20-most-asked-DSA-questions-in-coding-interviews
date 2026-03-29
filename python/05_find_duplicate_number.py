"""
Q5. Find the Duplicate Number (Category: Arrays)

Problem: Given an array of n+1 integers where each value is in [1, n],
         find the one duplicate. Do not modify the array; use O(1) extra space.

Approach: Floyd's cycle detection (treat array indices as a linked list).
          nums[i] acts as the "next" pointer. The duplicate creates the cycle entrance.

Time Complexity : O(n)
Space Complexity: O(1)
"""


def find_duplicate(nums: list[int]) -> int:
    # Phase 1: find intersection inside cycle
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find cycle entrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))  # 2
    print(find_duplicate([3, 1, 3, 4, 2]))  # 3
