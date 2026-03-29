/**
 * Q8. Longest Palindromic Substring (Category: Strings)
 *
 * Problem: Find the longest palindromic substring in a given string.
 *
 * Approach: Expand-around-center. For each position, expand outward for both
 *           odd-length and even-length palindromes and track the longest found.
 *
 * Time Complexity : O(n²)
 * Space Complexity: O(1)
 */
public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        if (s.length() < 2) return s;
        int start = 0, maxLen = 1;
        for (int i = 0; i < s.length() - 1; i++) {
            int len1 = expandAroundCenter(s, i, i);     // Odd length
            int len2 = expandAroundCenter(s, i, i + 1); // Even length
            int len  = Math.max(len1, len2);
            if (len > maxLen) {
                maxLen = len;
                start  = i - (len - 1) / 2;
            }
        }
        return s.substring(start, start + maxLen);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // left and right are now one step outside the palindrome
        return right - left - 1;
    }

    public static void main(String[] args) {
        LongestPalindromicSubstring solution = new LongestPalindromicSubstring();
        System.out.println(solution.longestPalindrome("babad")); // "bab" or "aba"
        System.out.println(solution.longestPalindrome("cbbd"));  // "bb"
    }
}
