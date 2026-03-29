/**
 * Q15. Search in Rotated Sorted Array (Category: Binary Search)
 *
 * Problem: Search a target in a sorted array that has been rotated at an unknown pivot.
 *
 * Approach: Modified binary search. At each step, determine which half is sorted,
 *           then decide which half to search based on the target's range.
 *
 * Time Complexity : O(log n)
 * Space Complexity: O(1)
 */
public class SearchInRotatedSortedArray {

    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            // Left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        SearchInRotatedSortedArray solution = new SearchInRotatedSortedArray();
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        System.out.println(solution.search(nums, 0)); // 4
        System.out.println(solution.search(nums, 3)); // -1
    }
}
