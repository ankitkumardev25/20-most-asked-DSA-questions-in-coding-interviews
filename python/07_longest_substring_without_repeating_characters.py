"""
Q7. Longest Substring Without Repeating Characters (Category: Strings)

Problem: Find the length of the longest substring with no repeated characters.

Approach: Sliding window. Use a dict to track the last seen index of each char.
          Move the left pointer past the duplicate when one is found.

Time Complexity : O(n)
Space Complexity: O(min(n, m))  m = charset size
"""


def length_of_longest_substring(s: str) -> int:
    last_index: dict[str, int] = {}
    max_len = left = 0

    for right, char in enumerate(s):
        if char in last_index and last_index[char] >= left:
            left = last_index[char] + 1
        last_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
