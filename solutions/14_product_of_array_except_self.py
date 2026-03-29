"""
14. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

Solve it without using division and in O(n) time.

Example:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Time Complexity: O(n)
Space Complexity: O(1) (output array not counted)
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Left pass: result[i] = product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right pass: multiply by product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))    # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
