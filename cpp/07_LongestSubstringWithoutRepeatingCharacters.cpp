/*
 * Q7. Longest Substring Without Repeating Characters (Category: Strings)
 *
 * Problem: Find the length of the longest substring with no repeated characters.
 *
 * Approach: Sliding window with an unordered_map storing the last seen index.
 *           Move the left pointer past the duplicate when one is found.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(min(n, m))  m = charset size
 */
#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> lastIndex;
    int maxLen = 0, left = 0;

    for (int right = 0; right < (int)s.length(); right++) {
        char c = s[right];
        if (lastIndex.count(c) && lastIndex[c] >= left) {
            left = lastIndex[c] + 1;
        }
        lastIndex[c] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}

int main() {
    cout << lengthOfLongestSubstring("abcabcbb") << endl; // 3
    cout << lengthOfLongestSubstring("bbbbb")    << endl; // 1
    cout << lengthOfLongestSubstring("pwwkew")   << endl; // 3
    return 0;
}
