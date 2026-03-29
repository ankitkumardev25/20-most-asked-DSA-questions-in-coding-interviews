"""
Q19. Subarray Sum Equals K (Category: Sliding Window / Misc)

Problem: Return the total number of subarrays whose sum equals k.

Approach: Prefix sum + frequency dict.
          For each index, count how many previous prefix sums equal (prefix_sum - k).

Time Complexity : O(n)
Space Complexity: O(n)
"""
from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    prefix_count: dict[int, int] = defaultdict(int)
    prefix_count[0] = 1
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))  # 2
    print(subarray_sum([1, 2, 3], 3))  # 2
