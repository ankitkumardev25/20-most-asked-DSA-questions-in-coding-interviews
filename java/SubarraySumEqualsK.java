import java.util.HashMap;

/**
 * Q19. Subarray Sum Equals K (Category: Sliding Window / Misc)
 *
 * Problem: Return the total number of subarrays whose sum equals k.
 *
 * Approach: Prefix sum + HashMap (frequency count).
 *           For every index i, if (prefixSum - k) has been seen before,
 *           those previous prefix sums form valid subarrays ending at i.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
public class SubarraySumEqualsK {

    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0, 1); // One way to have an empty prefix
        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {
            prefixSum += num;
            count += prefixCount.getOrDefault(prefixSum - k, 0);
            prefixCount.merge(prefixSum, 1, Integer::sum);
        }
        return count;
    }

    public static void main(String[] args) {
        SubarraySumEqualsK solution = new SubarraySumEqualsK();
        int[] nums1 = {1, 1, 1};
        System.out.println(solution.subarraySum(nums1, 2)); // 2
        int[] nums2 = {1, 2, 3};
        System.out.println(solution.subarraySum(nums2, 3)); // 2
    }
}
