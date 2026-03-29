/**
 * Q6. Valid Anagram (Category: Strings)
 *
 * Problem: Given two strings s and t, return true if t is an anagram of s.
 *
 * Approach: Use a frequency count array of size 26 (for lowercase letters).
 *           Increment for each char in s, decrement for each char in t.
 *           If all counts are zero at the end, they are anagrams.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)  — fixed-size array of 26
 */
public class ValidAnagram {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        ValidAnagram solution = new ValidAnagram();
        System.out.println(solution.isAnagram("anagram", "nagaram")); // true
        System.out.println(solution.isAnagram("rat", "car"));         // false
    }
}
