/**
 * Q14. Binary Search (Category: Binary Search)
 *
 * Problem: Search for a target value in a sorted array. Return its index or -1.
 *
 * Approach: Classic binary search — compare mid element to target and
 *           halve the search space each iteration.
 *
 * Time Complexity : O(log n)
 * Space Complexity: O(1)
 */
public class BinarySearch {

    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Prevent overflow
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch solution = new BinarySearch();
        int[] nums = {-1, 0, 3, 5, 9, 12};
        System.out.println(solution.search(nums, 9));  // 4
        System.out.println(solution.search(nums, 2));  // -1
    }
}
