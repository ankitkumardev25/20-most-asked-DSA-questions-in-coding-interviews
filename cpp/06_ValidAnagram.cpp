/*
 * Q6. Valid Anagram (Category: Strings)
 *
 * Problem: Return true if t is an anagram of s.
 *
 * Approach: Frequency count array of size 26.
 *           Increment for s, decrement for t. All must be zero.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;

    vector<int> count(26, 0);
    for (int i = 0; i < (int)s.length(); i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}

int main() {
    cout << boolalpha;
    cout << isAnagram("anagram", "nagaram") << endl; // true
    cout << isAnagram("rat", "car")         << endl; // false
    return 0;
}
