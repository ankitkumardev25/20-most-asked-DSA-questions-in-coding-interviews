"""
Q9. String to Integer (atoi) (Category: Strings)

Problem: Implement myAtoi — convert a string to a 32-bit signed integer.
         Handle leading whitespace, optional sign, non-digit termination, overflow.

Time Complexity : O(n)
Space Complexity: O(1)
"""

INT_MAX = 2**31 - 1   #  2147483647
INT_MIN = -(2**31)    # -2147483648


def my_atoi(s: str) -> int:
    i, n = 0, len(s)
    result = 0
    sign = 1

    # Skip leading whitespace
    while i < n and s[i] == " ":
        i += 1

    # Handle optional sign
    if i < n and s[i] in ("+", "-"):
        sign = -1 if s[i] == "-" else 1
        i += 1

    # Read digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        if result * sign >= INT_MAX:
            return INT_MAX
        if result * sign <= INT_MIN:
            return INT_MIN
        i += 1

    return result * sign


if __name__ == "__main__":
    print(my_atoi("42"))              # 42
    print(my_atoi("   -42"))          # -42
    print(my_atoi("4193 with words")) # 4193
    print(my_atoi("-91283472332"))    # -2147483648
