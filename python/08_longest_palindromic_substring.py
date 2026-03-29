"""
Q8. Longest Palindromic Substring (Category: Strings)

Problem: Find the longest palindromic substring in a string.

Approach: Expand-around-center. For each position try both odd and even-length
          palindromes and track the longest found.

Time Complexity : O(n²)
Space Complexity: O(1)
"""


def longest_palindrome(s: str) -> str:
    start, max_len = 0, 1

    def expand(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        length = right - left - 1
        if length > max_len:
            max_len = length
            start = left + 1

    for i in range(len(s)):
        expand(i, i)      # Odd-length palindrome
        expand(i, i + 1)  # Even-length palindrome

    return s[start : start + max_len]


if __name__ == "__main__":
    print(longest_palindrome("babad"))  # "bab" or "aba"
    print(longest_palindrome("cbbd"))   # "bb"
    print(longest_palindrome("a"))      # "a"
