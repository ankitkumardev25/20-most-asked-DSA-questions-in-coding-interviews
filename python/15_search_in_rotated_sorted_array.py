"""
Q15. Search in Rotated Sorted Array (Category: Binary Search)

Problem: Search a target in a sorted array that was rotated at an unknown pivot.

Approach: Modified binary search. Determine which half is sorted, then decide
          which half to search based on where the target falls.

Time Complexity : O(log n)
Space Complexity: O(1)
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(search([1], 0))                     # -1
