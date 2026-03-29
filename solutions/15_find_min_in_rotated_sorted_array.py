"""
15. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between
1 and n times. Find the minimum element.

Example:
    Input: nums = [3, 4, 5, 1, 2]
    Output: 1

    Input: nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))        # 1
    print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(find_min([11, 13, 15, 17]))        # 11
