"""
16. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the k-th largest element
in the array.

Example:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5

Time Complexity: O(n) average using QuickSelect
Space Complexity: O(1)
"""

import random


def find_kth_largest(nums, k):
    # We want the k-th largest, which is the (n-k)-th smallest (0-indexed)
    target = len(nums) - k

    def quickselect(left, right):
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        store = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]
        if store == target:
            return nums[store]
        elif store < target:
            return quickselect(store + 1, right)
        else:
            return quickselect(left, store - 1)

    return quickselect(0, len(nums) - 1)


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
