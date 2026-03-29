"""
Q14. Binary Search (Category: Binary Search)

Problem: Search for a target in a sorted array. Return its index or -1.

Approach: Classic binary search — halve the search space each iteration.

Time Complexity : O(log n)
Space Complexity: O(1)
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
