/**
 * Q5. Find the Duplicate Number (Category: Arrays)
 *
 * Problem: Given an array nums containing n+1 integers where each integer is in [1, n],
 *          find the duplicate number. Must not modify the array; O(1) extra space.
 *
 * Approach: Floyd's Cycle Detection (slow/fast pointers treated like a linked list).
 *           nums[i] acts as a "next" pointer. The duplicate creates the cycle entrance.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class FindDuplicateNumber {

    public int findDuplicate(int[] nums) {
        // Phase 1: Find intersection point inside the cycle
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Find cycle entrance (duplicate)
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }

    public static void main(String[] args) {
        FindDuplicateNumber solution = new FindDuplicateNumber();
        int[] nums = {1, 3, 4, 2, 2};
        System.out.println("Duplicate: " + solution.findDuplicate(nums)); // 2
    }
}
