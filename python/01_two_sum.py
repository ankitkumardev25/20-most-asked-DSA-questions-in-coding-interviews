"""
Q1. Two Sum (Category: Arrays)

Problem: Given an array of integers nums and a target, return indices of the
         two numbers that add up to target.

Approach: Use a dict to map value -> index.
          For each element, check if (target - element) is already in the dict.

Time Complexity : O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))       # [1, 2]
