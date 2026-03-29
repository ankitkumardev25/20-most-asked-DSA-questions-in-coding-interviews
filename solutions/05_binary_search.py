"""
5. Binary Search
Given an array of integers nums sorted in ascending order and an integer target,
write a function to search target in nums. Return the index if target is found,
otherwise return -1.

Example:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # -1
    print(binary_search([5], 5))                      # 0
