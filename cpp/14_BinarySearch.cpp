/*
 * Q14. Binary Search (Category: Binary Search)
 *
 * Problem: Search for a target in a sorted array. Return its index or -1.
 *
 * Approach: Classic binary search — narrow the search space by halving each iteration.
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
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    cout << search(nums, 9)  << endl; // 4
    cout << search(nums, 2)  << endl; // -1
    return 0;
}
