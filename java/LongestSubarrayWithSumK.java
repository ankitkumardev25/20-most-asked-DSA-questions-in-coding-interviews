import java.util.HashMap;

/**
 * Q18. Longest Subarray with Sum K (Category: Sliding Window / Misc)
 *
 * Problem: Find the length of the longest contiguous subarray whose sum equals k.
 *          (Array may contain negatives or zeros.)
 *
 * Approach: Prefix sum + HashMap.
 *           Store earliest index where a particular prefix sum occurred.
 *           If (prefixSum - k) is in the map, we found a valid subarray.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
public class LongestSubarrayWithSumK {

    public int longestSubarrayWithSumK(int[] nums, int k) {
        HashMap<Long, Integer> prefixSumIndex = new HashMap<>();
        prefixSumIndex.put(0L, -1); // Empty prefix at index -1
        long prefixSum = 0;
        int maxLen = 0;

        for (int i = 0; i < nums.length; i++) {
            prefixSum += nums[i];
            if (prefixSumIndex.containsKey(prefixSum - k)) {
                maxLen = Math.max(maxLen, i - prefixSumIndex.get(prefixSum - k));
            }
            // Store only the first (earliest) occurrence of this prefix sum
            prefixSumIndex.putIfAbsent(prefixSum, i);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LongestSubarrayWithSumK solution = new LongestSubarrayWithSumK();
        int[] nums = {1, -1, 5, -2, 3};
        System.out.println(solution.longestSubarrayWithSumK(nums, 3)); // 4
        int[] nums2 = {-2, -1, 2, 1};
        System.out.println(solution.longestSubarrayWithSumK(nums2, 1)); // 2
    }
}
