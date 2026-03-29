"""
Q18. Longest Subarray with Sum K (Category: Sliding Window / Misc)

Problem: Find the length of the longest contiguous subarray with sum = k.
         (Array may contain negatives or zeros.)

Approach: Prefix sum + dict.
          Store the earliest index where each prefix sum first occurred.
          If (prefix_sum - k) is in the dict, we found a valid subarray.

Time Complexity : O(n)
Space Complexity: O(n)
"""


def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
    prefix_sum_index: dict[int, int] = {0: -1}
    prefix_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in prefix_sum_index:
            max_len = max(max_len, i - prefix_sum_index[prefix_sum - k])
        # Store only the earliest occurrence
        if prefix_sum not in prefix_sum_index:
            prefix_sum_index[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    print(longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3))  # 4
    print(longest_subarray_with_sum_k([-2, -1, 2, 1], 1))     # 2
