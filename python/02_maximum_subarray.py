"""
Q2. Maximum Subarray – Kadane's Algorithm (Category: Arrays)

Problem: Find the contiguous subarray with the largest sum.

Approach: Track current_sum. If adding the next element is worse than starting
          fresh, restart. Update max_sum at every step.

Time Complexity : O(n)
Space Complexity: O(1)
"""


def max_sub_array(nums: list[int]) -> int:
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sub_array([1]))                                # 1
    print(max_sub_array([5, 4, -1, 7, 8]))                  # 23
