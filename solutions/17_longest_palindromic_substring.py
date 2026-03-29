"""
17. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example:
    Input: s = "babad"
    Output: "bab" (or "aba")

    Input: s = "cbbd"
    Output: "bb"

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def longest_palindrome(s):
    start, max_len = 0, 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)      # Odd length palindromes
        expand(i, i + 1)  # Even length palindromes

    return s[start:start + max_len]


if __name__ == "__main__":
    print(longest_palindrome("babad"))   # "bab" or "aba"
    print(longest_palindrome("cbbd"))    # "bb"
    print(longest_palindrome("racecar")) # "racecar"
