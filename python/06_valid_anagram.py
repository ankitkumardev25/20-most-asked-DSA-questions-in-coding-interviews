"""
Q6. Valid Anagram (Category: Strings)

Problem: Return True if t is an anagram of s.

Approach: Frequency count array of size 26 (lowercase letters only).
          Increment for s, decrement for t. All must be zero at the end.

Time Complexity : O(n)
Space Complexity: O(1)
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for a, b in zip(s, t):
        count[ord(a) - ord("a")] += 1
        count[ord(b) - ord("a")] -= 1
    return all(c == 0 for c in count)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
