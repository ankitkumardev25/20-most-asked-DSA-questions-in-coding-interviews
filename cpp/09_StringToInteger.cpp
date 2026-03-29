/*
 * Q9. String to Integer (atoi) (Category: Strings)
 *
 * Problem: Implement myAtoi — convert a string to a 32-bit signed integer.
 *          Handle leading whitespace, optional sign, non-digit termination, overflow.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <string>
#include <climits>
using namespace std;

int myAtoi(string s) {
    int i = 0, n = s.length();
    long result = 0;
    int sign = 1;

    // Skip leading whitespace
    while (i < n && s[i] == ' ') i++;

    // Handle optional sign
    if (i < n && (s[i] == '+' || s[i] == '-')) {
        sign = (s[i] == '-') ? -1 : 1;
        i++;
    }

    // Read digits and clamp overflow
    while (i < n && isdigit(s[i])) {
        result = result * 10 + (s[i] - '0');
        if (result * sign >= INT_MAX) return INT_MAX;
        if (result * sign <= INT_MIN) return INT_MIN;
        i++;
    }
    return (int)(result * sign);
}

int main() {
    cout << myAtoi("42")             << endl; // 42
    cout << myAtoi("   -42")         << endl; // -42
    cout << myAtoi("4193 with words")<< endl; // 4193
    cout << myAtoi("-91283472332")   << endl; // -2147483648
    return 0;
}
