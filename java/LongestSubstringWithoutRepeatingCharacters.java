import java.util.HashMap;

/**
 * Q7. Longest Substring Without Repeating Characters (Category: Strings)
 *
 * Problem: Find the length of the longest substring without repeating characters.
 *
 * Approach: Sliding window. Use a HashMap to store the last seen index of each
 *           character. Move the left pointer past the duplicate when one is found.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(min(n, m))  where m is charset size
 */
public class LongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> lastIndex = new HashMap<>();
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastIndex.containsKey(c) && lastIndex.get(c) >= left) {
                left = lastIndex.get(c) + 1;
            }
            lastIndex.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters solution =
                new LongestSubstringWithoutRepeatingCharacters();
        System.out.println(solution.lengthOfLongestSubstring("abcabcbb")); // 3
        System.out.println(solution.lengthOfLongestSubstring("bbbbb"));    // 1
        System.out.println(solution.lengthOfLongestSubstring("pwwkew"));   // 3
    }
}
