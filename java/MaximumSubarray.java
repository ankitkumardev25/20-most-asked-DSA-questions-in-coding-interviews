/**
 * Q2. Maximum Subarray – Kadane's Algorithm (Category: Arrays)
 *
 * Problem: Find the contiguous subarray with the largest sum.
 *
 * Approach: Maintain a running currentSum. If it drops below zero, reset to 0.
 *           Track the maximum sum seen so far.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        MaximumSubarray solution = new MaximumSubarray();
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Max Subarray Sum: " + solution.maxSubArray(nums)); // 6
    }
}
