/*
 * Q15. Search in Rotated Sorted Array (Category: Binary Search)
 *
 * Problem: Search a target in a sorted array that was rotated at an unknown pivot.
 *
 * Approach: Modified binary search. Determine which half is sorted at each step,
 *           then narrow the search window based on the target's range.
 *
 * Time Complexity : O(log n)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0, right = (int)nums.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;

        // Left half is sorted
        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) right = mid - 1;
            else left = mid + 1;
        } else {
            // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) left = mid + 1;
            else right = mid - 1;
        }
    }
    return -1;
}

int main() {
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    cout << search(nums, 0) << endl; // 4
    cout << search(nums, 3) << endl; // -1
    return 0;
}
