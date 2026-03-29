/*
 * Q8. Longest Palindromic Substring (Category: Strings)
 *
 * Problem: Find the longest palindromic substring in a string.
 *
 * Approach: Expand-around-center. For each position expand outward for both
 *           odd-length and even-length palindromes.
 *
 * Time Complexity : O(n²)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int expandAroundCenter(const string& s, int left, int right) {
    while (left >= 0 && right < (int)s.length() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1; // length of palindrome
}

string longestPalindrome(string s) {
    if (s.length() < 2) return s;
    int start = 0, maxLen = 1;

    for (int i = 0; i < (int)s.length() - 1; i++) {
        int len1 = expandAroundCenter(s, i, i);     // Odd
        int len2 = expandAroundCenter(s, i, i + 1); // Even
        int len  = max(len1, len2);
        if (len > maxLen) {
            maxLen = len;
            start  = i - (len - 1) / 2;
        }
    }
    return s.substr(start, maxLen);
}

int main() {
    cout << longestPalindrome("babad") << endl; // "bab" or "aba"
    cout << longestPalindrome("cbbd")  << endl; // "bb"
    return 0;
}
