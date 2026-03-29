"""
Q3. Move Zeros (Category: Arrays)

Problem: Move all zeros to the end of the array in-place while maintaining
         the relative order of non-zero elements.

Approach: Two-pointer. insert_pos tracks where the next non-zero element goes.

Time Complexity : O(n)
Space Complexity: O(1)
"""


def move_zeroes(nums: list[int]) -> None:
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)  # [1, 3, 12, 0, 0]
